# python-orangeribbon-donate

子どもの虐待防止運動「オレンジリボン」への寄付を、Python と Selenium を使って自動化するスクリプトです。
## セットアップ手順

仮想環境を作成し、必要なライブラリをインストールします。

```bash
python -m venv venv
source venv/bin/activate  # Windows の場合: venv\Scripts\activate
pip install -r requirements.txt
```

※ `requirements.txt` がない場合は以下で作成できます。

```bash
pip install selenium webdriver-manager
pip freeze > requirements.txt
```

## 実行方法

```bash
python orangeribbon_donate.py
```

実行すると、Chromeブラウザが自動で立ち上がり、フォーム入力から決済までを自動で処理します。  

## ファイル構成

```
python-orangeribbon-donate/
├── orangeribbon_donate.py        # メインスクリプト
├── requirements.txt              # 使用ライブラリ一覧
├── .gitignore                    # 仮想環境などを除外
└── README.md                     # このファイル
```

## 注意事項

- このスクリプトは、寄付フォームの構造が変更された場合に動作しなくなる可能性があります。
- クレジットカード情報などの重要な情報は、**環境変数や .env ファイルを利用して安全に管理**することを推奨します。
- 実行には **Google Chrome** がインストールされている必要があります。
- `webdriver_manager` を使っているため、Chrome のバージョンに合ったドライバは自動で取得されます。

## ライセンス

MIT License
