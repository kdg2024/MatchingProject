# MatchingProject
## 目的
授業を通してDjangoの基本を一巡した人向けの復習＆発展用教材．
何もない白紙の状態からマニュアルに従って進めることで，
必要最低限の機能だけを有している
（デザインなどは微塵も考えていない）
mainブランチにあるものと同じものが作成可能である．
そして，これをベースとして自由にカスタマイズして素晴らしいアプリを作ってもらいたい．

## アプリ概要
メンターとメンティーのマッチングアプリ．
メンターを探している人が
一覧の中から気になるメンターとを探し，
プロフィールを確認したあと
ダイレクトメッセージでやりとりをすることができる．
内部の構造（特に**カスタムユーザー**とデータベースにおける**多対多**
，共に教科書には載っていない）
に焦点をあてているため**デザインに関しては1mmも考えていない**．
自作のcssはサンプルとして一つ入れてあるのみで，
他にBootstrapを一部で利用している程度である．
そのため，デザインは各自で自由に行うこと．

## マニュアル
本リポジトリと同じものを0から作るためのマニュアル．
1. [機能](doc/function.md)
1. 制作
    1. [仮想環境（任意）](doc/environment.md)
    1. [初期設定](doc/settings.md)
    1. [カスタムユーザーとログイン機能（accountsアプリ）](doc/custom_user.md)
    1. [matchingアプリ](doc/matching.md)
    1. [messageアプリ](doc/message.md)
    1. [その他・デバッグ](doc/other_debug.md)
1. [デプロイ](doc/deploy.md)

## おまけ
- Git基礎マニュアル(comming soon)

## その他・補足
- 本リポジトリ内において「教科書」とは，秀和システム社より発刊されている「Djangoのツボとコツがゼッタイにわかる本[第2版] 」のことである．

