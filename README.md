## インストール
```
pip install politylink
```
`politylink.nlp.keyphrase`を使用する場合は、追加で以下を実行してください。
```
pip install git+https://github.com/boudinfl/pke.git
python -m nltk.downloader stopwords
```
## 使い方

### GraphQLClient

PolityLinkの[GraphQLエンドポイント](https://graphql.politylink.jp/)にアクセスするためのGraphQLClientが用意されています。
```
from politylink.graphql.client import GraphQLClient
client = GraphQLClient()
```

#### 基本編

`exec`メソッドを使えば任意のGraphQLクエリを実行することができます。
```
query = """
query {
  Bill(filter: {submittedDate: {year: 2020, month: 1, day: 20}}) {
    name
  }
}
"""
client.exec(query)
```
2020年1月20日に提出された3つの法律案の名前がJSON形式で得られるはずです。
```
{'data': {'Bill': [{'name': '特定複合観光施設区域の整備の推進に関する法律及び特定複合観光施設区域整備法を廃止する法律案'},
   {'name': '地方交付税法及び特別会計に関する法律の一部を改正する法律案'},
   {'name': '平成三十年度歳入歳出の決算上の剰余金の処理の特例に関する法律案'}]}}
```

また、`get_all_*`メソッドを使うことで、返り値をJSONではなくPythonクラスのインスタンスとして取得することができます。
例えば`get_all_bills`では法律案をBillインスタンスとして取得することができます。

```
bills = client.get_all_bills(fields=['id', 'name'])
first_bill = bills[0]

print(f'{len(bills)}件の法律案を取得しました')
print(f'最初の法律案は「{first_bill.name}」（{first_bill.id}）です')
```

全ての法律案のidと名前（name）が得られるはずです。
返り値はBillインスタンスなので、ドットを使って各フィールドにアクセスできます。
```
207件の法律案を取得しました
最初の法律案は「地方交付税法及び特別会計に関する法律の一部を改正する法律案」（Bill:s1QZfjoCPyfdXXbrplP3-A）です
```

また`filter_`を引数に渡すことで条件を指定して取得することもできます。詳しくは応用編を見てください。


#### 応用編

GraphQLClientは[sgqlc](https://github.com/profusion/sgqlc)のラッパークラスであり、クエリをコードで組み立てることも可能です。
例えば最初の`exec`の例のクエリを組み立てると以下のようになります。

```
from politylink.graphql.schema import Query, _BillFilter, _Neo4jDateTimeInput
from sgqlc.operation import Operation

op = Operation(Query)
filter_ = _BillFilter(None)
filter_.submitted_date = _Neo4jDateTimeInput(year=2020, month=1, day=20)
bills = op.bill(filter=filter_)
bills.name()
client.exec(op)
```

組み立てた`Operation`は自動で文字列に変換されるので`exec`に直接渡すことができます。

また上で作ったfilter_は`get_all_*`メソッドの引数として渡すこともできます。
```
client.get_all_bills(fields=['name'], filter_=filter_)
```

最初の3件の法律案がBillインスタンスとして取得できました。
```
[Bill(name='地方交付税法及び特別会計に関する法律の一部を改正する法律案'),
 Bill(name='平成三十年度歳入歳出の決算上の剰余金の処理の特例に関する法律案'),
 Bill(name='特定複合観光施設区域の整備の推進に関する法律及び特定複合観光施設区域整備法を廃止する法律案')]
```
