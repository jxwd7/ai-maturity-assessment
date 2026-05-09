# AI Maturity Assessment Engine

**A lightweight scoring engine for turning AI readiness conversations into structured maturity levels.**

This repository contains the logic for a six-pillar AI maturity assessment. It is designed for consulting, workshops, and internal strategy work where a team needs to move from subjective AI enthusiasm to a clearer readiness score.

## What It Measures

The assessment is organized around six operating pillars:

| Pillar | Weight | What It Tests |
| --- | ---: | --- |
| Business | 25% | Strategy alignment, use-case value, ROI thinking, executive support |
| Platform | 25% | Data infrastructure, tooling, cloud readiness, experimentation, MLOps |
| People | 15% | Skills, ownership, readiness, change management |
| Operations | 15% | Monitoring, retraining, deployment resilience, cost control, documentation |
| Governance | 10% | Responsible AI, decision rights, explainability, compliance, data governance |
| Security | 10% | Privacy, model/data security, adversarial risk, DevSecOps, auditability |

## How Scoring Works

Each answer maps to a 1-5 score. The engine calculates:

1. Average score per pillar.
2. Weighted overall score on a 1-5 scale.
3. Percentage score from 0-100.
4. Maturity level from Level 1 to Level 5.

```text
Level 1: Initial / Ad-Hoc
Level 2: Managed / Opportunistic
Level 3: Defined / Strategic
Level 4: Embedded
Level 5: Optimizing / Transformational
```

## Repository Map

```text
assessment_data.py   Question bank, answer options, and pillar structure
scoring.py           Pillar scoring, weighted scoring, and maturity mapping
main.py              Simple command-line assessment runner
test_scoring.py      Unit tests for score and level behavior
requirements.txt     Dependency marker; current code uses the Python standard library
```

## Run Locally

```bash
python main.py
```

Run the scoring tests:

```bash
python -m unittest test_scoring.py
```

## Why This Matters

AI adoption fails when the conversation jumps from "we need AI" to "which model should we use" without checking whether the business, platform, people, governance, security, and operating practices are ready.

This project captures the consulting backbone for that conversation. It gives leaders a clear current-state view, helps identify weak pillars, and creates a practical starting point for an AI automation roadmap.

## Next Steps

- Add a Streamlit or React interface for workshop delivery.
- Export assessment results to PDF and slide-ready summaries.
- Add recommendation logic for each maturity level.
- Add team-specific benchmarks by industry or function.

## Maintainer

Built by [Jawwad Ahmed](https://jawwad.xyz) as part of an AI maturity and automation-readiness toolkit.
