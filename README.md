# Claude for Reservoir Engineering

A hands-on Claude Code course for reservoir engineers, production engineers, petroleum engineers, subsurface data scientists, and technical teams who want to use AI-assisted coding without giving up engineering rigor.

This repository teaches Claude Code through reservoir engineering tasks instead of generic toy examples. Every exercise is framed around workflows engineers actually recognize: production data QA, water-cut trends, PVT unit checks, decline curve analysis, material balance discipline, nodal-analysis prompts, black-oil simulation preparation, pyResToolbox usage, and Model Context Protocol (MCP) tools.

The goal is not to make Claude "do engineering" blindly. The goal is to teach engineers how to direct Claude like a disciplined technical assistant: give it context, constrain assumptions, require units, verify results, use tests, and prefer proven libraries or MCP tools over invented formulas.

## Why This Course Exists

Reservoir engineering work is full of small but consequential details:

- pressure units: psia vs barsa
- temperature units: degF vs degC
- gas gravity parameter names that change across APIs
- correlations that are only valid in certain ranges
- production forecasts that look smooth but violate simple sanity checks
- material balance calculations that are only as good as their input history
- simulation tables that must be traceable and reproducible

AI tools can accelerate this work, but only when the engineer supplies enough domain context and demands verification. This course shows that workflow in concrete, repeatable exercises.

## What You Will Learn

By the end of the course, you should be able to:

- use Claude Code's explore, plan, code, and verify loop on engineering scripts
- write prompts that identify the file, function, failing behavior, units, and expected engineering relationship
- ask Claude to add tests with known values, monotonicity checks, and physical bounds
- create and use `CLAUDE.md` project memory for reservoir-specific standards
- package repeatable reservoir workflows as Claude skills
- use a reviewer subagent to catch unit, assumption, and correlation mistakes
- combine Claude with shell commands for production-data QA
- use pyResToolbox and pyrestoolbox-mcp for reservoir calculations rather than hand-rolling correlations
- parallelize independent sensitivity cases and aggregate the results carefully

## Who This Is For

This course is designed for:

- reservoir engineers learning AI-assisted coding
- production engineers working with CSV exports and decline curves
- petroleum engineering students who know the domain but want better coding workflows
- data scientists supporting subsurface teams
- technical managers evaluating Claude Code for engineering workflows
- open-source contributors building reservoir engineering automation

You do not need to be a software engineer. You should be comfortable reading basic Python and using a terminal.

## Source Inspiration

This project adapts the excellent exercise style of [`claude-code-for-hydrology`](https://github.com/lorenliu13/claude-code-for-hydrology) to reservoir engineering.

It is built around concepts and tooling from:

- [`pyResToolbox`](https://github.com/mwburgoyne/pyResToolbox), a Python reservoir engineering utility library by Mark Burgoyne
- [`pyrestoolbox-mcp`](https://github.com/gabrielserrao/pyrestoolbox-mcp), an MCP server exposing pyResToolbox calculations to AI assistants
- Claude Code workflows: project memory, skills, subagents, testing, MCP, and parallel work

## Repository Structure

```text
.
├── 01_explore_plan_code/          # Production analysis: explore, plan, implement
├── 02_specific_context/           # PVT conversion bug: precise context beats vague prompts
├── 03_verify_your_work/           # DCA checks: tests and sanity checks
├── 04_init_claude_md/             # Project memory with CLAUDE.md
├── 05_skills/                     # Reservoir engineering Claude skills
├── 06_subagent_review/            # Reservoir reviewer subagent workflow
├── 07_cli_workflow/               # Shell + Python QA for production CSVs
├── 08_mcp_pyrestoolbox/           # Using pyResToolbox through MCP
├── 09_parallel_fanout/            # Parallel sensitivity studies
├── .claude/
│   ├── agents/reservoir-reviewer.md
│   └── skills/
│       ├── reservoir-engineering/SKILL.md
│       └── run-tests/SKILL.md
├── references/pyrestoolbox-workflows.md
├── video-claude-reservoir-engineering/
├── CLAUDE.md
├── requirements.txt
└── README.md
```

## Prerequisites

Install:

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- Python 3.10 or newer
- `pip` or a Python environment manager
- optional but recommended: `pyrestoolbox`
- optional for live AI tool calls: [`pyrestoolbox-mcp`](https://github.com/gabrielserrao/pyrestoolbox-mcp)

Clone the repository:

```bash
git clone https://github.com/gabrielserrao/Claude-for-reservoir-engineering.git
cd Claude-for-reservoir-engineering
```

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

If your system uses `python` instead of `python3`, adjust the commands accordingly.

## Quick Start

Open Claude Code from the repository root:

```bash
claude
```

Start with Exercise 1:

```bash
cd 01_explore_plan_code
```

Read the exercise README, then try the "before" prompt and the "after" prompt. The contrast is the point of the course: you will see how much better Claude performs when you provide files, units, expected engineering behavior, and verification commands.

## How Each Exercise Works

Each exercise is self-contained and follows a consistent structure:

1. Read the exercise README.
2. Try the vague prompt first.
3. Clear Claude's context with `/clear`.
4. Try the improved prompt.
5. Compare the results.
6. Run the tests or checks.
7. Reflect on what changed in the prompt and workflow.

The "before" prompts are intentionally under-specified. They mimic how engineers often start with an AI tool. The "after" prompts show the level of context and constraint that produces dependable technical work.

## Course Modules

| # | Folder | Claude Code Practice | Reservoir Engineering Focus |
|---|--------|----------------------|-----------------------------|
| 1 | `01_explore_plan_code/` | Explore -> Plan -> Code | Production summary and water-cut trend analysis |
| 2 | `02_specific_context/` | Provide exact file/function/symptom context | Fixing PVT unit-conversion behavior |
| 3 | `03_verify_your_work/` | Use tests as the quality gate | Exponential decline and EUR sanity checks |
| 4 | `04_init_claude_md/` | Create persistent project memory | Reservoir standards in `CLAUDE.md` |
| 5 | `05_skills/` | Encode repeatable domain workflows | Reservoir engineering skill usage |
| 6 | `06_subagent_review/` | Add a reviewer agent | Unit, assumption, and correlation review |
| 7 | `07_cli_workflow/` | Use shell tools and Python together | Production CSV QA before analysis |
| 8 | `08_mcp_pyrestoolbox/` | Use MCP tools for live calculations | pyResToolbox PVT and simulation workflows |
| 9 | `09_parallel_fanout/` | Parallelize independent cases | Sensitivity studies across methods and assumptions |

## Exercise 1: Explore, Plan, Then Code

Claude is most useful when it first understands the codebase. In this exercise, Claude reads a production analysis script, a sample production CSV, and existing tests before adding water-cut trend analysis.

Engineering lesson:

- Water cut must be computed from oil and water volumes.
- The trend must respect well/date ordering.
- A production metric should be tested against known values.

Claude lesson:

- Plan mode reduces unnecessary edits.
- File-specific prompts produce better implementations.
- Tests define what "done" means.

## Exercise 2: Specific Context

Small PVT conversion bugs are easy to miss and costly to propagate. This exercise shows how to tell Claude exactly which test fails and which petroleum engineering relationship applies.

Engineering relationship:

```text
SG = 141.5 / (API + 131.5)
API = 141.5 / SG - 131.5
```

Claude lesson:

- "Fix the PVT bug" makes Claude search and guess.
- Naming the failing test and expected formula lets Claude go directly to the fault.

## Exercise 3: Verify Your Work

Decline curve helpers can look plausible while hiding invalid assumptions. This exercise uses known values and sanity checks for exponential decline and EUR calculations.

Good tests include:

- known analytic values
- nonnegative rates
- rejected invalid inputs
- EUR increasing as the economic limit decreases

Claude lesson:

- Ask for verification, not just implementation.
- Give Claude a command to run after edits.
- Make engineering checks explicit.

## Exercise 4: Project Memory With CLAUDE.md

Reservoir engineering projects have recurring rules: units, method names, assumptions, validation, and output standards. `CLAUDE.md` keeps that context available across sessions.

This repository's root `CLAUDE.md` tells Claude to:

- state field vs metric units
- prefer pyResToolbox or MCP tools for standard calculations
- avoid silent correlation changes
- include tests or sanity checks for engineering functions
- watch pyrestoolbox-mcp parameter naming conventions

Claude lesson:

- Persistent project memory prevents repeated explanations.
- Domain-specific instructions improve every later prompt.

## Exercise 5: Skills

Skills package reusable instructions for common work. This repository includes a reservoir engineering skill and a test-running skill.

The reservoir engineering skill covers:

- oil PVT
- gas PVT
- brine and CO2 workflows
- DCA
- material balance
- nodal/IPR/VLP
- relative permeability tables
- simulation table preparation
- parameter naming pitfalls in pyrestoolbox-mcp

Claude lesson:

- Do not paste the same domain rules into every prompt.
- Use skills to keep high-value instructions close to the model.

## Exercise 6: Subagent Review

Engineering code benefits from an independent review pass. The included `reservoir-reviewer` agent checks for:

- unit consistency
- correlation applicability
- nonphysical outputs
- pyResToolbox or MCP parameter mistakes
- missing tests
- weak assumptions

Claude lesson:

- Use a reviewer for higher-risk work.
- Ask for findings first, not praise or summaries.
- Treat the review as a quality gate.

## Exercise 7: CLI Workflow

Before fitting DCA models or running material balance, production data should be checked. This module uses Claude with shell commands and Python checks to inspect CSV data.

Typical QA checks:

- required columns exist
- dates parse correctly
- rates are nonnegative
- well/date rows are not duplicated
- cumulative production is monotonic when expected

Claude lesson:

- Let Claude use the terminal to inspect real files.
- Ask it to summarize evidence, not just assumptions.

## Exercise 8: pyResToolbox MCP

Claude should not invent industry correlations when reliable tools are available. This exercise shows how to ask Claude to use pyResToolbox through MCP for live reservoir engineering calculations.

Example prompt:

```text
Use the pyResToolbox MCP tools.
Calculate bubble point pressure for 35 API oil at 180 degF with solution GOR 800 scf/stb and gas gravity 0.75.
Use Valko-McCain if available.
State units, method, inputs, and one sanity check.
```

Important pyrestoolbox-mcp reminders:

- oil tools usually use `sg_g` for gas gravity
- gas tools usually use `sg`
- inflow tools use `psd` for sandface pressure
- some gas tools use `zmethod`, not `method`
- relative permeability table types include `SWOF`, `SGOF`, and `SGWFN`

Claude lesson:

- Use MCP tools when you need live calculations.
- Ask for inputs, units, method, output, and sanity check every time.

## Exercise 9: Parallel Fan-Out

Sensitivity cases are often independent. Claude can split them across workers or parallel calls, then aggregate the results.

Example independent cases:

- bubble point methods: `STAN`, `VALMC`, `VELAR`
- gas Z-factor methods: `DAK`, `HY`, `WYW`
- skin cases: `-2`, `0`, `5`

Claude lesson:

- Parallelize independent scenarios only.
- Require each worker to return assumptions and units.
- Use a final aggregation step to compare results.

## Running Tests

Run all tests:

```bash
python3 -m pytest -v
```

Run one exercise:

```bash
python3 -m pytest 01_explore_plan_code/ -v
```

The tests are intentionally small. They are teaching tools, not a complete engineering validation suite. When adapting the patterns to real work, add more edge cases, known-value comparisons, and domain-specific acceptance criteria.

## Using pyResToolbox

Install pyResToolbox:

```bash
python3 -m pip install pyrestoolbox
```

Example:

```python
from pyrestoolbox import oil

pbub = oil.oil_pbub(
    api=35,
    degf=180,
    rsb=800,
    sg_g=0.75,
    pbmethod="VALMC",
)

print(pbub)
```

When using pyResToolbox directly, always capture:

- input values and units
- method/correlation name
- output units
- applicability assumptions
- simple sanity checks

## Using pyrestoolbox-mcp

For Claude Desktop or another MCP-capable assistant, use:

```text
https://github.com/gabrielserrao/pyrestoolbox-mcp
```

That project exposes pyResToolbox calculations as MCP tools so Claude can call reservoir engineering functions directly.

Recommended response format for MCP-backed calculations:

```text
Inputs:
- API gravity: ...
- reservoir temperature: ...
- pressure: ...

Method:
- correlation/tool used: ...

Result:
- value and units: ...

Sanity check:
- physical or engineering check: ...

Assumptions:
- ...
```

## Included Claude Assets

This repository includes Claude configuration examples:

- `.claude/skills/reservoir-engineering/SKILL.md`
- `.claude/skills/run-tests/SKILL.md`
- `.claude/agents/reservoir-reviewer.md`
- `.claude/settings.json`
- `CLAUDE.md`

These are meant to be studied and adapted. The most important pattern is not the exact wording. The important pattern is that reservoir engineering constraints are made explicit and reusable.

## Project Video

A short Hyperframes video introducing the project is included in:

```text
video-claude-reservoir-engineering/
```

Rendered MP4:

```text
video-claude-reservoir-engineering/renders/claude-for-reservoir-engineering.mp4
```

Editable Hyperframes source:

```text
video-claude-reservoir-engineering/index.html
```

## Suggested Teaching Format

For a workshop or internal training session:

1. Spend 10 minutes introducing Claude Code and the repository.
2. Run Exercise 1 as a live demo.
3. Have participants do Exercises 2 and 3 individually.
4. Discuss how each prompt changed Claude's behavior.
5. Show `CLAUDE.md`, skills, and the reviewer agent.
6. Demonstrate an MCP-backed pyResToolbox calculation.
7. Finish with the parallel fan-out exercise.

Expected workshop duration: 90 to 150 minutes.

## Engineering Standards Used In This Course

Every serious reservoir engineering prompt should include:

- units
- method or correlation
- input ranges
- expected output shape
- validation criteria
- assumptions
- whether field or metric units are being used
- whether the answer is screening-level or decision-grade

Every serious engineering code change should include:

- focused tests
- known-value checks where possible
- nonphysical input handling
- output bounds or monotonicity checks where appropriate
- clear file/function scope

## Limitations

This course is educational. The sample data is fictional and intentionally small. The examples are designed to teach Claude Code workflows, not to certify engineering calculations.

For real reservoir decisions:

- validate against company standards
- check correlation applicability
- peer review material calculations
- document assumptions
- compare against independent tools where appropriate
- do not use AI output as the sole technical basis for field decisions

## Contributing

Contributions are welcome, especially:

- new reservoir engineering exercises
- better tests with known petroleum engineering values
- pyResToolbox or pyrestoolbox-mcp workflow examples
- additional Claude skills or reviewer agents
- teaching notes for classroom or workshop use
- fixes to units, terminology, or engineering assumptions

Suggested contribution pattern:

1. Add a numbered exercise folder.
2. Include a `README.md` with before/after prompts.
3. Include a small Python file or workflow artifact.
4. Include focused tests or validation instructions.
5. Keep sample data fictional or openly licensed.

## License

This project is intended to be open sourced as a course. See `LICENSE` for details.

## Acknowledgements

Thanks to the maintainers and contributors of:

- Claude Code and the Claude ecosystem
- pyResToolbox
- pyrestoolbox-mcp
- claude-code-for-hydrology
- Hyperframes, used to create the included project video

