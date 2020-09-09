# 目的
ここではPolityLink開発者向けの情報をまとめています。

## Pyenv
PolityLinkではPythonのバージョンの管理にPyenvを使っています。
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"
```
* 詳しくは[公式ドキュメント](https://github.com/pyenv/pyenv)参照

3.6.1以上のpythonを入れておきましょう。
```
pyenv install 3.8.2
pyenv local 3.8.2
```

## Poetry
PolityLinkではPythonのパッケージの管理にPoetryを使っています。
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
* 詳しくは[公式ドキュメント](https://python-poetry.org/docs/)参照

試しにpolitylink-common用のpoetry環境を構築しましょう。
```
git clone https://github.com/politylink/politylink-common.git
cd politylink-common
poetry install
```
* デフォルトでは`~/Library/Caches/pypoetry/virtualenvs`に仮想環境が作られます。
* `poetry run ${command}`もしくは`poetry shell`で仮想環境でスクリプトを実行できます。
* `poetry add`で依存ライブラリを追加できます。
* `poetry update`で依存ライブラリを更新できます。

## PyCharm
PolityLinkではPythonの統合開発環境である[PyCharm](https://www.jetbrains.com/ja-jp/pycharm/)を使って開発をしています。

### 基本設定
* [poetry plugin](https://plugins.jetbrains.com/plugin/14307-poetry)を入れる
    * Poetry InterpreterをProject Interpreterとして設定できるようになる
* pytestを実行できるようにする
   * PycharmのデフォルトテストをUnitTestからpytestに変更する（[参考](https://pleiades.io/help/pycharm/pytest.html)）
      * Preferences -> Tools -> Python Integrated Tools
      * pytestの関数の横に実行アイコンが出ることを確認
   * tests以下の全てのテストをまとめて実行するための新しいRun configurationを設定する
        * Target directory と Working directoryをtestsに設定したpytest configurationを追加する

### プロジェクトを開く
* 1つのwindowでpolitylinkに関する全てのプロジェクト（e.g. politylink-common, politylink-crawler, etc）を開くことができます。
    * 2つ目以降を開く時はFile -> Open -> Detach
* プロジェクトごとに異なるinterpreterを設定できます。
    * Preferences -> Project -> Project InterpreterからそれぞれのプロジェクトのPoetry Interpreterを選択
* プロジェクト間で依存関係を定義できます。
    * Preferences -> Project -> Project Dependencies
    * 例えばpolitylink-crawlerをpolitylink-commonに依存させると、poetry環境のpolitylink-commonではなく、ローカルのpolitylink-commonに基づいてコード補完やコードジャンプが行われるようになります。


## FAQ
* politylinkパッケージを更新したいとき
    * politylink-commonは他のレポジトリやjupyter notebookなどの解析環境から呼び出せるように[PyPI](https://pypi.org/project/politylink/)にパッケージを公開しています。
    * Poetryを使ってパッケージを公開できます。必要に応じてバージョンをpyproject.tomlから変更してください。
```
poetry build  # build tar.gz and wheel under ./dist
poetry publish  # publish to PyPI, auth required
```

* 単体テストを実行したいとき
    * 例えばpolitylink-commonではpytestによるテストコードが書いてあります。
```
poetry run pytest
poetry run pytest -o log_cli=true  # enable logging
```   

* GraphQLスキーマを更新したいとき
    1. politylink-backendのapi/src/schema.graphqlを更新する
    2. politylink-backendのコンテナを再起動する
    3. politylink-commonのpolitylink/graphql/schema.pyをschema.shで更新する
```
cd politylink-common/politylink/graphql
poetry run bash schema.sh
```

* ローカルのGraphQLエンドポイントを使いたいとき
    * 例えば新しいクローラーのテストをしているときなど、ローカルで立てたGraphQLエンドポイントを使いたい場合があります。
    * POLITYLINK_URLとPOLITYLINK_AUTHという2つの環境変数をローカルのエンドポイント用に変更しましょう。
    * 例えば`~/.bash_profile`に以下のように書いておけばデフォルトでローカルを使うようにできます。
```
export POLITYLINK_URL='http://localhost:4000/'
export POLITYLINK_AUTH=
```

* ローカルのpolitylink-commonライブラリを他のレポジトリから使いたい場合
    * 例えばpolitylink-crawlerとpolitylink-commonを同時に更新しているときなど、ローカルのpolitylink-commonをpolitylink-crawlerから呼び出したい場合があります。
    * ローカルでbuildされたtar.gzを直接pipでinstallすることができます。
    * PyCharm上ではDependenciesを設定することでローカルのコードを優先できます。
```
cd politylink-crawler
poetry shell # activate poetry environment of politylink-crawler
pip install ../politylink-common/dist/politylink-0.1.9.tar.gz
```
   

