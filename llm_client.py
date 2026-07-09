"""Gemini API call and JSON validation for the daily English monologue generator."""

import json
import os

from google import genai

from prompt import build_prompt

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def _get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in the environment")
    return genai.Client(api_key=api_key)


def generate_daily_content(date: str, topic: str) -> dict:
    """Call Gemini and return the parsed JSON content for the given date/topic."""
    client = _get_client()
    prompt = build_prompt(date, topic)

    response = client.models.generate_content(
        model=DEFAULT_MODEL,
        contents=prompt,
        config={"response_mime_type": "application/json"},
    )

    return json.loads(response.text)


def validate_content(data: dict) -> None:
    """Validate the JSON structure per the rules in section 8 of the README.

    Raises ValueError with a descriptive message on the first violation found.
    """

    def _require_len(key: str, expected: int) -> None:
        value = data.get(key)
        if not isinstance(value, list) or len(value) != expected:
            actual = len(value) if isinstance(value, list) else type(value).__name__
            raise ValueError(f"'{key}' must contain exactly {expected} items, got {actual}")

    _require_len("english_monologue", 10)
    _require_len("literal_translation", 10)
    _require_len("natural_translation", 10)
    _require_len("sentence_study", 10)
    _require_len("memorization_sentences", 3)
    _require_len("chunk_practice", 3)

    monologue = set(data["english_monologue"])
    for sentence in data["memorization_sentences"]:
        if sentence not in monologue:
            raise ValueError(
                f"memorization sentence not found in english_monologue: {sentence!r}"
            )

    memorization = data["memorization_sentences"]
    chunk_sentences = [entry.get("sentence") for entry in data["chunk_practice"]]
    if chunk_sentences != memorization:
        raise ValueError(
            "chunk_practice sentences must match memorization_sentences "
            f"exactly (in order): {chunk_sentences!r} != {memorization!r}"
        )
