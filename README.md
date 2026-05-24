# Hermes for Reservoir Engineering

Ported from [Claude-for-reservoir-engineering](https://github.com/gabrielserrao/Claude-for-reservoir-engineering) for **Nous Research Hermes Agent**. All exercises adapted to Hermes tooling: skills, subagents, cron scheduling, web search, project memory, and more.

This is a hands-on reservoir engineering course for engineers, petroleum data scientists, and technical teams who want AI-assisted coding without sacrificing engineering rigor. Every exercise uses real engineering workflows: production QA, water-cut trends, PVT unit checks, decline curves, material balance, nodal analysis, pyResToolbox usage, and parallel sensitivity studies.

The goal is to teach engineers how to direct AI like a disciplined technical assistant: give it context, constrain assumptions, require units, verify results, use tests, and prefer proven libraries over invented formulas.

## Why This Course Exists

Reservoir engineering is full of small but consequential details:

- pressure units: psia vs barsa
- temperature units: degF vs degC
- gas gravity parameter names that change across APIs
- correlations valid only in certain ranges
- production forecasts that violate simple sanity checks
- material balance only as good as its input history
- simulation tables that must be traceable and reproducible

AI tools can accelerate this work, but only when the engineer supplies domain context and demands verification. This course shows that workflow in concrete, repeatable exercises.

## What You Will Learn

By the end of this course:

- use Hermes explore-plan-code-verify loop on engineering scripts
- write prompts that identify the file, function, failing behavior, units, and expected relationship
- ask Hermes to add tests with known values, monotonicity checks, and physical bounds
- create CLAUDE.md / AGENTS.md project memory for reservoir-specific standards
- package repeatable workflows as Hermes skills (.hermes/skills/)
- use a reviewer subagent (delegate_task) to catch unit and assumption mistakes
- combine Hermes with shell commands for production-data QA
- use cron scheduling for recurring analysis workflows
- use pyResToolbox and pyrestoolbox-mcp for live reservoir calculations
- parallelize sensitivity cases across subagents and aggregate carefully

## Who This Is For

- reservoir engineers learning AI-assisted coding
- production engineers working with CSV exports and decline curves
- petroleum engineering students who know the domain but want better coding workflows
- data scientists supporting subsurface teams
- technical managers evaluating AI agents for engineering workflows
- open-source contributors building reservoir engineering automation

You do not need to be a software engineer. Comfort with basic Python and a terminal is enough.

## Source Inspiration

This project adapts the exercise style of [claude-code-for-hydrology](https://github.com/lorenliu13/claude-code-for-hydrology) to reservoir engineering, then ports it to Hermes Agent.

Built around:

- [pyResToolbox](https://github.com/mwburgoyne/pyResToolbox) by Mark Burgoyne
- [pyrestoolbox-mcp](https://github.com/gabrielserrao/pyrestoolbox-mcp) for MCP-backed AI tool calls
- Hermes Agent workflows: skills, subagents, memory, cron, web search, testing, MCP

## Repository Structure

    .
    |-- 01_explore_plan_code/          # Production analysis: explore, plan, implement
    |-- 02_specific_context/           # PVT conversion bug: precise context beats vague prompts
    |-- 03_verify_your_work/            # DCA checks: tests and sanity checks
    |-- 04_init_project_memory/          # Project memory with CLAUDE.md + AGENTS.md
    |-- 05_skills/                      # Reusable Hermes skills
    |-- 06_subagent_review/             # Reviewer subagent workflow
    |-- 07_cli_workflow/                # Shell + Python QA for production CSVs
    |-- 08_mcp_pyrestoolbox/             # pyResToolbox via MCP
    |-- 09_parallel_fanout/             # Parallel sensitivity studies
    |-- assets/                          # Generated plots + result tables
    |-- scripts/generate_course_figures.py
    |-- .hermes/skills/                  # Hermes-style skill files
    |-- AGENTS.md                        # Reviewer subagent prompt
    |-- CLAUDE.md                        # Project rules
    |-- requirements.txt
    |-- README.md

## Prerequisites

- Hermes Agent -- Install guide: https://hermes-agent.nousresearch.com/docs/
- Python 3.10+ and pip
- Optional but recommended: pyrestoolbox
- Optional for live AI tool calls: pyrestoolbox-mcp

Clone and enter:

    git clone https://github.com/zakusworo/hermes-reservoir-engineering.git
    cd hermes-reservoir-engineering

Install dependencies:

    python3 -m pip install -r requirements.txt

Generate course figures:

    python3 scripts/generate_course_figures.py

Figures live in assets/ and are committed so the course is readable on GitHub without running code first.

## Quick Start

Start Hermes from the repo root:

    hermes

Or with project rules preloaded:

    hermes --worktree

Navigate to Exercise 1:

    cd 01_explore_plan_code

Read the exercise README, then try the vague prompt first, /clear, then the improved prompt. The contrast is the point.

## Hermes vs Claude Code: What Changes

| Feature | Claude Code | Hermes Agent |
|---------|-------------|--------------|
| Explore/plan/code/verify | Yes | Yes, plus /skill preloading |
| Project memory | CLAUDE.md | CLAUDE.md + AGENTS.md + .hermes/skills/ |
| Skills | .claude/skills/ | .hermes/skills/ -- loaded with /skill |
| Subagent review | Reviewer agent | delegate_task -- spawn isolated subagent |
| Cron/scheduled tasks | Not built-in | /cron -- schedule recurring analysis |
| Web search | Not built-in | Built-in web_search tool |
| Memory across sessions | Manual | Persistent memory via /memory |
| CLI approvals | --yolo | hermes config set approvals.mode manual (default) |
| WSL/Windows | Natively supported | Yes, with /mnt/c/ path conventions |

All exercises in this course have been adapted for Hermes tool model (terminal(), browser_navigate(), delegate_task(), cronjob(), web_search(), skill_view(), etc.).

## Course Modules

| # | Folder | Hermes Practice | Reservoir Engineering Focus |
|---|--------|-----------------|-----------------------------|
| 1 | 01_explore_plan_code/ | Explore -> Plan -> Code | Production summary and water-cut trend analysis |
| 2 | 02_specific_context/ | Provide exact file/function/symptom context | Fixing PVT unit-conversion behavior |
| 3 | 03_verify_your_work/ | Use tests as the quality gate | Exponential decline and EUR sanity checks |
| 4 | 04_init_project_memory/ | Project memory (CLAUDE.md + AGENTS.md) | Reservoir standards in persistent context |
| 5 | 05_skills/ | Encode repeatable domain workflows | Reservoir engineering skill usage |
| 6 | 06_subagent_review/ | Add a reviewer subagent | Unit, assumption, and correlation review |
| 7 | 07_cli_workflow/ | Shell tools and Python together | Production CSV QA before analysis |
| 8 | 08_mcp_pyrestoolbox/ | Use MCP tools for live calculations | pyResToolbox PVT and simulation workflows |
| 9 | 09_parallel_fanout/ | Parallelize independent cases via delegate_task | Sensitivity studies across methods |

## Illustrated Outputs

Run python3 scripts/generate_course_figures.py to regenerate.

| Graph | File | Description |
|-------|------|-------------|
| Monthly Production & Water-Cut | ![production_water_cut.png](assets/production_water_cut.png) | Oil/water volumes and water-cut % trend by well |
| PVT API-to-Specific-Gravity | ![pvt_api_specific_gravity.png](assets/pvt_api_specific_gravity.png) | API gravity vs oil-specific gravity curve with sample points |
| DCA Decline & EUR Sensitivity | ![dca_decline_sensitivity.png](assets/dca_decline_sensitivity.png) | Exponential decline curves and EUR sensitivity to economic limit |
| Engineering Workflow Map | ![hermes_reservoir_workflow.png](assets/hermes_reservoir_workflow.png) | 5-step guardrail workflow (explore-plan-code-verify-review) |

### Production Water-Cut Diagnostic

![Production water-cut diagnostic](assets/production_water_cut.png)

- A-01 has stronger oil volume but water cut increases from 7.7% to 14.6%.
- B-02 starts wetter and also trends upward from 21.6% to 27.7%.
- A good prompt asks for both calculation and interpretation: is water cut increasing, by how many percentage points, and does the trend respect well/date ordering?

### PVT API to Specific Gravity

![PVT API to specific gravity curve](assets/pvt_api_specific_gravity.png)

Higher API gravity means lighter oil, so specific gravity decreases as API increases. A fix that passes a round-trip test but violates monotonicity is still suspicious.

### DCA Decline Sensitivity

![DCA decline sensitivity](assets/dca_decline_sensitivity.png)

- Higher nominal decline produces lower future rates for the same initial rate.
- Lower economic limits increase EUR, but this remains a screening calculation, not reserves booking.

### Hermes Workflow Map

![Claude reservoir workflow](assets/hermes_reservoir_workflow.png)

The 5-step quality loop: explore codebase -> plan changes -> implement code -> verify with tests -> review with subagent.

## Exercise Highlights

### Exercise 1: Explore, Plan, Then Code

Hermes reads the production analysis script, CSV sample, and existing tests before adding water-cut trend analysis. Engineering guardrails: compute water cut from volumes, respect well/date ordering, test against known values, plot as second verification surface.

### Exercise 2: Specific Context

Fix PVT unit-conversion bugs by telling Hermes exactly which test fails and which petroleum relationship applies:

    SG = 141.5 / (API + 131.5)
    API = 141.5 / SG - 131.5

Interpretation guardrail: API and SG move in opposite directions. 35 API oil has SG near 0.850.

### Exercise 3: Verify Your Work

Decline-curve helpers are only trustworthy with known-value checks, nonnegative rates, rejected invalid inputs, EUR monotonicity, and sensitivity plots.

### Exercise 4: Project Memory (CLAUDE.md + AGENTS.md)

Reservoir projects have recurring rules. This repo root files tell Hermes to:

- state field vs metric units
- prefer pyResToolbox or MCP tools
- avoid silent correlation changes
- include tests for engineering functions
- respect pyrestoolbox-mcp parameter conventions

### Exercise 5: Skills

.hermes/skills/reservoir-engineering/ packages reusable instructions for:

- oil PVT, gas PVT, brine/CO2 workflows
- DCA, material balance, nodal/IPR/VLP
- relative permeability tables, simulation prep
- pyrestoolbox-mcp parameter pitfalls

Load with /skill reservoir-engineering.

### Exercise 6: Subagent Review

delegate_task spawns an isolated reviewer that checks for unit consistency, correlation applicability, nonphysical outputs, MCP parameter mistakes, missing tests, and weak assumptions.

### Exercise 7: CLI Workflow

Hermes runs terminal() tool natively. Inspect CSVs, check columns, parse dates, verify nonnegative rates, detect duplicates -- directly from the shell.

### Exercise 8: pyResToolbox MCP

Use pyrestoolbox-mcp tools for live calculations. Hermes can call these via browser_navigate() or MCP if configured.

Key reminders:

- oil tools: sg_g for gas gravity
- gas tools: sg
- inflow tools: psd for sandface pressure
- gas Z-factor: zmethod not method
- rel-perm tables: SWOF, SGOF, SGWFN

### Exercise 9: Parallel Fan-Out

Sensitivity cases are often independent. Use delegate_task with multiple tasks array entries to run them in parallel, then aggregate results.

Examples:

- bubble point methods: STAN, VALMC, VELAR
- gas Z-factor methods: DAK, HY, WYW
- skin cases: -2, 0, 5

## Key Hermes Commands

    hermes                              # start session in this repo
    hermes -w                           # isolated worktree (git-safe parallel agents)
    hermes -s reservoir-engineering     # preload skill
    /skill reservoir-engineering        # load within session
    /skill run-tests                    # load test skill
    /init                               # reload CLAUDE.md project rules
    /delegate_task                      # spawn subagent for review or parallel work
    /cron                               # schedule recurring analysis
    /agents                             # list active subagents
    /memory add                         # save durable note across sessions
    /web_search                         # search web for latest data or references

## Running Tests

All tests:

    python3 -m pytest -v

One exercise:

    python3 -m pytest 01_explore_plan_code/ -v

Tests are teaching tools, not a complete engineering validation suite. Add more edge cases and known-value comparisons for real work.

## Using pyResToolbox

    python3 -m pip install pyrestoolbox

Example:

    from pyrestoolbox import oil
    pbub = oil.oil_pbub(api=35, degf=180, rsb=800, sg_g=0.75, pbmethod="VALMC")
    print(pbub)

Always capture: inputs, units, method, output, sanity check, applicability assumptions.

## Using pyrestoolbox-mcp

For Hermes with MCP configured, use:

    https://github.com/gabrielserrao/pyrestoolbox-mcp

Recommended response format:

    Inputs:
    - API gravity: 35
    - reservoir temperature: 180 degF
    - pressure: ...

    Method:
    - correlation/tool used: Valko-McCain

    Result:
    - value and units: 2841 psia

    Sanity check:
    - physical or engineering check: ...

    Assumptions:
    - ...

## Security Note

Destructive commands default to manual approval:

    hermes config set approvals.mode manual

For CI/batch, use --yolo. Hermes runs shell via terminal() tool. This repo intentionally allows python, python3, pytest, and uv run during exercises.

## Contributing

Contributions welcome:

- new reservoir engineering exercises
- better tests with known petroleum engineering values
- pyResToolbox or pyrestoolbox-mcp workflow examples
- additional Hermes skills or reviewer agents
- teaching notes for classroom or workshop use
- fixes to units, terminology, or engineering assumptions

Pattern:

1. Add a numbered exercise folder.
2. Include README.md with before/after prompts.
3. Include a small Python file or workflow artifact.
4. Include focused tests or validation instructions.
5. Keep sample data fictional or openly licensed.

## License

MIT License. See LICENSE.

- Copyright (c) 2025 Gabriel Serrao (original course)
- Copyright (c) 2026 Zulfikar Aji Kusworo -- Hermes Agent port, code rewrite, figures, and packaging.

## Acknowledgements

Thanks to the maintainers of:

- Claude Code and the Claude ecosystem
- pyResToolbox
- pyrestoolbox-mcp
- claude-code-for-hydrology
- Nous Research Hermes Agent
