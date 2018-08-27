# pixiv-dl-ver2
Pixivから画像を取得するためのツール

### 設定
①依存パッケージのインストール  
プロジェクトディレクトリでpackage.txtをインストール

```
$ pip install -r package.txt
```

②setting.pyを変更
```
# pixiv id and client password
pixiv_id = 'XXXXXXXXXX'           ← ピクシブID
client_password = 'XXXXXXXXXX'    ← クライアントパスワード
```

### 実行

```
$ python pixiv_image_downloader.py
取得したい絵師のページID(start)を入力してください。>>>      # ページIDを入力
取得したい絵師のページID(end)を入力してください。>>>        # ページIDを入力
取得タグを指定してください。>>>                            # 対象とするタグを指定(未入力の場合はすべてを対象とする)

```
