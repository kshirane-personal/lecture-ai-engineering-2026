# 運用ルール（kshirane-personal のフォーク）

講座が想定する進め方（README の「A：Codespaces で作業」）と、このフォークでの実際の進め方
（B：手元の Mac で Claude Code と協働）の対応を書いたメモです。講座の要件は README と
`lectures/NN/problem.md` が正で、このファイルはそれに合わせるための補足です。

> README.md や lectures/ は講座側が更新するファイルなので、直接は書き換えません
> （書き換えると、講座側の更新を取り込むときに衝突しやすくなるため）。運用の追記はこのファイルに書きます。

## 場所の関係

```
matsuolab/lecture-ai-engineering-2026   （upstream：講座の元リポジトリ。読むだけ）
        │  講座側が教材を追加 → 自分のフォークへ取り込む
        ▼
kshirane-personal/lecture-ai-engineering-2026   （origin：自分のフォーク。提出先）
        │  push / pull
        ▼
~/Developer/lecture-ai-engineering-2026   （手元の作業場所。Cursor で開く）
```

- 提出の PR は **自分のフォークの中** で `lecNN` → `main` に出す。元リポジトリには PR も Issue も出さない
- 元リポジトリへの push は、手元の設定で無効にしてある（`git remote -v` で upstream の push が `DISABLE`）
- フォークは公開状態。answer.md やコードに、業務上の情報・個人情報・API キーを書かない

## 役割分担

| 担当 | やること |
|---|---|
| Claude Code | 各回の解説、実装、テスト実行、git 操作、PR 作成、answer.md の下書き |
| 自分 | 宿題レベルの選択、差分を読んで理解・承認、answer.md の「気づき・疑問」を自分の言葉で書く、Colab での実行 |

## 1回分の流れ

0. **講座側の更新を取り込む**（新しい回が公開されたら）
   - 手元の `main` に upstream を取り込み、フォークへ push する（Claude Code に「最新にして」と頼めばよい）
   - GitHub のフォーク画面の **Sync fork** でも同じことができる。その場合は手元で `git pull` も行う
1. `main` から作業ブランチ `lecNN` を作る（例：`lec03`）
2. 解説を聞き、宿題のレベル（基礎・実装・発展のどれか1つ）を決める
3. 演習と宿題を進める。コードの変更は区切りごとに差分を確認する
4. `uv run pytest -q` が通ることを確認する（PR での自動テストは現状ないため、手元で確認する）
5. `lectures/NN/answer.md` を書く。「取り組んだレベル」の選ばなかったものは消す。
   講座の提出ルールで「選んだレベル・やったこと・結果・使ったモデル」を書くことになっている
6. コミットして `lecNN` をフォークへ push し、PR（`lecNN` → `main`）を作る
7. 内容に納得したら PR を merge する。次の回は、それを含んだ `main` から始める
   （problem.md の「前の回までの作業が終わっている場合は main から」の前提に合わせるため）
8. 講座の提出フォームに、リポジトリの URL（`https://github.com/kshirane-personal/lecture-ai-engineering-2026`）を記入する。
   運営はリポジトリを見に来るので、フォームを送る前に 7 の merge を済ませ、`main` に記入済みの answer.md がある状態にする

### PR を出す前の確認

- [ ] PR の提出先（base repository）が `kshirane-personal/lecture-ai-engineering-2026`、base ブランチが `main`
- [ ] 変更が、その回に関係するファイルだけになっている（WORKFLOW.md や CLAUDE.md の変更を混ぜない）
- [ ] `uv run pytest -q` が通る
- [ ] API キー、`.env`、`learning_log/`（第3回）が含まれていない
- [ ] answer.md の各欄が埋まっている

## 講座の想定（A）と違う進め方をする箇所

answer.md に「手元の Mac で実施」「Copilot の代わりに Cursor を使用」などを一言書いておく。

| 回 | 講座の想定 | このフォークでの扱い |
|---|---|---|
| 全体 | Codespaces、Codespaces secret の `GEMINI_API_KEY` | 手元の Mac。キーは macOS のキーチェーンに保存し、シェルの起動時に環境変数 `GEMINI_API_KEY` として読み込む |
| 第1回 演習6 | Copilot でトークン数の表示を足す | Cursor か Claude Code で行う（README で AI ツールの利用は許可されている） |
| 第2回 | Google Colab（T4 GPU） | **そのまま Colab で実行する**。`result.json` をダウンロードして `lectures/02/` に置き、answer.md の整理は手元で行う |
| 第3回 発展(b) | Pi を **Codespaces の中で** 動かす | Pi は確認なしでファイルの操作やコマンドの実行をするため、手元の Mac では動かさない。この課題を選ぶ場合だけ Codespaces を使う |
| 第5回 発展 | Copilot Chat（VS Code）を MCP クライアントにする | Cursor の MCP 設定（`.cursor/mcp.json`）で同じ用語集サーバーを使い、違いを answer.md に書く |

Codespaces を使うときは、フォークに push 済みの内容から起動する。手元と Codespaces の両方で編集した場合は、
片方で push → もう片方で pull してから続ける。使い終わったら Codespaces を停止する。

## 現状の注意点（2026-11-09 時点）

- `lec03-start` / `lec05-start` タグは、元リポジトリにまだない。前の回を飛ばして始める手順は使えない
- README にある `.github/workflows/test.yml`（PR での自動テスト）は存在しない
- `lectures/02/reference/` には README だけがあり、講師の実行結果のファイルはない
- 提出期限は、リポジトリには書かれていない。講座からの案内で確認する
- 提出は「PR を作る」＋「講座のフォームにリポジトリの URL を記入する」（講座の案内で確認済み、2026-11-09）。
  フォームには「運営が参照できるよう公開リポジトリにする」とあり、このフォークは公開（PUBLIC）になっている
- 講座の提出ルール（スライド）：どれか1つ以上を実施する／AI ツールは使ってよいが、自分で確かめたことを書く／
  API キーを answer.md・コード・ログ・スクリーンショットに書かない／うまくいかなかった結果や差が出なかった結果も、そのまま書く
- 元リポジトリに `.github/workflows/` が追加された場合、それを取り込んでフォークへ push するには、
  GitHub の認証に `workflow` 権限が必要になる（`gh auth refresh -h github.com -s workflow`）
