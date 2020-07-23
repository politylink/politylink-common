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

## PyCharmの設定
* set poetry interpreter as project intepreter
    * add poetry plugin first
        * https://plugins.jetbrains.com/plugin/14307-poetry
    * Preferences -> Project -> Project Interpreter and select the target poetry virtualenv
* change default testing to pytest from UnitTest
    * https://pleiades.io/help/pycharm/pytest.html
    * Preferences -> Tools -> Python Integrated Tools
    * add a new Run configuration to run all pytest in
        * set test directory as Target and Working directory

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