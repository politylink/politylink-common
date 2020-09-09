## インストール
```
pip install politylink
```

## 使い方

### GraphQLClient

PolityLinkの[GraphQLエンドポイント](https://graphql.politylink.jp/)にアクセスするためのGraphQLClientが用意されています。
```
from politylink.graphql.client import GraphQLClient
client = GraphQLClient()
```

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
2020年1月20日に提出された3つの法律案の名前が得られるはずです。
```
{'data': {'Bill': [{'name': '特定複合観光施設区域の整備の推進に関する法律及び特定複合観光施設区域整備法を廃止する法律案'},
   {'name': '地方交付税法及び特別会計に関する法律の一部を改正する法律案'},
   {'name': '平成三十年度歳入歳出の決算上の剰余金の処理の特例に関する法律案'}]}}
```

GraphQLClientは[sgglc](https://github.com/profusion/sgqlc)のラッパークラスであり、クエリをコードで組み立てることも可能です。例えば上のクエリを組み立てると以下のようになります。
```
from politylink.graphql.schema import Query, _BillFilter, _Neo4jDateTimeInput
from sgqlc.operation import Operation

op = Operation(Query)
bill_filter = _BillFilter(None)
bill_filter.submitted_date = _Neo4jDateTimeInput(year=2020, month=1, day=20)
bills = op.bill(filter=bill_filter)
bills.name()
client.exec(op)
```
