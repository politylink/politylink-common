## poetryのinstall
* [公式ドキュメント](https://python-poetry.org/docs/) 参照

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

## パッケージの作成
* pyenvでinstallしたpython3.8.2の環境で以下を実行した。
```
poetry new politylink
cd politylink
poetry add pandas
```
* テストとしてpandasへのdependencyも追加しておいた。addをした時に自動でvirtualenvが`~/Library/Caches/pypoetry/virtualenvs`以下に作成される。

## テストの実行
```
poetry run test
```

## パッケージの配布
```
poetry build
poetry publish
```
* [PyPI](https://pypi.org/project/politylink/) が更新されていることを確認

## パッケージの利用
```
poetry add politylink
poetry run python
>>> from politylink import graphql
>>> graphql.hello()
'graphql'
```

## PyCharmの設定
* poetry interpreterをproject intepreterとして設定する
    * [poetry plugin](https://plugins.jetbrains.com/plugin/14307-poetry)を入れる
    * Preferences -> Project -> Project Interpreter から目的のpoetry virtualenvを選ぶ
* pytestを実行できるようにする
   * PycharmのデフォルトテストをUnitTestからpytestに変更する（[参考](https://pleiades.io/help/pycharm/pytest.html) ）
      * Preferences -> Tools -> Python Integrated Tools
      * pytestの関数の横に実行アイコンが出ることを確認
   * tests以下の全てのテストをまとめて実行するための新しいRun configurationを設定する
        * Target directory と Working directoryをtestsに設定したpytest configurationを追加する
