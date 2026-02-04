# Vibe Package Constitution

## 0. Purpose
This repository defines a Vibe Coding Package: a file-based operating model where AI converts human thinking into reproducible structure, decisions, and implementations.

## 1. Non-Negotiables (Must)
1) **Structure precedes implementation.**  
   No code until the structure/spec is clear enough to review.

2) **Source of truth lives in repository files.**  
   Conversations are transient. Files are memory.

3) **Ambiguity triggers questions, not assumptions.**  
   If a requirement is unclear, ask or record it as an open question.

4) **Decisions must be explicit and recorded.**  
   Major choices go to `vibe/memory/decisions.md` with an ID.

5) **Minimize context contamination.**  
   One Vibe Package = one repository. Keep rules in `vibe/`, outputs in `workspace/`.

6) **Reproducibility over speed.**  
   Optimize for “anyone can re-run and understand,” not “fastest output.”

## 2. What This Repo Is / Is Not
### Is
- A repository-level definition of how AI collaborates
- A system for decision tracking and structural clarity
- A portable model that can later be driven via CLI

### Is Not
- A “prompt trick”
- A ChatGPT-only workflow
- “Just generate code faster”

## 3. Operating Principle
At any time, the primary question is:
> **What are we defining right now?**
