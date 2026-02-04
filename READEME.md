# Vibe Coding Package (Repository OS)

This repository defines a **Vibe Package**: a file-based operating model where AI turns human thinking into **structure, decisions, and reproducible outputs**.

## Read First (5-minute Onboarding)

### What this repo is
- A **repository-level OS** for AI collaboration
- The goal is **reproducibility and clarity**, not fast code generation
- **Files are the source of truth** (conversation is not)

### Repo structure
- `vibe/`  
  → The engine: rules, roles, memory, templates

- `workspace/`  
  → Outputs only: specs, designs, plans, code, tests

### Start here (read order)
1) `vibe/constitution.md`  
2) `vibe/operating_rules.md`  
3) `vibe/memory/context.md`  
4) `workspace/README.md`

If anything is ambiguous:
- ask a question, or
- record it in `vibe/memory/open_questions.md`

---

## How to start a new project (2 minutes)

1) Create a new folder:
- `workspace/projects/<project_slug>/`

2) Copy templates into the project folder:
- `vibe/templates/spec.md`   → `workspace/projects/<project_slug>/spec.md`
- `vibe/templates/design.md` → `workspace/projects/<project_slug>/design.md`
- `vibe/templates/task_plan.md` → `workspace/projects/<project_slug>/plan.md`

3) Fill in `spec.md` first.
- No spec → no implementation.

---

## Operating Principles (short)
- **Structure precedes implementation**
- **Ambiguity triggers questions**
- **Decisions must be recorded**
- **Keep always-loaded docs short** (constitution/rules/context)

---

## Where to record things
- Current status summary → `vibe/memory/context.md`
- Decisions that change direction → `vibe/memory/decisions.md`
- Unresolved questions → `vibe/memory/open_questions.md`
- Term definitions → `vibe/memory/glossary.md`

---

## Current Phase
This repository is in the **definition phase**.
Focus on:
- rules, memory, roles, templates
Not on:
- runtime/CLI implementation
