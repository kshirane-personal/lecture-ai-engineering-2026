# このリポジトリでの作業ルール（Claude Code 向け）

AIE2026（AIエンジニアリング実践講座）の演習・宿題を、kshirane-personal のフォーク上で進める。
運用の全体像は @WORKFLOW.md を参照。講座の要件は README.md と `lectures/NN/problem.md` が正。

## 役割

- 利用者の目的は講座内容の理解。実装は Claude が担い、利用者は理解と意思決定を担う
- 各回の始めに、その回の狙いと関係するコードを解説する。宿題のレベルは利用者に選んでもらう
- 実装は小さく区切り、区切りごとに「何を・なぜ変えたか」を説明して承認をもらってから進める
- answer.md は下書きまで。「気づき・疑問」の欄は利用者が自分の言葉で書く（空欄のまま渡し、促す）

## git（グローバル設定の「バージョン管理の代行」より、こちらを優先する）

- GitHub の認証は `kshirane-personal` を使う。作業前に `gh api user --jq .login` で確認し、
  違っていたら `gh auth switch --hostname github.com --user kshirane-personal` で切り替える
- 元リポジトリ（upstream = matsuolab）には、push・PR・Issue・コメントを一切しない
- PR は必ず `gh pr create --repo kshirane-personal/lecture-ai-engineering-2026 --base main` で作る
  （フォークでは、指定しないと提出先が元リポジトリになる）
- 回ごとの作業は `main` から切った `lecNN` ブランチで行う。`lecNN` を `main` に直接 merge しない（PR 経由）
- PR の merge は、利用者の承認を得てから行う
- 「保存して」と言われたら：`lecNN` 上ならコミットして `lecNN` を push する（PR がなければ作るか確認する）
- WORKFLOW.md・CLAUDE.md など運用ファイルの変更は `main` に直接コミットしてよい。`lecNN` の PR に混ぜない
- 「最新にして」と言われたら：`git fetch upstream` → `main` に `upstream/main` を merge → `origin` へ push。
  衝突したらグローバル設定の手順で利用者に確認する。その後 `uv sync --frozen` を実行する

## 環境

- 作業場所は `~/Developer/lecture-ai-engineering-2026`（手元の Mac）。利用者のエディタは Cursor
- 依存パッケージは `uv sync --frozen` で入れる。`uv.lock` と `pyproject.toml` の版は上げない（講座の指定）
- API キーは環境変数 `GEMINI_API_KEY` だけで扱う。値を表示・ファイルに書く・コミットすることはしない
- テストは `uv run pytest -q`（API キー不要）。PR を作る前に必ず実行する
- Gemini の無料枠にはレート制限がある。LLM を呼ぶコマンドは、必要な回数に絞って実行する
- 第2回は Google Colab で利用者が実行する。第3回の発展(b)（Pi）は手元の Mac で動かさない
