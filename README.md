[![Downloads](https://pepy.tech/badge/mildom)](https://pepy.tech/project/mildom)
[![Downloads](https://pepy.tech/badge/mildom/month)](https://pepy.tech/project/mildom)
[![Downloads](https://pepy.tech/badge/mildom/week)](https://pepy.tech/project/mildom)

# これは何？
Python用Mildom APIの非公式ライブラリです。
開発途中です。<br>バグがあればGithubのissueをお願いします。<br>
This is an unofficial api wrapper for Mildom.
If you find any bugs, please report it on issues by English or Japanese.

# 対応状況
- ProfileV2 API
- PlayBack API (配信アーカイブ)

# 対応予定
- async/await(非同期処理)
- PlayBack APIでのアーカイブの範囲取得

# 注意
あくまでも**非公式APIの非公式ラッパー**です。開発が継続される保証はありません。
開発者は募集中です。

# 破壊的変更
バージョン2.0には破壊的変更を含みます。
```python
from mildom import api_request
```
# 使い方
- ユーザーオブジェクトを作成して詳細を取得<br>
情報を更新する時は、User.updateで情報を更新できます。
## Userオブジェクト -ProfileV2 API-
```python
import mildom
user_id = 12345678

# 8桁のIDを指定してユーザーオブジェクトを作成
user = mildom.User(user_id)
```
Examples: 
```python
# bool値でライブ中かどうかを取得
print(user.is_live)

# プロフィールの画像URLを取得
print(user.avatar_url)

# レベルを取得
print(user.level)
```

- ライブ中かどうかだけを取得
```python
import mildom
user_id = 12345678

if mildom.is_live(user_id):
    print('now on live')
```

## PlayBack(アーカイブ)オブジェクト -PlayBack API-
- 複数のアーカイブをリストで取得
```python
import mildom
user_id = 12345678
user = mildom.User(user_id)

# "limit" argument is optional.
playback_list: list = user.fetch_playback(limit=10)
```
- 特定のアーカイブを取得(fetch specific PlayBack)
```python
import mildom
user_id = 12345678
user = mildom.User(user_id)

# index starts from 0.
playback = user.fetch_playback(index=10)
```
Examples:
```python
# URLを取得
print(playback.url)
# タイトルを取得
print(playback.title)
# MP4のURLを取得
print(playback.source_url)
```
### 注意
「最新から2番目のアーカイブを取得したい」といった場合にはindexを指定してください。  
使用しているAPIが異なるため、レスポンスを高速化できます。  
以下は指定範囲のアーカイブをランダムに取得するテストにおけるレスポンス時間の平均値です。
```
0~425
index api time: 0.045539161014556885
----------------------------------------------
legacy api time: 0.06734103298187255


200~425
index api time: 0.049199145197868346
----------------------------------------------
legacy api time: 0.08169150960445404

300~425
index api time: 0.049523269319534304
----------------------------------------------
legacy api time: 0.10116533222198486
```