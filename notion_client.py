"""Create a new page in the Notion database for today's English content."""

import os

import requests

NOTION_VERSION = "2022-06-28"
NOTION_BASE_URL = "https://api.notion.com/v1"
BATCH_SIZE = 100


def _headers() -> dict:
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        raise RuntimeError("NOTION_API_KEY is not set in the environment")
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _build_properties(data: dict) -> dict:
    return {
        "Title": {"title": [{"text": {"content": data["title"]}}]},
        "Date": {"date": {"start": data["date"]}},
        "Topic": {"rich_text": [{"text": {"content": data["topic"]}}]},
        "Status": {"select": {"name": data["status"]}},
    }


def create_daily_page(data: dict, blocks: list) -> dict:
    """Create a new page in the Notion database and append all body blocks."""
    database_id = os.getenv("NOTION_DATABASE_ID")
    if not database_id:
        raise RuntimeError("NOTION_DATABASE_ID is not set in the environment")

    payload = {
        "parent": {"database_id": database_id},
        "properties": _build_properties(data),
        "children": blocks[:BATCH_SIZE],
    }

    response = requests.post(f"{NOTION_BASE_URL}/pages", headers=_headers(), json=payload)
    response.raise_for_status()
    page = response.json()
    page_id = page["id"]

    remaining = blocks[BATCH_SIZE:]
    for i in range(0, len(remaining), BATCH_SIZE):
        batch = remaining[i : i + BATCH_SIZE]
        append_response = requests.patch(
            f"{NOTION_BASE_URL}/blocks/{page_id}/children",
            headers=_headers(),
            json={"children": batch},
        )
        append_response.raise_for_status()

    return page
