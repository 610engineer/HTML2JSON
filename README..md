# 環仮想環境境立ち上げ
プロジェクトがあるディレクトリでターミナルを開き、以下のコマンド
python -m venv venv
venv\Scripts\activate

ターミナル表示が　(venv) C:\Users\xxx　となればOK

# ライブラリインストール(初回のみ)
仮想環境内に以下のコマンドでインストール
pip install -r requirements.txt