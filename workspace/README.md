# Workspace

This directory stores outputs produced by vibe coding.
Rules and operating logic must live under `vibe/`.

## What goes here
- Project artifacts (spec/design/plan)
- Code prototypes / implementations
- Tests and runnable examples
- Generated docs that are outputs (not rules)

## What must NOT go here
- AI behavior rules
- Memory/decision logs for the package itself
- Global policies or prompts (those belong in `vibe/`)

## Project Structure Convention
Each project lives under:

workspace/projects/<project_slug>/
- spec.md
- design.md
- plan.md
- src/
- tests/

## Naming
- Use descriptive slugs (snake_case)
- Example: quickstart_onboarding, data_pipeline_poc

## Workflow (minimal)
1) Create project folder
2) Write spec.md
3) Write design.md (if needed)
4) Write plan.md
5) Then implement under src/ and tests/
