"""
Visualization Generator for AI Quality Evaluation Platform.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any
from ai_platform.schema import PlatformHealthReport, PillarType


class Visualizer:
    """Generates executive dashboard figures and system health score graphics."""

    @staticmethod
    def generate_all_figures(
        report: PlatformHealthReport, output_dir: str = "reports/figures"
    ) -> Dict[str, str]:
        os.makedirs(output_dir, exist_ok=True)
        generated = {}

        # 1. Platform Health Overview
        health_path = os.path.join(output_dir, "platform_health_overview.png")
        Visualizer._plot_health_overview(report, health_path)
        generated["platform_health_overview"] = health_path

        # 2. Cross-Pillar Quality Matrix
        matrix_path = os.path.join(output_dir, "cross_pillar_quality_matrix.png")
        Visualizer._plot_quality_matrix(report, matrix_path)
        generated["cross_pillar_quality_matrix"] = matrix_path

        # 3. Executive Quality Dashboard
        dash_path = os.path.join(output_dir, "executive_quality_dashboard.png")
        Visualizer._plot_executive_dashboard(report, dash_path)
        generated["executive_quality_dashboard"] = dash_path

        return generated

    @staticmethod
    def _plot_health_overview(report: PlatformHealthReport, output_path: str):
        fig, ax = plt.subplots(figsize=(10, 5))
        pillars = [p.pillar.value if hasattr(p.pillar, "value") else str(p.pillar) for p in report.pillar_summaries]
        scores = [p.score * 100 for p in report.pillar_summaries]
        p_labels = [p.replace("_", "\n") for p in pillars]

        colors = ["#5cb85c" if s >= 85 else "#f0ad4e" if s >= 70 else "#d9534f" for s in scores]

        bars = ax.bar(p_labels, scores, color=colors, edgecolor="#333333", width=0.45)
        ax.set_ylabel("Quality Health Score (%)", fontsize=11, fontweight="bold")
        ax.set_title(f"Unified AI System Quality Health Overview (Overall Score: {report.overall_health_score*100:.1f}%)", fontsize=12, fontweight="bold", pad=15)
        ax.set_ylim(0, 115)
        ax.axhline(y=85.0, color="#2b5c8f", linestyle="--", linewidth=1.5, label="Production Gate Threshold (85%)")
        ax.legend(loc="lower right")
        ax.grid(axis="y", linestyle=":", alpha=0.6)

        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., h + 1.5, f"{h:.1f}%", ha="center", va="bottom", fontsize=9, fontweight="bold")

        plt.tight_layout()
        plt.savefig(output_path, dpi=200)
        plt.close()

    @staticmethod
    def _plot_quality_matrix(report: PlatformHealthReport, output_path: str):
        fig, ax = plt.subplots(figsize=(11, 5))
        pillars = [p.pillar.value if hasattr(p.pillar, "value") else str(p.pillar) for p in report.pillar_summaries]
        p_labels = [p.replace("_", "\n") for p in pillars]

        totals = [p.total_tests for p in report.pillar_summaries]
        passeds = [p.passed_tests for p in report.pillar_summaries]

        x = np.arange(len(p_labels))
        width = 0.35

        rects1 = ax.bar(x - width/2, totals, width, label="Total Evaluation Cases", color="#2b5c8f")
        rects2 = ax.bar(x + width/2, passeds, width, label="Passed Test Cases", color="#5cb85c")

        ax.set_ylabel("Number of Test Cases", fontsize=11, fontweight="bold")
        ax.set_title("Cross-Pillar Test Case Execution & Pass Matrix", fontsize=12, fontweight="bold", pad=15)
        ax.set_xticks(x)
        ax.set_xticklabels(p_labels)
        ax.legend(loc="upper right")
        ax.grid(axis="y", linestyle=":", alpha=0.6)

        for rects in [rects1, rects2]:
            for r in rects:
                h = r.get_height()
                ax.text(r.get_x() + r.get_width()/2., h + 0.2, f"{int(h)}", ha="center", va="bottom", fontsize=9, fontweight="bold")

        plt.tight_layout()
        plt.savefig(output_path, dpi=200)
        plt.close()

    @staticmethod
    def _plot_executive_dashboard(report: PlatformHealthReport, output_path: str):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis("off")

        bg_color = "#eafaf1" if report.deployment_approved else "#fdedec"
        fig.patch.set_facecolor(bg_color)

        status_str = "APPROVED FOR PRODUCTION" if report.deployment_approved else "DEPLOYMENT BLOCKED"
        health_pct = f"{report.overall_health_score * 100:.1f}%"

        text_content = (
            f"ENTERPRISE AI QUALITY PLATFORM EXECUTIVE DASHBOARD\n"
            f"────────────────────────────────────────────────────────\n\n"
            f"Overall AI Health Score : {health_pct}\n"
            f"Deployment Status       : {status_str}\n"
            f"Total Pillars Evaluated : {report.total_pillars} / 7 Pillars Passed\n"
            f"Critical Safety Alerts  : {len(report.critical_alerts)} Alerts\n"
        )

        ax.text(
            0.05, 0.5,
            text_content,
            fontsize=13,
            fontfamily="monospace",
            fontweight="bold",
            va="center",
            ha="left"
        )

        plt.tight_layout()
        plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor())
        plt.close()
