"""
Tests for Schema module in AI Quality Evaluation Platform.
"""

from ai_platform.schema import PillarType, PillarStatus, PillarEvaluationSummary, PlatformHealthReport


def test_pillar_evaluation_summary():
    summary = PillarEvaluationSummary(
        pillar=PillarType.RESPONSE_QUALITY,
        score=0.95,
        status=PillarStatus.PASSED,
        total_tests=10,
        passed_tests=10,
    )
    assert summary.pillar == PillarType.RESPONSE_QUALITY
    assert summary.score == 0.95
    assert summary.status == PillarStatus.PASSED


def test_platform_health_report():
    report = PlatformHealthReport(
        total_pillars=7,
        overall_health_score=0.95,
        pillar_summaries=[],
        critical_alerts=[],
        deployment_approved=True,
    )
    assert report.total_pillars == 7
    assert report.deployment_approved is True
