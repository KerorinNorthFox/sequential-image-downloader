# Sequential image downloader
画像まとめサイトの画像を上から順にダウンロードして保存する

# インストール
```
$ git clone git@github.com:KerorinNorthFox/sequential-image-downloader.git
$ cd sequential-image-downloader
$ python -m pip install -r requirements.txt
```

## 実行環境
```
Windows 11
python >= 3.11.3
```

# ディレクトリ構造
```
sequential-image-downloader
|-save                # ここにドメインごとに画像が保存されていく
  |-example.com       # 例
|-image_dl.py         # 画像をダウンロードするクラス
|-logger.py           # ログを出力するクラス
|-main.py             # これを実行する
|-selector.json       # ここにサイトごとのcssセレクタを書いていく
|-uri.py              # uriクラス
|-urls.txt            # ここにダウンロードしたいページを入れていく
```

# 使い方
## 0. 最初にすること
main.pyと同じディレクトリにselector.jsonとurls.txtを作成する。
## 1. URLを登録する
selector.jsonに保存したい画像まとめサイトのURLごとに画像のCSSセレクタを指定する
### selector.jsonのフォーマット
```json
"example.com":{
  "selectors":[
    "body > div > a:nth-child(xxxx) > img",
    "body > div > img.nth-child(xxxx)"
  ],
  "offset":1,
  "isNecessaryFileNumber":false
},
"example2.com":{
  "selectors":[
    "#post-yyyy > div > a:nth-child(xxxx) > img",
    "#post-yyyy > div > img:nth-child(xxxx)"
  ],
  "offset":1,
  "isNecessaryFileNumber":true
}
.
.
.
```
### selector.jsonの各項目の説明
|key|type|description|
|:-|:-|:-|
|selectors|list[str]|imgタグまでのcssセレクタを登録する<br>xxxxはoffsetの値が入る<br>yyyyにはURLの末尾の番号が入る想定|
|offset|int|画像が始まる番号<br>cssセレクタを抽出する際に、一番先頭の画像のimgタグを選択し、nth-child(番号)の番号の部分をoffsetとする|
|isNecessaryFileNumber|bool|selectorsでyyyyが有効になる|

```
$ python main.py
```

## 2. URLをファイルに入力
ダウンロードしたいページのURLをurls.txtに入力する。

改行して指定することで複数のページの画像をを一度にダウンロードできる。
### urls.txtのフォーマット
```
example.com/post/index.html
example2.com/post/0001
```
※ ファイル末尾に改行を入れないこと

## 3.実行
main.pyを実行する
```
$ python main.py
```

# yyyyについて
TODO