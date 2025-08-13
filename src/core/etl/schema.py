from pydantic import BaseModel, Field, ConfigDict

class ComplexityCfg(BaseModel):
    model_config = ConfigDict(extra="forbid")
    length_thresholds: list[int] = Field(min_items=2)
    branching_markers: list[str]
    uniq_ratio_penalty_lt: float
    multistep_scale: float

class LatencyKeywordsCfg(BaseModel):
    medium: list[str]

class FeatureCfg(BaseModel):
    schema_version: str
    json_terms: list[str]
    code_terms: list[str]
    multistep: list[str]
    urgency: list[str]
    safety: list[str]
    tiktoken_encoding: str | None = None
    latency_keywords: LatencyKeywordsCfg
    complexity: ComplexityCfg