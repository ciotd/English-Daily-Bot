"""Convert the validated daily-content JSON into Notion block children."""

MAX_TEXT_LEN = 2000


def _text(content: str, bold: bool = False, italic: bool = False) -> dict:
    return {
        "type": "text",
        "text": {"content": content[:MAX_TEXT_LEN]},
        "annotations": {"bold": bold, "italic": italic},
    }


def _rich(*parts: dict) -> list:
    return list(parts)


def heading_2(text: str) -> dict:
    return {
        "object": "block",
        "type": "heading_2",
        "heading_2": {"rich_text": _rich(_text(text, bold=True))},
    }


def heading_3(text: str) -> dict:
    return {
        "object": "block",
        "type": "heading_3",
        "heading_3": {"rich_text": _rich(_text(text, bold=True))},
    }


def paragraph(*rich_text_parts: dict) -> dict:
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": list(rich_text_parts)},
    }


def numbered_list_item(*rich_text_parts: dict) -> dict:
    return {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {"rich_text": list(rich_text_parts)},
    }


def bulleted_list_item(*rich_text_parts: dict) -> dict:
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": list(rich_text_parts)},
    }


def _section_english_monologue(data: dict) -> list:
    blocks = [heading_2("1. English Monologue")]
    for sentence in data["english_monologue"]:
        blocks.append(numbered_list_item(_text(sentence)))
    return blocks


def _section_literal_translation(data: dict) -> list:
    blocks = [heading_2("2. Literal Translation")]
    for sentence in data["literal_translation"]:
        blocks.append(numbered_list_item(_text(sentence)))
    return blocks


def _section_natural_translation(data: dict) -> list:
    blocks = [heading_2("3. Natural Translation")]
    for sentence in data["natural_translation"]:
        blocks.append(numbered_list_item(_text(sentence)))
    return blocks


def _section_sentence_study(data: dict) -> list:
    blocks = [heading_2("4. Sentence-by-Sentence Study")]
    for item in data["sentence_study"]:
        blocks.append(heading_3(f"Sentence {item['sentence_id']} ({item['type']})"))
        blocks.append(paragraph(_text(item["english"], italic=True)))
        blocks.append(bulleted_list_item(_text("Core structure: ", bold=True), _text(item["core_structure"])))
        blocks.append(bulleted_list_item(_text("Grammar: ", bold=True), _text(item["grammar_note"])))
        blocks.append(bulleted_list_item(_text("Useful expression: ", bold=True), _text(item["useful_expression"])))
    return blocks


def _section_grammar_notes(data: dict) -> list:
    blocks = [heading_2("5. Grammar Notes")]
    for note in data["grammar_notes"]:
        blocks.append(bulleted_list_item(_text(f"{note['title']}: ", bold=True), _text(note["explanation"])))
        blocks.append(paragraph(_text(note["example"], italic=True)))
    return blocks


def _section_useful_expressions(data: dict) -> list:
    blocks = [heading_2("6. Useful Expressions")]
    for expr in data["useful_expressions"]:
        blocks.append(bulleted_list_item(_text(f"{expr['expression']}: ", bold=True), _text(expr["meaning"])))
        blocks.append(paragraph(_text(expr["example"], italic=True)))
    return blocks


def _section_difficult_words(data: dict) -> list:
    blocks = [heading_2("7. Difficult Words")]
    for word in data["difficult_words"]:
        blocks.append(bulleted_list_item(_text(f"{word['word']}: ", bold=True), _text(word["meaning"])))
        blocks.append(paragraph(_text(word["example"], italic=True)))
    return blocks


def _section_memorization_sentences(data: dict) -> list:
    blocks = [heading_2("8. Memorization Sentences")]
    for sentence in data["memorization_sentences"]:
        blocks.append(numbered_list_item(_text(sentence, bold=True)))
    return blocks


def _section_chunk_practice(data: dict) -> list:
    blocks = [heading_2("9. Chunk Practice")]
    for entry in data["chunk_practice"]:
        blocks.append(paragraph(_text(entry["sentence"], bold=True)))
        blocks.append(bulleted_list_item(_text(" / ".join(entry["chunks"]))))
    return blocks


def build_blocks(data: dict) -> list:
    """Build the full ordered list of Notion block children for the page body."""
    blocks = []
    blocks += _section_english_monologue(data)
    blocks += _section_literal_translation(data)
    blocks += _section_natural_translation(data)
    blocks += _section_sentence_study(data)
    blocks += _section_grammar_notes(data)
    blocks += _section_useful_expressions(data)
    blocks += _section_difficult_words(data)
    blocks += _section_memorization_sentences(data)
    blocks += _section_chunk_practice(data)
    return blocks
