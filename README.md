## poetryのinstall
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
* [公式ドキュメント](https://python-poetry.org/docs/)参照

## poetry環境の構築
```
git clone https://github.com/politylink/politylink-common.git
cd politylink-common
poetry install
```
* `~/Library/Caches/pypoetry/virtualenvs`に仮想環境が作られる

## テストの実行
```
poetry run pytest
poetry run pytest -o log_cli=true  # enable logging
```

## パッケージの配布
```
poetry build
poetry publish
```
* [PyPI](https://pypi.org/project/politylink/)が更新されていることを確認

## パッケージを他のプロジェクトから呼び出す
```
poetry add politylink
poetry run python
>>> from politylink.graphql.client import GraphQLClient
>>> client = GraphQLClient()
```

## PyCharmの設定
* poetry interpreterをproject intepreterとして設定する
    * [poetry plugin](https://plugins.jetbrains.com/plugin/14307-poetry)を入れる
    * Preferences -> Project -> Project Interpreter から目的のpoetry virtualenvを選ぶ
* pytestを実行できるようにする
   * PycharmのデフォルトテストをUnitTestからpytestに変更する（[参考](https://pleiades.io/help/pycharm/pytest.html)）
      * Preferences -> Tools -> Python Integrated Tools
      * pytestの関数の横に実行アイコンが出ることを確認
   * tests以下の全てのテストをまとめて実行するための新しいRun configurationを設定する
        * Target directory と Working directoryをtestsに設定したpytest configurationを追加する
