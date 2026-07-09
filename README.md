# Daily English Notion Automation

매일 영어 혼잣말 독백문을 생성하고, 직역/의역/문법 설명/유용한 표현/암기 문장 등을 정리하여 Notion 데이터베이스에 저장하는 개인 영어 학습 자동화 프로젝트입니다.

## 1. 프로젝트 목적

이 프로젝트의 목적은 매일 외울 수 있는 영어 문장을 자동으로 생성하고, Notion에 학습 자료 형태로 저장하는 것입니다.

주요 목표는 다음과 같습니다.

- 매일 약 10문장 분량의 영어 독백문 생성
- 일상생활에서 실제로 혼잣말처럼 사용할 수 있는 문장 구성
- 간단한 문장과 복잡한 문장을 적절히 섞어 학습
- 일상에서 자주 쓰이는 구동사 표현 반복 학습
- 직역과 의역을 함께 제공하여 속독과 의미 이해를 동시에 훈련
- 간단한 문법 설명과 유용한 표현 정리
- 암기할 핵심 문장 3개와 chunk practice 제공
- Notion 데이터베이스에 매일 새 페이지로 자동 저장

## 2. 생성할 영어 콘텐츠 기준

매일 생성되는 영어 글은 다음 조건을 만족해야 합니다.

### 2.1 문장 수

- 정확히 10문장
- 하나의 자연스러운 독백처럼 연결된 글
- 서로 따로 떨어진 예문 형태가 아니라, 하나의 흐름을 가진 self-talk monologue

### 2.2 문장 구성

- 간단한 문장: 3~5개
- 복잡한 문장: 5~7개

복잡한 문장은 다음과 같은 구조를 포함할 수 있습니다.

- 관계대명사절
- 관계부사절
- 부사절
- 조건절
- 시간절
- 여러 개의 절이 연결된 문장
- 부사구/전치사구가 이어지는 문장

### 2.3 표현 기준

- 일상생활에서 실제로 자주 쓰이는 구동사 사용
- 원어민이 대화에서 자주 쓰는 자연스러운 표현 사용
- 너무 학문적이거나 문학적이거나 과하게 극적인 표현은 제외
- 말하기 연습에 바로 사용할 수 있는 자연스러운 톤 유지

### 2.4 어려운 단어

매일 약 3개 정도의 단어를 포함합니다.

조건은 다음과 같습니다.

- 일상생활에서 비교적 자주 쓰임
- 너무 전문적이지 않음
- 초급자에게는 약간 어렵지만 실용성이 있음

예시:

- overwhelmed
- tedious
- relieved
- cluttered
- distracted
- hesitant

## 3. 콘텐츠 주제

주제는 사용자가 평소 혼잣말로 중얼거릴 수 있는 일상적인 내용으로 설정합니다.

예시 주제:

- 늦잠 잔 아침에 하루를 시작하기
- 책상 정리하기
- 해야 할 일을 미루지 않기
- 휴대폰을 너무 많이 보는 습관 줄이기
- 운동하러 나가기 전 마음 다잡기
- 하루 일과를 정리하기
- 피곤하지만 작은 일부터 시작하기
- 방 정리하기
- 공부 시작 전 마음 정리하기
- 자기 전에 하루를 돌아보기

## 4. Notion 저장 방식

Notion에는 데이터베이스 형태로 저장합니다.

### 4.1 저장 방식

- Notion 데이터베이스에 매일 새 페이지 1개 생성
- 하나의 페이지에 날짜별로 누적하지 않음

### 4.2 Notion 페이지 제목

형식:

```text
YYYY-MM-DD Daily English Monologue
```

예시:

```text
2026-07-09 Daily English Monologue
```

### 4.3 Notion 데이터베이스 속성

사용할 속성은 다음과 같습니다.

| 속성 | 타입 | 설명 |
|---|---|---|
| Title | Title | 페이지 제목 |
| Date | Date | 생성 날짜 |
| Topic | Text 또는 Rich Text | 오늘의 독백 주제 |
| Status | Select | 암기 상태 |

### 4.4 Status 값

Status 속성은 복습 상태 관리를 위해 사용합니다.

추천 값:

```text
Not Memorized
Memorizing
Done
```

### 4.5 제외하기로 한 속성

다음 속성은 사용하지 않습니다.

- Difficulty
- Sentence Count

이유:

- 처음에는 구조를 단순하게 유지하기 위함
- 모든 글이 기본적으로 10문장으로 고정되므로 Sentence Count가 불필요함
- 난이도는 초기에 Medium 수준으로 암묵적으로 유지하면 충분함

## 5. Notion 페이지 본문 구조

각 Notion 페이지의 본문은 다음 순서로 구성합니다.

```text
1. English Monologue
2. Literal Translation
3. Natural Translation
4. Sentence-by-Sentence Study
5. Grammar Notes
6. Useful Expressions
7. Difficult Words
8. Memorization Sentences
9. Chunk Practice
```

### 5.1 English Monologue

영어 독백문 전체를 먼저 제공합니다.

목적:

- 외우기 전에 전체 흐름 파악
- 실제 말하기용 독백으로 사용
- 문장들이 자연스럽게 연결되는지 확인

### 5.2 Literal Translation

직역입니다.

목적:

- 영어 어순 파악
- 속독 훈련
- 문장 구조 이해

특징:

- 자연스러운 한국어보다 영어 구조를 최대한 살림
- 어색해도 구조 이해를 우선함

### 5.3 Natural Translation

의역입니다.

목적:

- 실제 의미 이해
- 자연스러운 한국어 감각으로 내용 파악

특징:

- 자연스러운 반말 한국어 사용
- 영어 문장을 한국어식으로 자연스럽게 풀어줌

### 5.4 Sentence-by-Sentence Study

문장별 학습 섹션입니다.

각 문장마다 다음 내용을 정리합니다.

- 영어 문장
- 문장 유형: simple 또는 complex
- 핵심 구조
- 간단한 문법 설명
- 유용한 표현

### 5.5 Grammar Notes

그날 문장에서 중요한 문법 포인트를 짧게 정리합니다.

예시:

- before + S + V
- even though + S + V
- once + S + V
- the thing that + S + V
- as if + S + V
- if + S + V

### 5.6 Useful Expressions

구동사와 일상 표현을 정리합니다.

예시:

- talk oneself out of something
- clean up
- put on
- end up -ing
- sleep in
- stay up
- put off
- pile up
- figure out
- break down
- throw away
- get through

### 5.7 Difficult Words

약간 어렵지만 자주 쓰이는 단어 3개를 정리합니다.

각 단어마다 다음 내용을 포함합니다.

- 단어
- 한국어 의미
- 영어 예문

### 5.8 Memorization Sentences

그날 반드시 외울 핵심 문장 3개를 제공합니다.

조건:

- 반드시 English Monologue 안에 있는 문장에서 선택
- 말하기에 유용한 문장 우선
- 구동사, 문법 구조, 일상 표현이 잘 들어간 문장 우선

### 5.9 Chunk Practice

암기 문장 3개만 chunk 단위로 나눕니다.

목적:

- 한 문장을 통째로 외우기 전에 말하기 단위로 분해
- 자연스러운 리듬으로 따라 말하기
- 긴 문장에 대한 부담 줄이기

## 6. LLM 출력 방식

LLM 응답은 일반 텍스트가 아니라 JSON으로 받습니다.

이유:

- Python에서 파싱하기 쉬움
- Notion 블록으로 변환하기 쉬움
- 항목 누락 여부를 검증하기 쉬움
- 자동화 안정성이 높아짐

## 7. JSON 스키마

Gemini API가 반환해야 하는 기본 JSON 구조는 다음과 같습니다.

```json
{
  "date": "YYYY-MM-DD",
  "title": "YYYY-MM-DD Daily English Monologue",
  "topic": "English topic title",
  "status": "Not Memorized",
  "english_monologue": [
    "sentence 1",
    "sentence 2",
    "sentence 3",
    "sentence 4",
    "sentence 5",
    "sentence 6",
    "sentence 7",
    "sentence 8",
    "sentence 9",
    "sentence 10"
  ],
  "literal_translation": [
    "sentence 1 literal Korean translation",
    "sentence 2 literal Korean translation",
    "sentence 3 literal Korean translation",
    "sentence 4 literal Korean translation",
    "sentence 5 literal Korean translation",
    "sentence 6 literal Korean translation",
    "sentence 7 literal Korean translation",
    "sentence 8 literal Korean translation",
    "sentence 9 literal Korean translation",
    "sentence 10 literal Korean translation"
  ],
  "natural_translation": [
    "sentence 1 natural Korean translation",
    "sentence 2 natural Korean translation",
    "sentence 3 natural Korean translation",
    "sentence 4 natural Korean translation",
    "sentence 5 natural Korean translation",
    "sentence 6 natural Korean translation",
    "sentence 7 natural Korean translation",
    "sentence 8 natural Korean translation",
    "sentence 9 natural Korean translation",
    "sentence 10 natural Korean translation"
  ],
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
    {
      "title": "grammar point",
      "explanation": "short Korean explanation",
      "example": "English example sentence"
    }
  ],
  "useful_expressions": [
    {
      "expression": "expression",
      "meaning": "Korean meaning",
      "example": "English example sentence"
    }
  ],
  "difficult_words": [
    {
      "word": "word",
      "meaning": "Korean meaning",
      "example": "English example sentence"
    }
  ],
  "memorization_sentences": [
    "key sentence 1",
    "key sentence 2",
    "key sentence 3"
  ],
  "chunk_practice": [
    {
      "sentence": "key sentence 1",
      "chunks": [
        "chunk 1",
        "chunk 2",
        "chunk 3"
      ]
    },
    {
      "sentence": "key sentence 2",
      "chunks": [
        "chunk 1",
        "chunk 2",
        "chunk 3"
      ]
    },
    {
      "sentence": "key sentence 3",
      "chunks": [
        "chunk 1",
        "chunk 2",
        "chunk 3"
      ]
    }
  ]
}
```

## 8. JSON 검증 규칙

Python 코드에서 다음 항목을 검증합니다.

- `english_monologue`: 정확히 10개
- `literal_translation`: 정확히 10개
- `natural_translation`: 정확히 10개
- `sentence_study`: 정확히 10개
- `memorization_sentences`: 정확히 3개
- `chunk_practice`: 정확히 3개
- `memorization_sentences`는 반드시 `english_monologue` 안의 문장에서 선택
- `chunk_practice`의 sentence는 `memorization_sentences`와 일치

## 9. 사용할 API

### 9.1 기본 LLM API

초기 버전에서는 Gemini API를 사용합니다.

이유:

- 무료 티어로 시작하기 쉬움
- 하루 1회 생성 수준에서는 비용 부담이 적음
- JSON 출력 실험에 적합함

### 9.2 보조 옵션

Claude API key도 보유하고 있지만, 비용 사용량을 줄이기 위해 기본값으로 사용하지 않습니다.

향후 구조:

```text
기본 생성: Gemini API
예비 생성 또는 품질 개선: Claude API
```

### 9.3 OpenAI API

ChatGPT Plus 구독과 OpenAI API 과금은 별도입니다.

따라서 현재 프로젝트 초기 단계에서는 OpenAI API를 기본으로 사용하지 않습니다.

## 10. 프로젝트 폴더 구조

추천 구조는 다음과 같습니다.

```text
daily_english_notion/
├── main.py
├── prompt.py
├── llm_client.py
├── notion_client.py
├── formatter.py
├── daily_english_output.json
├── README.md
└── .env
```

각 파일의 역할은 다음과 같습니다.

| 파일 | 역할 |
|---|---|
| `main.py` | 전체 실행 흐름 관리 |
| `prompt.py` | LLM 프롬프트 저장 |
| `llm_client.py` | Gemini API 호출 및 JSON 생성 |
| `formatter.py` | JSON 데이터를 Notion 블록 구조로 변환 |
| `notion_client.py` | Notion API로 페이지 생성 |
| `.env` | API key, Notion DB ID 저장 |
| `daily_english_output.json` | 생성된 JSON 결과 확인용 파일 |
| `README.md` | 프로젝트 설명 문서 |

## 11. `.env` 구조

초기 Gemini 테스트 단계:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Notion 연동 단계 이후:

```env
GEMINI_API_KEY=your_gemini_api_key
NOTION_API_KEY=your_notion_integration_secret
NOTION_DATABASE_ID=your_notion_database_id
```

Claude fallback을 추가할 경우:

```env
CLAUDE_API_KEY=your_claude_api_key
```

## 12. 개발 단계

### Step 1. Notion 저장 구조 결정

완료됨.

결정사항:

- 데이터베이스에 매일 새 페이지 생성
- 페이지 본문은 B 방식 사용
  - 영어 독백 전체 먼저 제공
  - 아래에 직역/의역/문법/표현 정리
- Status 속성 포함
- Difficulty, Sentence Count 속성 제외

### Step 2. JSON 구조 결정

완료됨.

결정사항:

- 직역과 의역은 각각 문장별 배열로 분리
- sentence_study에 문장별 문법 설명 포함
- chunk_practice는 전체 문장이 아니라 암기 문장 3개에만 제공

### Step 3. 프롬프트 작성

완료됨.

`prompt.py`에 저장할 프롬프트를 정의합니다.

### Step 4. Gemini API 연결

진행 예정.

목표:

- Gemini API로 JSON 생성
- `daily_english_output.json` 파일로 저장
- Notion 연동 전, JSON 생성 안정성 확인

### Step 5. Notion formatter 작성

진행 예정.

목표:

- JSON 데이터를 Notion block 구조로 변환
- 제목, 문단, 번호 목록, 불릿 목록 등을 구성

### Step 6. Notion API 연결

진행 예정.

목표:

- Notion 데이터베이스에 새 페이지 생성
- 속성 입력
  - Title
  - Date
  - Topic
  - Status
- 본문 children 블록 삽입

### Step 7. 실행 자동화

선택 사항.

가능한 방식:

- 수동 실행
- Windows 작업 스케줄러
- cron
- GitHub Actions
- Notion 버튼 또는 외부 자동화 도구 연동

초기에는 수동 실행을 추천합니다.

```bash
python main.py
```

## 13. 현재 최소 실행 흐름

초기 목표는 다음 흐름입니다.

```text
main.py 실행
→ Gemini API 호출
→ JSON 생성
→ JSON 검증
→ daily_english_output.json 저장
```

Notion 연동 이후 최종 흐름은 다음과 같습니다.

```text
main.py 실행
→ Gemini API 호출
→ JSON 생성
→ JSON 검증
→ Notion 블록으로 변환
→ Notion DB에 새 페이지 생성
→ 학습 자료 저장 완료
```

## 14. 설치 패키지

초기 Gemini 테스트용:

```bash
pip install google-genai python-dotenv
```

Notion API 연동용:

```bash
pip install requests
```

## 15. 초기 실행 명령어

프로젝트 폴더 생성:

```bash
mkdir daily_english_notion
cd daily_english_notion
```

파일 생성:

```bash
touch main.py prompt.py llm_client.py notion_client.py formatter.py .env README.md
```

Windows PowerShell:

```powershell
mkdir daily_english_notion
cd daily_english_notion

New-Item main.py
New-Item prompt.py
New-Item llm_client.py
New-Item notion_client.py
New-Item formatter.py
New-Item .env
New-Item README.md
```

실행:

```bash
python main.py
```

## 16. 향후 개선 아이디어

향후 다음 기능을 추가할 수 있습니다.

- 주제 자동 순환
- 사용자가 원하는 주제 직접 입력
- 난이도 자동 조절
- 이전에 배운 구동사 재사용
- 복습 주기 자동 생성
- Notion에서 Status가 Done이 아닌 글만 복습 목록으로 추출
- Claude API fallback 추가
- JSON 생성 실패 시 자동 재시도
- 매일 생성된 문장 중 표현 bank 자동 누적
- `/recap`, `/bank`, `/drill` 같은 학습 명령어와 연결

## 17. 프로젝트 핵심 요약

이 프로젝트는 단순히 영어 문장을 생성하는 도구가 아니라, 매일 반복 가능한 영어 말하기 학습 시스템입니다.

핵심은 다음과 같습니다.

```text
일상 독백 생성
→ 직역으로 구조 이해
→ 의역으로 의미 이해
→ 문법/표현 정리
→ 핵심 문장 3개 암기
→ chunk 단위로 말하기 연습
→ Notion에 누적
→ 장기 복습
```

초기 버전은 단순하게 시작합니다.

```text
Gemini API + JSON 출력 + Notion DB 저장
```

이후 필요에 따라 Claude API, 자동 복습, 표현 bank, 난이도 조절 기능을 확장합니다.
