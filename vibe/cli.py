# vibe/cli.py
# 목적:
# - 최소 CLI 엔트리포인트 (dry-run)
# - agent 이름을 받아 llm.yaml/agents.yaml 매핑이 정상인지 확인한다.

from __future__ import annotations

import os
import argparse
from pathlib import Path

from vibe.runtime.config import load_env_file_if_exists, load_llm_config, load_agents_config


def main() -> None:
    parser = argparse.ArgumentParser(prog="vibe")
    parser.add_argument(
        "agent",
        choices=["chief", "analyst", "dev", "qa", "librarian"],
        help="실행할 에이전트 역할",
    )
    parser.add_argument(
        "message",
        nargs="?",
        default="",
        help="(선택) 세션 시작 메시지",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="실제 LLM 호출 없이 설정/프롬프트 매핑만 출력",
    )
    args = parser.parse_args()

    # .env 로드 (있으면)
    load_env_file_if_exists()

    # 설정 로드
    llm = load_llm_config()
    agents = load_agents_config()

    agent_cfg = agents.agents[args.agent]
    model_cfg = llm.models[agent_cfg.llm_profile]
    provider_cfg = llm.providers[model_cfg.provider]

    prompt_path = Path(agent_cfg.prompt_file)

    print("=== VIBE SESSION START ===")
    print(f"Agent       : {args.agent}")
    print(f"LLM Profile : {agent_cfg.llm_profile}")
    print(f"Provider    : {model_cfg.provider}")
    print(f"Model       : {model_cfg.model}")
    print(f"Prompt File : {prompt_path.as_posix()}")
    print(f"Env Var Key : {provider_cfg.env_key_name}")
    if args.message:
        print(f"Message     : {args.message}")
    print("==========================")

    if args.dry_run:
        print("DRY RUN: LLM 호출 없이 종료합니다.")
        return

    # ===== REAL CHIEF CALL (MINIMAL) =====
    from openai import OpenAI
    api_key = os.environ.get(provider_cfg.env_key_name)
    if not api_key:
        raise SystemExit(
            f"Missing env var: {provider_cfg.env_key_name}. "
            f"Check .env at repo root or your terminal environment."
        )
    
    client = OpenAI(api_key=api_key)

    system_prompt = Path(prompt_path).read_text(encoding="utf-8")

    response = client.chat.completions.create(
        model=model_cfg.model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": args.message},
        ],
    )

    print("\n=== CHIEF RESPONSE ===")
    print(response.choices[0].message.content)
    print("======================")



if __name__ == "__main__":
    main()
