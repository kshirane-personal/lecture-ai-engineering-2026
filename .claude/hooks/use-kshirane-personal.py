"""Claude Code の PreToolUse フック：このリポジトリで gh コマンドを実行するときは kshirane-personal で認証する。

gh の「有効なアカウント」は切り替えない（別のリポジトリでの作業に影響させないため）。
代わりに、gh を含むコマンドの先頭で GH_TOKEN に kshirane-personal のトークンを入れてから実行させる。
git（push / pull / fetch）は、このリポジトリの .git/config の credential helper で同じアカウントにしている。
"""

import json
import re
import shutil
import subprocess
import sys

ACCOUNT = "kshirane-personal"
GH = shutil.which("gh") or "/opt/homebrew/bin/gh"

data = json.load(sys.stdin)
tool_input = data.get("tool_input", {})
command = tool_input.get("command", "")

# 単語としての gh を含むコマンドだけを対象にする（例：gh pr create、cd x && gh api user）
if not re.search(r"(^|[\s;&|(])gh\s", command):
    sys.exit(0)
# gh auth（ログイン・切り替え・状態確認）は対象外。GH_TOKEN があると gh が切り替えなどを受け付けないため
if re.search(r"(^|[\s;&|(])gh\s+auth\s", command):
    sys.exit(0)

token = subprocess.run(
    [GH, "auth", "token", "--hostname", "github.com", "--user", ACCOUNT],
    capture_output=True, text=True,
)
if token.returncode != 0 or not token.stdout.strip():
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": f"gh に {ACCOUNT} でログインしていないため止めました。"
                                    f"`gh auth login` で {ACCOUNT} を追加してください。",
    }}))
    sys.exit(0)

# トークンの値はコマンドに書かず、実行時に取り出させる
prefix = f'export GH_TOKEN="$({GH} auth token --hostname github.com --user {ACCOUNT})"; '
print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "updatedInput": {**tool_input, "command": prefix + command},
}}))
