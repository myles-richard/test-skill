---
name: fork-terminal-skill
description: Fork a terminal session to a new terminal window. Use this when the user requests 'fork terminal' or 'new terminal: <command>'. 'fork session: <command>'.
---

## Purpose

Fork a terminal session to a new terminal window. Using one agentic coding tools or raw cli commands.
Follow the `Instructions`, execute the `Workflow`, based on the `Cookbook`.

## Variables

ENABLE_RAW_CLI: true
ENABLE_GEMENI_CLI: true
ENABLE_CLAUDE_CLI: true
ENABLE_CODEX_CLI: true
AGENTIC_CODING_TOOLS: claude-code, codex-cli, gemini-cli

## Instructions

- Based on the user's request, follow the `Cookbook` section to determine which tool to use.

### Fork Summary User Prompts

- IF: The user requests a fork terminal with a summary. This ONLY works for our agentic coding tools 'AGENTIC_CODING_TOOLS'. The tool MUST BE enabled as well.
- THEN: 
  - Read, and REPLACE the ".claude/skills/fork-terminal/prompts/fork_summary_user_prompt.md with the history of the conversation between you and the user so far.
  - include the next users request in the 'Next User Request" section.
  - this will be what you pass into the PROMPT parameter of the agentic coding tool.
  - IMPORTANT: to be clear, don't update the file directly, just read it, and use it to craft a new prompt in the structure provided for the new fork
- EXAMPLES:
- "fork terminal use claude code to <xyz> summarize work so far"
- "spin up a new terminal request <xyz> using claude code include summary"
- "create a new terminal to <xyz> with claude code with summary"

## Workflow

1.understand the user's request
2.READ: `.claude/skills/fork-terminal/tools/fork_terminal.py` to understand our tooling.
2.Follow the `Cookbook` section to determine which tool to use.
3.Execute the `.claude/skills/fork-terminal/tools/fork_terminal.py: fork_terminal(command: str)` tool.

## Cookbook



## Raw CLI Commands
- IF: the user requests a non-agentic coding tool AND `ENABLE_RAW_COMMANDS` is true,
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/cli-command.md`
-EXAMPLES:
  - "Create a new terminal to <xyz>"
  - "Create a new terminal and run <xyz>"
  - "Fork terminal and run <xyz>"

## Claude Code

- IF: the user requests a claude code agent to execut the command AND `ENABLE_CLAUDE_CODE` is true,
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/claude-code.md`
-EXAMPLES:
  - "fork terminal use claude code to <xyz>"
  - "spin up a new ternminal request <xyz> using claude code"


## Codex CLI

- IF: the user requests a codex cli agent to execute the command AND `ENABLE_CODEX_CLI` is true,
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/codex-cli.md`
- EXAMPLES:
  - "fork terminal using codex to <xyz>"
  - "create a new terminal with codex-cli running <xyz>"
  - "run <xyz> in a new terminal via codex cli"


## Gemeni CLI

- IF: the user requests a gemeni cli agent to execute the command AND `ENABLE_GEMENI_CLI` is true,
- THEN: Read and execute: `.claude/skills/fork-terminal/cookbook/gemeni-cli.md`
- EXAMPLES:
  - "fork terminal using gemeni to <xyz>"
  - "start a new terminal window and run <xyz> with gemeni cli"
  - "create new terminal via gemeni and execute <xyz>"