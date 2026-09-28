"""
Platform Metrics & System Health Score Aggregator.
"""

from typing import Dict, Any, List
from ai_platform.schema import PlatformHealthReport, PillarEvaluationSummary


class PlatformMetricsCalculator:
    """Aggregates multi-pillar quality metrics and computes deployment readiness."""

    @staticmethod
    def calculate_health_summary(report: PlatformHealthReport) -> Dict[str, Any]:
        passed_pillars = sum(1 for p in report.pillar_summaries if p.status.value == "Passed")
        total_tests = sum(p.total_tests for p in report.pillar_summaries)
        total_passed = sum(p.passed_tests for p in report.pillar_summaries)

        return {
            "total_pillars": report.total_pillars,
            "passed_pillars": passed_pillars,
            "overall_health_score": round(report.overall_health_score, 4),
            "overall_health_percentage": round(report.overall_health_score * 100, 1),
            "total_test_cases": total_tests,
            "total_passed_cases": total_passed,
            "global_pass_rate": round(total_passed / max(total_tests, 1), 4),
            "deployment_approved": report.deployment_approved,
            "critical_alerts_count": len(report.critical_alerts),
        }


MetricsCalculator = PlatformMetricsCalculator
