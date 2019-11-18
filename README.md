# Heroku SchedulerでPythonを定期実行する

- [Heroku SchedulerでPythonを定期実行する](#heroku-scheduler%e3%81%a7python%e3%82%92%e5%ae%9a%e6%9c%9f%e5%ae%9f%e8%a1%8c%e3%81%99%e3%82%8b)
  - [はじめに](#%e3%81%af%e3%81%98%e3%82%81%e3%81%ab)
    - [目的](#%e7%9b%ae%e7%9a%84)
    - [関連する記事](#%e9%96%a2%e9%80%a3%e3%81%99%e3%82%8b%e8%a8%98%e4%ba%8b)
    - [実行環境](#%e5%ae%9f%e8%a1%8c%e7%92%b0%e5%a2%83)
    - [ソースコード](#%e3%82%bd%e3%83%bc%e3%82%b9%e3%82%b3%e3%83%bc%e3%83%89)
  - [シナリオと前提条件](#%e3%82%b7%e3%83%8a%e3%83%aa%e3%82%aa%e3%81%a8%e5%89%8d%e6%8f%90%e6%9d%a1%e4%bb%b6)
  - [事前準備](#%e4%ba%8b%e5%89%8d%e6%ba%96%e5%82%99)
    - [FXレートAPIの作成](#fx%e3%83%ac%e3%83%bc%e3%83%88api%e3%81%ae%e4%bd%9c%e6%88%90)
  - [Schedulerのセットアップ](#scheduler%e3%81%ae%e3%82%bb%e3%83%83%e3%83%88%e3%82%a2%e3%83%83%e3%83%97)
    - [Schedulerの登録](#scheduler%e3%81%ae%e7%99%bb%e9%8c%b2)

## はじめに

Mac環境の記事ですが、Windows環境も同じ手順になります。環境依存の部分は読み替えてお試しください。

### 目的

この記事を最後まで読むと、次のことができるようになります。

- Heroku Schedulerを使ってPythonを定期実行する

`Schedulerの設定`

毎時00分にPythonを実行する。

<img width="400" alt="スクリーンショット 2019-11-16 21.11.16.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/850ae67b-7aa8-59d0-4eb1-6c5a07a0aaf6.png">

### 関連する記事

- [Heroku + Selenium + ChromeでWEBプロセスを自動化する](https://qiita.com/nsuhara/items/76ae132734b7e2b352dd)
- [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler)

### 実行環境

| 環境         | Ver.    |
| ------------ | ------- |
| macOS Mojave | 10.14.6 |
| Python       | 3.7.3   |

### ソースコード

実際に実装内容やソースコードを追いながら読むとより理解が深まるかと思います。是非ご活用ください。

[GitHub](https://github.com/nsuhara/python-scheduler.git)

## シナリオと前提条件

1. 毎時00分にYahoo!ファイナンスのFXチャート・レートから**米ドル/円**を取得してログ出力する。

## 事前準備

### FXレートAPIの作成

1. [Heroku + Selenium + ChromeでWEBプロセスを自動化する](https://qiita.com/nsuhara/items/76ae132734b7e2b352dd)を参照して作成する

## Schedulerのセットアップ

### Schedulerの登録

`本プロセスは事前にクレジットカードの登録が必要となります。(無料枠でも登録が必要となります)`

1. Resources > Add-onsセクションの**Find more add-ons**をクリックします。

    <img width="600" alt="スクリーンショット 2019-11-16 21.05.28.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/a6eca10a-d727-6646-e027-5d7b25c07187.png">

2. **Heroku Scheduler**をクリックします。

    <img width="200" alt="スクリーンショット 2019-11-16 21.06.25.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/c66ca6c7-f734-aa04-a31c-10b3766ffd61.png">

3. **Install Heroku Scheduler**をクリックします。

    <img width="600" alt="スクリーンショット 2019-11-16 21.06.43.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/9f6a6f83-0cf0-6352-a130-5ec9a81a82a0.png">

4. **App to provision to**に**アプリケーション名**を入力します。

    <img width="600" alt="スクリーンショット 2019-11-16 21.07.57.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/72a59a42-2f5c-0819-6ae5-8c2b590e741a.png">

    <img width="600" alt="スクリーンショット 2019-11-16 21.09.14.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/8af4784a-165c-3eb3-705c-2eadc625fbdf.png">

5. **Schedule**に実行周期を設定します。**Run Command**にPythonの実行コマンドを設定します。

    <img width="400" alt="スクリーンショット 2019-11-16 21.11.16.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/ea1737c9-a281-f7d1-4e41-19c2e40f5260.png">
