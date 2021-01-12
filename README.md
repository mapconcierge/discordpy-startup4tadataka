# discordpy-startup

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## 伊能忠敬Botの実装状況

### 「忠敬さん」コマンド使用方法
* 忠敬さん教えて → 大事なメッセージを回答
* 忠敬さん助けて → 総合案内チャンネルへ誘導

* メンテナンス用コマンド
   - 忠敬さんping → 「ぽん」 と回答
   - 忠敬さんmap → 地図に関する何かを回答


### 今後のロードマップ
- 定期アナウンス機能実装
- 適宜リアクション追加

### バグ報告や機能要望
- [Issuesで管理](https://github.com/mapconcierge/discordpy-startup4tadataka/issues)




--- 以下は本家ドキュメント

- Herokuでdiscord.pyを始めるテンプレートです。
- Use Template からご利用ください。
- 使い方はこちら： [Discord Bot 最速チュートリアル【Python&Heroku&GitHub】 - Qiita](https://qiita.com/1ntegrale9/items/aa4b373e8895273875a8)

## 各種ファイル情報

### discordbot.py
PythonによるDiscordBotのアプリケーションファイルです。

### requirements.txt
使用しているPythonのライブラリ情報の設定ファイルです。

### Procfile
Herokuでのプロセス実行コマンドの設定ファイルです。

### runtime.txt
Herokuでの実行環境の設定ファイルです。

### app.json
Herokuデプロイボタンの設定ファイルです。

### .github/workflows/flake8.yaml
GitHub Actions による自動構文チェックの設定ファイルです。

### .gitignore
Git管理が不要なファイル/ディレクトリの設定ファイルです。

### LICENSE
このリポジトリのコードの権利情報です。MITライセンスの範囲でご自由にご利用ください。

### README.md
このドキュメントです。
