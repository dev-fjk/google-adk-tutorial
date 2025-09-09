# Copilot Instructions for google-adk-tutorial

## プロジェクト概要

このリポジトリは Google ADK (Agent Development Kit) のチュートリアル用です。`multi_tool_agent/` ディレクトリ配下に、都市の天気や時刻を返すエージェントの実装例が含まれています。

## 主要構成

- `multi_tool_agent/agent.py`: エージェントの主要ロジック。Google ADK の `Agent` クラスを継承し、天気 (`get_weather`) と時刻 (`get_current_time`) のツール関数を提供。
- `multi_tool_agent/__init__.py`: モジュール初期化。
- `pyproject.toml`, `uv.lock`: Python パッケージ管理用。

## 開発・実行ワークフロー

- **仮想環境**: `.venv` ディレクトリを利用。PowerShell では `& .venv\Scripts\Activate.ps1` で有効化。
- **依存管理**: `uv` コマンドまたは `pyproject.toml`/`uv.lock` を利用。
- **起動例**: `adk web --no-reload` でエージェントの Web サーバーを起動（`adk` コマンドは Google ADK の一部）。
- **テスト**: テストコードは現状未実装。追加時は `tests/` ディレクトリを作成し、pytest などを利用。

## コーディング規約・パターン

- **ツール関数**: エージェントのツールは Python 関数として実装し、`tools=[...]` で `Agent` に登録。
- **エラーハンドリング**: 返り値は `status` キーで成功/失敗を明示し、失敗時は `error_message` を含める。
- **日本語対応**: ユーザー向けメッセージやコメントは日本語で記述。
- **拡張**: 新しい都市や機能を追加する場合は、既存のツール関数パターンに倣う。

## 参考

- [Google ADK 公式チュートリアル](https://google.github.io/adk-docs/tutorials/agent-team/)
- `README.md` も参照

---

- 主要なロジックやワークフローは `multi_tool_agent/agent.py` を参照。
- 不明点や追加ルールがあれば `README.md` も確認。
