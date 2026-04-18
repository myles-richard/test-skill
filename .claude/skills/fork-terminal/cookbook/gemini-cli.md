## Purpose

Create a new Gemini CLI agent to execute the command.

## Variables

DEFAULT_MODEL: gemini-3-pro-preview
BASE_MODEL: gemini-3-pro-preview
FAST_MODEL: gemini-2.5-flash

## Instructions
- Before executing the command, run `gemini --help` to understand the command and its options.
- Always use interactive mode (so leave off -p/--prompt)
- For the -m (model) argument, use the DEFAULT_MODEL if not specified. If 'fast' is requested, use the FAST_MODEL.
- Always run with `--yolo` (auto-approve all actions)
