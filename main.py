"""Entry point: generate today's English monologue and save it to Notion."""

import argparse
import json
import random
import sys
import time
from datetime import date as date_cls

from dotenv import load_dotenv
from google.genai.errors import APIError

from formatter import build_blocks
from llm_client import generate_daily_content, validate_content
from notion_client import create_daily_page
from prompt import TOPICS

OUTPUT_PATH = "daily_english_output.json"
MAX_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = 15


def generate_and_validate(today: str, topic: str) -> dict:
    last_error = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            data = generate_daily_content(today, topic)
            validate_content(data)
            return data
        except (ValueError, APIError) as exc:
            last_error = exc
            print(f"Attempt {attempt} failed: {exc}", file=sys.stderr)
            if attempt < MAX_ATTEMPTS:
                time.sleep(RETRY_BACKOFF_SECONDS * attempt)
    raise RuntimeError(f"Failed to generate valid content after {MAX_ATTEMPTS} attempts: {last_error}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate today's English monologue and save it to Notion.")
    parser.add_argument("--topic", help="Force a specific topic instead of a random one")
    parser.add_argument("--skip-notion", action="store_true", help="Only generate and save the JSON locally")
    args = parser.parse_args()

    load_dotenv()

    today = date_cls.today().isoformat()
    topic = args.topic or random.choice(TOPICS)

    print(f"Generating monologue for {today} on topic: {topic}")
    data = generate_and_validate(today, topic)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved generated content to {OUTPUT_PATH}")

    if args.skip_notion:
        print("--skip-notion set, not creating a Notion page.")
        return

    blocks = build_blocks(data)
    page = create_daily_page(data, blocks)
    print(f"Created Notion page: {page.get('url', page.get('id'))}")


if __name__ == "__main__":
    main()
