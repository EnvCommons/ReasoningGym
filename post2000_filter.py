"""Cheap regex-based post-2000-topic filter for reasoning-gym generated
question text. No LLM stage needed here -- procedurally-generated abstract
puzzles have essentially no genuine post-2000 knowledge dependency (measured
empirically: 3,090 sampled entries across all 104 datasets, only 5 datasets
had any hits at all, and those are either an incidental numeric/date
coincidence -- a random year or number range landing in the 2000s -- or a
fixed vocabulary pool that includes a handful of modern-sounding words, not a
genuine knowledge requirement). See base_env.py for how this is used to
build the "train_old" split.
"""
import re

YEAR_RE = re.compile(r"\b20\d{2}\b")

POST_2000_TERMS = [
    "iphone", "ipad", "ipod", "android phone", "smartphone", "smart phone",
    "app store", "macbook", "chromebook", "kindle", "airpods", "apple watch",
    "smartwatch", "smart tv", "fitbit", "gopro", "oculus", "vr headset",
    "facebook", "instagram", "tiktok", "snapchat", "whatsapp", "youtube",
    "reddit", "linkedin", "wikipedia", "gmail", "google maps", "myspace",
    "hulu", "spotify", "uber", "lyft", "airbnb", "doordash", "instacart",
    "venmo", "zelle", "skype", "zoom call", "zoom meeting", "onlyfans",
    "podcast", "selfie", "hashtag", "emoji", "social media", "streaming service",
    "dating app", "mobile app", "smart speaker", "alexa", "siri", "cortana",
    "chatgpt", "gpt-3", "gpt-4", "openai", "large language model",
    "cryptocurrency", "bitcoin", "ethereum", "blockchain", "nft",
    "9/11", "war on terror", "iraq war", "hurricane katrina", "fukushima",
    "brexit", "covid", "coronavirus", "omicron", "social distancing",
    "barack obama", "obama", "obamacare", "biden", "donald trump",
    "president trump", "joe biden", "president biden", "kamala harris",
    "elon musk", "mark zuckerberg", "black lives matter", "#metoo",
    "january 6", "capitol riot",
    "taylor swift", "justin bieber", "lady gaga", "billie eilish",
    "game of thrones", "breaking bad", "stranger things", "squid game",
    "marvel cinematic", "fortnite", "minecraft", "roblox", "pokemon go",
    "league of legends", "world of warcraft", "call of duty", "xbox",
    "playstation 3", "ps3", "ps4", "ps5", "nintendo switch",
]

_TERMS_RE = re.compile(r"\b(" + "|".join(re.escape(t) for t in POST_2000_TERMS) + r")\b", re.IGNORECASE)


def mentions_post_2000_topic(text: str) -> bool:
    return bool(YEAR_RE.search(text)) or bool(_TERMS_RE.search(text))
