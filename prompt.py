"""LLM prompt template and topic list for the daily English monologue generator."""

TOPICS = [
    "늦잠 잔 아침에 하루를 시작하기",
    "책상 정리하기",
    "해야 할 일을 미루지 않기",
    "휴대폰을 너무 많이 보는 습관 줄이기",
    "운동하러 나가기 전 마음 다잡기",
    "하루 일과를 정리하기",
    "피곤하지만 작은 일부터 시작하기",
    "방 정리하기",
    "공부 시작 전 마음 정리하기",
    "자기 전에 하루를 돌아보기",
    "숙취로 힘든 아침에 오늘 하루 어떻게 보낼지 고민하기",
    "갑자기 컴퓨터나 일이 안 풀릴 때 혼잣말",
    "저녁 메뉴 뭐 먹을지 고민하기",
    "예상치 못한 귀찮은 일이 생겼을 때 대처 고민하기",
    "주말에 뭐 하고 놀지 고민하기",
    "가기 싫은 약속을 취소할지 말지 고민하기",
    "돈을 너무 많이 썼을 때 자책하기",
    "월요일 아침 출근하기 싫은 마음 달래기",
]

JSON_SCHEMA_EXAMPLE = """{
  "date": "YYYY-MM-DD",
  "title": "YYYY-MM-DD Daily English Monologue",
  "topic": "English topic title",
  "status": "Not Memorized",
  "english_monologue": ["sentence 1", "... 10 sentences total"],
  "literal_translation": ["sentence 1 literal Korean translation", "... 10 total"],
  "natural_translation": ["sentence 1 natural Korean translation", "... 10 total"],
  "sentence_study": [
    {
      "sentence_id": 1,
      "english": "sentence 1",
      "type": "simple or complex",
      "core_structure": "short structure explanation",
      "grammar_note": "short Korean grammar explanation",
      "useful_expression": "useful expression from the sentence"
    }
  ],
  "grammar_notes": [
    {"title": "grammar point", "explanation": "short Korean explanation", "example": "English example sentence"}
  ],
  "useful_expressions": [
    {"expression": "expression", "meaning": "Korean meaning", "example": "English example sentence"}
  ],
  "difficult_words": [
    {"word": "word", "meaning": "Korean meaning", "example": "English example sentence"}
  ],
  "memorization_sentences": ["key sentence 1", "key sentence 2", "key sentence 3"],
  "chunk_practice": [
    {"sentence": "key sentence 1", "chunks": ["chunk 1", "chunk 2", "chunk 3"]}
  ]
}"""


def build_prompt(date: str, topic: str) -> str:
    return f"""You are an English speaking coach who writes daily self-talk monologues for a Korean learner.

Write today's material for the date {date} on the topic: "{topic}".

Requirements:
- Write exactly 10 sentences that form a single natural, connected self-talk monologue (not disconnected example sentences).
- Use 3-5 simple sentences and 5-7 complex sentences. Complex sentences may use relative clauses, relative adverb clauses, adverbial clauses, conditional clauses, time clauses, multiple connected clauses, or chains of prepositional/adverbial phrases.
- Use everyday phrasal verbs and natural spoken expressions a native speaker would actually use. Avoid academic, literary, or overly dramatic language.
- Tone: this should sound like a real, unfiltered inner monologue, not a self-help pep talk. Include genuine hesitation and rhetorical self-questions ("Why isn't this working?", "Should I just...?", "What am I even going to do about...?"), mild complaining, indecision between options, and small mundane worries. Avoid neat, resolved, motivational endings — real self-talk is often messy, unresolved, or trails off. For example, a monologue about a rough hungover morning might sound like: "Ugh, why is this suddenly not working. My head is pounding — I probably drank way too much last night. Should I just take the afternoon off and head home early? What would I even do once I get home, though. Do I even have anything to eat at home. Maybe I should just order something for dinner. I'm not feeling great right now, so..." Match that level of realism and rhetorical questioning regardless of the topic given below.
- Include about 3 moderately difficult but commonly used words (e.g. overwhelmed, tedious, relieved, cluttered, distracted, hesitant) that are useful but not too technical.
- literal_translation: word-for-word Korean translation preserving English sentence structure, even if awkward, for structural/reading-speed practice.
- natural_translation: natural, casual (반말) Korean translation that conveys the real meaning.
- sentence_study: for every one of the 10 sentences, provide sentence_id, english, type ("simple" or "complex"), core_structure, a short Korean grammar_note, and one useful_expression drawn from that sentence.
- grammar_notes: the key grammar points appearing in today's sentences (e.g. before + S + V, even though + S + V, once + S + V, the thing that + S + V, as if + S + V, if + S + V), each with a short Korean explanation and an English example.
- useful_expressions: the phrasal verbs / everyday expressions used today (e.g. talk oneself out of something, clean up, put on, end up -ing, sleep in, stay up, put off, pile up, figure out, break down, throw away, get through), each with Korean meaning and an English example.
- difficult_words: exactly 3 words, each with the word, its Korean meaning, and an English example sentence.
- memorization_sentences: exactly 3 sentences, and they MUST be selected verbatim from english_monologue. Prefer sentences that best showcase phrasal verbs, grammar structures, or everyday expressions, and that are useful for speaking practice.
- chunk_practice: exactly 3 entries, one per memorization sentence, with "sentence" matching the memorization_sentences text exactly, broken into natural speaking chunks.
- Include natural English sentences in which signs, notices, instructions, maps, schedules, messages, documents, or other information sources act as the subject and "say," "tell," "show," "suggest," or "indicate" something. For example: "The sign said not to turn right," "The schedule says the train leaves at six," or "The instructions tell you to restart the device." Use these English-style structures when Korean would more naturally describe the rule, information, or situation without making the object the grammatical subject.
- status must be exactly "Not Memorized".
- title must be exactly "{date} Daily English Monologue".

Return ONLY valid JSON matching this exact structure (no markdown fences, no extra commentary):

{JSON_SCHEMA_EXAMPLE}
"""
