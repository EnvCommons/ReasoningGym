"""Test agent for reasoning-gym environments.

This script demonstrates how to use the reasoning-gym environments
with OpenReward and an LLM provider (OpenAI by default).
"""

import asyncio
import json
import os

from openai import AsyncOpenAI
from openreward import AsyncOpenReward

# Configuration
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4")
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
ENV_NAME = os.environ.get("ENV_NAME", "local/BasicArithmetic")
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8080")


async def test_single_task(env_name: str, task_index: int = 0) -> None:
    """Test a single task from the specified environment.

    Args:
        env_name: Name of the environment (e.g., "local/BasicArithmetic")
        task_index: Index of the task to test (default: 0)
    """
    or_client = AsyncOpenReward()
    oai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    # Get environment and list tasks
    environment = or_client.environments.get(name=env_name, base_url=BASE_URL, variant="familyrelationships")
    tasks = await environment.list_tasks(split="train")
    tools = await environment.list_tools(format="openai")

    print(f"\n{'=' * 80}")
    print(f"Testing environment: {env_name}")
    print(f"Total tasks available: {len(tasks)}")
    print(f"{'=' * 80}\n")

    if task_index >= len(tasks):
        print(f"Error: Task index {task_index} out of range (0-{len(tasks)-1})")
        return

    task = tasks[task_index]
    print(f"Testing task {task_index}: {task}\n")

    # Start session
    async with environment.session(task=task) as session:
        # Get the initial prompt
        prompt = await session.get_prompt()
        prompt_text = prompt[0].text if isinstance(prompt, list) else prompt

        print(f"Question: {prompt_text}\n")

        # Create input for LLM
        input_list = [{"role": "user", "content": prompt_text}]

        # Get response from LLM
        print("Waiting for model response...")
        response = await oai_client.responses.create(
            model=MODEL_NAME,
            tools=tools,
            input=input_list,
        )

        # Process response and extract tool calls
        for item in response.output:
            if item.type == "function_call":
                print(f"\nModel called tool: {item.name}")
                print(f"Arguments: {item.arguments}")

                # Execute the tool
                tool_result = await session.call_tool(
                    item.name,
                    json.loads(str(item.arguments)),
                )

                # Display results
                print(f"\n{'─' * 80}")
                print(f"Tool result:")
                print(f"  Reward: {tool_result.reward:.3f}")
                print(f"  Finished: {tool_result.finished}")
                if tool_result.blocks:
                    print(f"  Feedback: {tool_result.blocks[0].text}")
                print(f"{'─' * 80}\n")

                # Print metadata for debugging
                if tool_result.metadata:
                    print("Metadata:")
                    for key, value in tool_result.metadata.items():
                        print(f"  {key}: {value}")

                return

        # If no tool was called, the model might have just responded with text
        print("\nModel did not call any tools. Response:")
        for item in response.output:
            if hasattr(item, "text"):
                print(f"  {item.text}")


async def test_multiple_tasks(env_name: str, num_tasks: int = 3) -> None:
    """Test multiple tasks from the specified environment.

    Args:
        env_name: Name of the environment
        num_tasks: Number of tasks to test
    """
    print(f"\nTesting {num_tasks} tasks from {env_name}...\n")

    for i in range(num_tasks):
        await test_single_task(env_name, task_index=i)
        print("\n" + "=" * 80 + "\n")


async def main() -> None:
    """Main entry point for testing."""
    # Test a single task from the default environment
    await test_single_task(ENV_NAME, task_index=0)

    # Uncomment to test multiple tasks:
    # await test_multiple_tasks(ENV_NAME, num_tasks=3)

    # Uncomment to test a different environment:
    # await test_single_task("local/KnightsKnaves", task_index=0)


if __name__ == "__main__":
    asyncio.run(main())
