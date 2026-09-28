# Enterprise AI Quality Evaluation Platform (`ai-quality-evaluation-platform`)

> Capstone Unified Enterprise AI Quality & LLM Evaluation Platform Consolidating 7 Core AI Quality Pillars.

[![CI](https://github.com/user/ai-quality-evaluation-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/user/ai-quality-evaluation-platform/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Executive Summary

`ai-quality-evaluation-platform` is the capstone repository of the 12-project AI Evaluation & LLM Quality Engineering Portfolio. It consolidates all specialized evaluation pillars into a single unified CLI engine and executive reporting platform:

1. **Response Quality & Factuality**: Deterministic scoring and claim-level factuality verification.
2. **Decoupled RAG Benchmark**: Retrieval (Recall@K, NDCG) and generation (faithfulness) evaluation.
3. **CI/CD Prompt Regression**: Automated regression testing and quality gates ($\Delta < -0.05$ blocker).
4. **Adversarial Safety Red-Teaming**: Prompt injection, PII leakage, and DAN jailbreak scanning.
5. **Multi-Model Frontier Benchmarking**: Reasoning, JSON compliance, and Pareto cost-efficiency.
6. **Reward Model Calibration**: Bradley-Terry sigmoid probabilities and Expected Calibration Error (ECE).
7. **Autonomous Agent Trajectories**: Tool argument verification, step efficiency, and self-healing recovery.

---

## Unified 7-Pillar Architecture

```
                               ┌───────────────────────────────────────────┐
                               │   Enterprise AI Quality Platform CLI      │
                               └─────────────────────┬─────────────────────┘
                                                     │
        ┌─────────────┬─────────────┬────────────────┼────────────────┬─────────────┬─────────────┐
        ▼             ▼             ▼                ▼                ▼             ▼             ▼
   Response Quality  RAG Eval  Prompt Regression  Safety RedTeam  Model Benchmark  Reward Cal.   Agent Traj.
        │             │             │                │                │             │             │
        └─────────────┴─────────────┴────────────────┼────────────────┴─────────────┴─────────────┘
                                                     ▼
                                     ┌──────────────────────────────┐
                                     │  Unified Platform Health     │
                                     │      Score Calculator        │
                                     └───────────────┬──────────────┘
                                                     │
                    ┌────────────────────────────────┴────────────────────────────────┐
                    ▼                                                                 ▼
      🟢 APPROVED FOR PRODUCTION                                            🔴 DEPLOYMENT BLOCKED
     (Overall Health ≥ 85%, 0 Alerts)                                       (Safety Alert / Gate Fail)
```

---

## Quickstart & Installation

```bash
# Clone repository
git clone https://github.com/user/ai-quality-evaluation-platform.git
cd ai-quality-evaluation-platform

# Install in editable mode
pip install -e .

# Run pytest suite
pytest
```

---

## Executing Platform Benchmark CLI

Run the full 7-pillar platform evaluation suite via CLI:

```bash
python -m ai_platform.cli run-all \
  --output-dir results \
  --report-path reports/platform_executive_report.md \
  --figures-dir reports/figures
```

---

## Consolidated 7-Pillar Health Score Matrix

| Evaluation Pillar | Health Score | Status | Passed Test Cases |
| :--- | :--- | :--- | :--- |
| **`Response_Quality`** | `94.5%` | 🟢 Passed | `12 / 12` |
| **`RAG_Evaluation`** | `95.0%` | 🟢 Passed | `4 / 4` |
| **`Prompt_Regression`** | `95.4%` | 🟢 Passed | `5 / 5` |
| **`Safety_RedTeam`** | `100.0%` | 🟢 Passed | `5 / 5` |
| **`Model_Benchmark`** | `84.2%` | 🟢 Passed | `4 / 4` |
| **`Reward_Calibration`** | `98.9%` | 🟢 Passed | `5 / 5` |
| **`Agent_Trajectory`** | `100.0%` | 🟢 Passed | `3 / 3` |
| **OVERALL SYSTEM HEALTH** | **`95.4%`** | **🟢 APPROVED** | **`38 / 38` (100%)** |

### Executive Visual Dashboard Artifacts

- **Platform Health Overview**: `reports/figures/platform_health_overview.png`
- **Cross-Pillar Quality Matrix**: `reports/figures/cross_pillar_quality_matrix.png`
- **Executive Quality Dashboard**: `reports/figures/executive_quality_dashboard.png`

---

## Repository Structure

```
ai-quality-evaluation-platform/
├── .github/workflows/ci.yml     # Continuous Integration workflow
├── pyproject.toml               # Package build metadata
├── requirements.txt             # Project dependencies
├── ai_platform/                 # Core Python package
│   ├── __init__.py
│   ├── schema.py                # Data models & pillar enums
│   ├── orchestrator.py          # Unified 7-pillar engine
│   ├── metrics.py               # System health aggregator
│   ├── visualizer.py            # Executive dashboard figures
│   ├── report_generator.py      # Master Markdown report & JSON/CSV exporter
│   └── cli.py                   # CLI entry point
├── data/
│   ├── README.md
│   └── sample_eval_requests.json # Platform request config
├── results/                     # Exported JSON & CSV health reports
├── reports/
│   ├── platform_executive_report.md # Master executive report
│   └── figures/                 # Dashboard chart graphics
└── tests/                       # Unit and integration tests
```

---

## License

MIT License © 2026 AI Evaluation Engineering Team.
