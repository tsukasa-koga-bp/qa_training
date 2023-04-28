# タイタニック生存判定アプリ

もし、あなたがタイタニック号に乗っていたら生き残れるかどうか判定してくれる。
kaggleのタイタニックのデータセットを用いた簡単な機械学習アプリケーション。


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

## 開発

- 新規のライブラリをインストール
    - 例えばnumpyをインストールする場合のコード
    - ```poetry add numpy --dev```

- 実行
    - 入力データの投入
        - データのダウンロード
            - https://www.kaggle.com/competitions/titanic/data
            - download all
        - データ配置
            - (configを変更しなければ)
            - ```data/input/```にtrain.csvとtest.csvを配置

    - 実行
        - ```make run```
            - ```data/model```にmodel.pkl
                - 学習済みモデル
            - ```data/output```にdf_results.csv
                - 生存判定結果