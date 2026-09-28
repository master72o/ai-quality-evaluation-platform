"""
Tests for Platform Orchestrator and Metrics in AI Quality Evaluation Platform.
"""

from ai_platform.orchestrator import PlatformOrchestrator
from ai_platform.metrics import MetricsCalculator


def test_platform_orchestrator_run():
    report = PlatformOrchestrator.run_suite_evaluations()
    assert report.total_pillars == 7
    assert report.overall_health_score > 0.85
    assert report.deployment_approved is True


def test_metrics_calculator():
    report = PlatformOrchestrator.run_suite_evaluations()
    summary = MetricsCalculator.calculate_health_summary(report)

    assert summary["total_pillars"] == 7
    assert summary["passed_pillars"] == 7
    assert summary["overall_health_percentage"] > 85.0
    assert summary["deployment_approved"] is True
