# ガソリン配送最適化システム
本システムは、ガソリン配送会社によるガソリンスタンドへのガソリン配送を支援する(デモアプリ)。効率的なガソリン配送のために、各ガソリンスタンドのガソリンの使用量の予測を行い、予測に基いた配送ルートを最適化する。

(なお、本システムは社内のとある案件事例を参考に作成している)

## 開発環境構築
### Github Codespacesを利用する場合
- [リポジトリ](https://github.com/majitaki4ryu/qa_training)のCode -> Codespacesから環境を作成
### dev containerを利用する場合
1. 事前準備
    - vscodeとremote devcontainerの拡張をインストール
    - docker環境を用意
    - ```git clone```
2. vscode上で ```dev container rebuild```
### docker-composeを利用する場合
1. 事前準備
    - docker環境を用意
2. ```docker-compose -f ./docker/docker-compose.yml up -d```

## 使い方
アプリの主要なユースケースは以下。

- データ自動生成
    - 各ガソリンスタンドの使用量データ
    - 日々の配送データ
- 使用量予測
    - 予測モデルの学習
    - 予測モデルの予測結果の出力
    - 予測結果の評価
- 配送ルート最適化
    - 配送ルートの出力
    - 配送ルートの評価
- 配送シミュレーション
    - 配送シミュレーション結果の出力
    - 配送シミュレーション結果の評価

## 開発
- 新規のライブラリをインストール
    - 例えばnumpyをインストールする場合のコード
    - ```poetry add numpy --dev```