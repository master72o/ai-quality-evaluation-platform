"""
Data Schemas for AI Quality Evaluation Platform.
"""

from enum import Enum
from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any, List


class PillarType(str, Enum):
    RESPONSE_QUALITY = "Response_Quality"
    RAG_EVAL = "RAG_Evaluation"
    PROMPT_REGRESSION = "Prompt_Regression"
    SAFETY_REDTEAM = "Safety_RedTeam"
    MODEL_BENCHMARK = "Model_Benchmark"
    REWARD_CALIBRATION = "Reward_Calibration"
    AGENT_TRAJECTORY = "Agent_Trajectory"


class PillarStatus(str, Enum):
    PASSED = "Passed"
    WARNING = "Warning"
    FAILED = "Failed"


@dataclass
class PillarEvaluationSummary:
    __test__ = False

    pillar: PillarType
    score: float
    status: PillarStatus
    total_tests: int
    passed_tests: int
    metrics: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pillar": self.pillar.value if isinstance(self.pillar, PillarType) else str(self.pillar),
            "score": round(self.score, 4),
            "status": self.status.value if isinstance(self.status, PillarStatus) else str(self.status),
            "total_tests": self.total_tests,
            "passed_tests": self.passed_tests,
            "metrics": self.metrics,
        }


@dataclass
class PlatformHealthReport:
    total_pillars: int
    overall_health_score: float
    pillar_summaries: List[PillarEvaluationSummary]
    critical_alerts: List[str]
    deployment_approved: bool

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total_pillars": self.total_pillars,
            "overall_health_score": round(self.overall_health_score, 4),
            "deployment_approved": bool(self.deployment_approved),
            "critical_alerts": self.critical_alerts,
            "pillar_summaries": [p.to_dict() for p in self.pillar_summaries],
        }
