# Vibe Session Protocol

## Purpose
- 역할 기반 협업의 발화 순서와 산출물 반영 규칙을 고정한다.
- 대화가 길어져도 "파일이 Source of Truth"로 유지되게 한다.

---

## Default Turn Flow (권장 순서)

### 0) User (PM)
- 목표/범위/우선순위/제약을 제공한다.
- 질문에 답하고 최종 결정을 내린다.

### 1) Chief AI (Orchestrator)
- 이번 턴의 목적을 1줄로 고정한다.
- 확정된 결정 / 미결 질문 / 파일 작업 / 다음 액션(1~3)을 출력한다.

### 2) Analyst AI (Spec Structurer)
- spec/decision 후보/오픈질문/작업을 구조화한다.
- 필요 시 문서 업데이트 초안을 만든다.

### 3) Dev AI (Implementation) — 조건부
- 아래 조건 중 하나라도 만족할 때만 호출한다.
  - task_plan.md에 "Ready" 작업이 존재
  - 사용자(PM)가 구현을 명시적으로 요청
- 구현은 항상 POC 범위(MVP) 내에서만 한다.

### 4) QA AI (Quality & Risk) — 조건부
- 아래 조건 중 하나라도 만족할 때만 호출한다.
  - Acceptance Criteria가 정의됨
  - 구현 산출물이 생김(페이지/코드/스크립트 등)
- 결과는 must-fix / nice-to-have로 분리한다.

### 5) Librarian AI (File Memory)
- 이번 턴의 핵심을 "파일 변경"으로 환원한다.
- 결정/질문/작업이 각각 올바른 파일로 들어가도록 정리한다.

---

## File Update Rules (Single Source of Truth)

### Decisions
- "결정"은 decisions.md에 기록한다.
- 이유/기준/대안이 있으면 같이 남긴다.

### Open Questions
- "확인 필요"는 open_questions.md에 기록한다.
- 답이 나오면 항목을 닫고 decisions/spec로 반영한다.

### Task Plan
- 실행 가능한 작업만 task_plan.md에 남긴다.
- 상태는 다음 중 하나로 관리한다:
  - Backlog / Ready / Doing / Done / Blocked

### Spec
- spec.md는 Goal / Non-goals / Acceptance Criteria가 흔들리지 않게 유지한다.
- scope creep 징후가 있으면 Non-goals에 먼저 적는다.

---

## Minimal Operating Mode (POC 추천)
POC에서는 아래를 기본으로 한다:
- "스크랩"은 링크 + 제목 + (1~2문장) 요약까지만
- 전체 본문 저장/대량 크롤링은 POC 범위 밖
- 자동 요약/모델 호출은 2단계에서 붙인다

---

## Definition of Done (DoD) for Each Turn
한 턴이 끝났다고 말하려면 최소 아래 중 2개는 충족해야 한다:
- Decision 1개 이상 확정 또는 Open Question 정리
- File Ops가 명확(무슨 파일을 어떻게 바꿀지)
- Next Actions가 1~3개로 고정
