# VCleaner
[![MIT](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/kanno2inf/VCleaner/blob/master/LICENSE)

VRMファイルに含まれる不要テクスチャを削除するスクリプト

## 動作環境
* python 3.8.x

## ダウンロード
* 開発最新版 : [こちら](https://github.com/kanno2inf/VReducer/archive/master.zip) からダウンロード

## 使い方
```bash
$ python vcleaner.py [VRM_FILE_PATH] [-f|--force] [-h|--help] [-V|--version]
```
※実行環境によっては```python3, python3.8```を指定して実行する必要があります。

VRM_FILE_PATH: VRMファイルパス

-f, --force: ファイル保存時、確認なしに上書きする

-h, --help: ヘルプ表示

-V, --version: バージョン表示

変換後のファイルは以下のフォルダ以下に出力されます。
```
result
```
