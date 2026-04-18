#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

import subprocess
import shlex


def fork_terminal(command: str, cwd: str = None) -> str:
    if cwd is None:
        import os
        cwd = os.getcwd()
    full_command = f"cd {shlex.quote(cwd)} && {command}"
    script = f'tell application "Terminal" to do script "{full_command}"'
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip() or result.stderr.strip()


if __name__ == "__main__":
    import sys
    print(fork_terminal(sys.argv[1] if len(sys.argv) > 1 else "echo hello"))
