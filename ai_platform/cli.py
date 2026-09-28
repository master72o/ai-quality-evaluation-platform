"""
CLI Interface for Enterprise AI Quality Evaluation Platform.
"""

import argparse
import sys
from ai_platform.orchestrator import PlatformOrchestrator
from ai_platform.metrics import MetricsCalculator
from ai_platform.visualizer import Visualizer
from ai_platform.report_generator import ReportGenerator


def main():
    parser = argparse.ArgumentParser(description="Enterprise AI Quality Evaluation Platform CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    run_parser = subparsers.add_parser("run-all", help="Run full 7-pillar AI Quality & System Health evaluation")
    run_parser.add_argument("--output-dir", default="results", help="Directory to save JSON/CSV outputs")
    run_parser.add_argument("--report-path", default="reports/platform_executive_report.md", help="Path to save Markdown report")
    run_parser.add_argument("--figures-dir", default="reports/figures", help="Directory to save figure plots")

    args = parser.parse_args()

    if args.command == "run-all":
        print("Executing Enterprise AI Quality Platform 7-Pillar Evaluation Suite...")
        report = PlatformOrchestrator.run_suite_evaluations()

        metrics_summary = MetricsCalculator.calculate_health_summary(report)

        print("\nUnified System Health Summary:")
        print(f"  Overall AI Health Score: {metrics_summary['overall_health_percentage']}%")
        print(f"  Pillars Passed:          {metrics_summary['passed_pillars']} / {metrics_summary['total_pillars']}")
        print(f"  Total Test Cases Passed: {metrics_summary['total_passed_cases']} / {metrics_summary['total_test_cases']} ({metrics_summary['global_pass_rate']*100:.1f}%)")
        print(f"  Deployment Decision:     {'APPROVED' if report.deployment_approved else 'BLOCKED'}")

        print(f"\nExporting results to: {args.output_dir}")
        ReportGenerator.export_results(report, args.output_dir)

        print(f"Generating dashboard visualizations in: {args.figures_dir}")
        Visualizer.generate_all_figures(report, args.figures_dir)

        print(f"Generating master executive report at: {args.report_path}")
        ReportGenerator.generate_markdown_report(report, args.report_path)

        print("\nEnterprise AI Quality Platform evaluation completed successfully!")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
