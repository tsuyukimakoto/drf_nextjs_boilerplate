# prepare

## poetry のインストール

poetryをホームディレクトリにインストール

`$ curl -sSL https://install.python-poetry.org | python3 -`

PATHに $HOME/.local/bin を追加する

## ライブラリのインストール

`$ poetry install`

## .envの用意

`$ cp .env.example .env`

DJANGO SECRET KEYを生成してDJANGO_SECRET_KEYに設定する（ [ここで生成できる](https://djecrety.ir)）。

## django migrate

`$ poetry run migrate`

## django run development server

`$ poetry run local_server`

