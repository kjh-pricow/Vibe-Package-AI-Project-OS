# vibe/runtime/config.py
# 목적:
# - vibe/config/llm.yaml, vibe/config/agents.yaml 로드
# - .env(있으면) 단순 파싱해서 환경변수로 주입 (dry-run 준비)

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import yaml


@dataclass(frozen=True)
class ProviderConfig:
    # 목적: 프로바이더별 환경변수 키 이름과 base_url 저장
    env_key_name: str
    base_url: str | None = None


@dataclass(frozen=True)
class ModelConfig:
    # 목적: llm_profile → 실제 provider/model 매핑
    provider: str
    model: str


@dataclass(frozen=True)
class AgentConfig:
    # 목적: agent → prompt_file + llm_profile 매핑
    prompt_file: str
    llm_profile: str


@dataclass(frozen=True)
class LLMConfig:
    # 목적: llm.yaml 전체 로드 결과
    providers: dict[str, ProviderConfig]
    models: dict[str, ModelConfig]


@dataclass(frozen=True)
class AgentsConfig:
    # 목적: agents.yaml 전체 로드 결과
    agents: dict[str, AgentConfig]


def _repo_root() -> Path:
    # 목적: 어디서 실행하든 repo root를 찾기 (현재 파일 기준 2단계 상위)
    return Path(__file__).resolve().parents[2]


def load_env_file_if_exists() -> None:
    # 목적:
    # - .env가 있으면 간단히 파싱해서 os.environ에 넣는다.
    # - 이미 설정된 환경변수는 덮어쓰지 않는다.
    root = _repo_root()
    env_path = root / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip().lstrip("\ufeff")  # Windows UTF-8 BOM 방어
        if k.startswith("export "):     # bash 스타일 방어
            k = k[len("export "):].strip()
        
        v = v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)


def load_llm_config() -> LLMConfig:
    # 목적: vibe/config/llm.yaml 로드
    root = _repo_root()
    path = root / "vibe" / "config" / "llm.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    providers: dict[str, ProviderConfig] = {}
    for name, cfg in (data.get("providers") or {}).items():
        providers[name] = ProviderConfig(
            env_key_name=cfg["env_key_name"],
            base_url=cfg.get("base_url"),
        )

    models: dict[str, ModelConfig] = {}
    for profile, cfg in (data.get("models") or {}).items():
        models[profile] = ModelConfig(
            provider=cfg["provider"],
            model=cfg["model"],
        )

    return LLMConfig(providers=providers, models=models)


def load_agents_config() -> AgentsConfig:
    # 목적: vibe/config/agents.yaml 로드
    root = _repo_root()
    path = root / "vibe" / "config" / "agents.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    agents: dict[str, AgentConfig] = {}
    for agent_name, cfg in (data.get("agents") or {}).items():
        agents[agent_name] = AgentConfig(
            prompt_file=cfg["prompt_file"],
            llm_profile=cfg["llm_profile"],
        )

    return AgentsConfig(agents=agents)
