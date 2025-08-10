from __future__ import annotations

import yaml  
import tiktoken 
import pandas as pd
import re, os, json, hashlib

from pydantic import ValidationError
from dataclasses import dataclass
from typing import Dict, Optional, Iterable, Any

from src.core.fel.schema import FeatureCfg

@dataclass
class Features:
    char_len: int
    word_len: int
    token_est: int
    line_count: int
    has_json: bool
    strict_json: bool
    has_code: bool
    multistep_score: int
    complexity_score: float
    latency_tier: str
    safety_sensitive: bool

class FeatureExtractor:
    '''
    '''

    def __init__(self, cfg: FeatureCfg):
        if cfg is None:
            raise ValueError("feature configuration is required")
        
        self.token = None

        self.multistep = tuple(s.lower() for s in cfg.multistep)
        self.latency_medium = tuple(s.lower() for s in cfg.latency.medium)
        self.urgency = tuple(s.lower() for s in cfg.urgency)
        self.safety = tuple(s.lower() for s in cfg.safety)
        self.json_terms = tuple(s.lower() for s in cfg.json_terms)
        self.code_terms = tuple(s.lower() for s in cfg.code_terms)
        self.cx = cfg.complexity.model_dump()

        self.tk_enc = None
        enc = (cfg.tiktoken_encoding or "").strip()
        if enc and tiktoken:
            try:
                self.tk_enc = tiktoken.get_encoding(enc)
            except Exception:
                self.tk_enc = None
        
        self.config_hash = self._hash_config(cfg.model_dump())
        self.extractor_version = "fe-1.0"

    @staticmethod
    def _hash_config(cfg_dict: Dict) -> str:
        blob = json.dumps(cfg_dict, sort_keys=True, ensure_ascii=False).encode("utf-8")
        return hashlib.sha256(blob).hexdigest()[:12]

    @staticmethod
    def _id_for_prompt(text: str) -> str:
        return hashlib.sha1(text.encode("utf-8")).hexdigest()

    @classmethod
    def from_file(cls, path: str) -> "FeatureExtractor":
        if not os.path.exists(path):
            raise FileNotFoundError(f"feature extractor config file not found: {path}")
        if path.endswith((".yml", ".yaml")):
            if yaml is None:
                raise RuntimeError("pyyaml not installed (uv add pyyaml).")
            with open(path, "r", encoding="utf-8") as f:
                raw = yaml.safe_load(f)
        else:
            with open(path, "r", encoding="utf-8") as f:
                raw = json.load(f)
        try:
            cfg = FeatureCfg.model_validate(raw)
        except ValidationError as e:
            raise ValueError(f"Invalid feature config: {e}") from e
        return cls(cfg)


    def _estimate_tokens(self, text: str) -> int:
        if self.tk_enc:
            try:
                return len(self.tk_enc.encode(text))
            except Exception:
                pass
        return len(self.token.findall(text))

    def _score_complexity(self, text: str) -> float:
        pass

    def _estimate_latency(self, text: str) -> str:
        pass

    def _one(self, text: str) -> Features:
        pass

    def _batch(self, prompts: Iterable[str], ids: Optional[Iterable[str]] = None) -> pd.DataFrame:
        pass

    def save(self, data: Any, path: str) -> None:
        pass

    def load(self, path: str) -> pd.DataFrame:
        pass