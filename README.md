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
  - アーカイブの範囲取得
- EnterStudio API (ライブ配信)

# 対応予定
- async/await(非同期処理)

# 注意 - notice-
あくまでも**非公式APIの非公式ラッパー**です。開発が継続される保証はありません。  
**This is unofficial wrapper**. There is no guarantee of continuous development.  
開発者は募集中です。  
※バージョン2.0には破壊的変更を含む予定です。

# 使い方 -how to use-
- 下の例に沿って各種オブジェクトを生成して使用する。  
  Use as the instruction below.
- mildom.api_request から各種API1のレスポンスをJSON(dict)で受け取る。  
  Use mildom.api_request to get API response as json(dict).

## Userオブジェクト -ProfileV2 API-
情報を更新する時は、User.updateで情報を更新できます。  
You can refresh the data with User.update.
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

- ライブ中かどうかだけを取得 -get only if it's streaming or not-
```python
import mildom
user_id = 12345678

if mildom.is_live(user_id):
    print('now on live')
```

## PlayBack(アーカイブ)オブジェクト -PlayBack API-
- 複数のアーカイブをリストで取得 -get multiple playbacks as a list-
```python
import mildom
user_id = 12345678
user = mildom.User(user_id)

# "limit" argument is optional.
playback_list: list = user.fetch_playback(limit=10)
```
- 特定のアーカイブを取得 -fetch specific PlayBack-
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
### 注意 -notice-
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

## LiveStream(ライブ配信)オブジェクト -EnterStudio API-

```python
import mildom
live_stream = mildom.LiveStream(user_id)

# 配信状況を取得
print(live_stream.is_live)
# タイトルを取得
print(live_stream.title)
# m3u8形式でストリーミングのURLを取得(VLCなどで再生可能)
if live_stream.is_dvr_enabled:
    # 配信者がDVRを有効にしていないと取得不可
    video_stream_links = live_stream.dvr_videos
```

## Search API
category引数に指定できるstr一覧  
List of str that can be used as the category argument.  
`["user", "live_stream", "video", "playback", "recommended_live_stream", "clip_video"]`
```python
import mildom
search_result: mildom.SearchResult = mildom.search("query")
search_result_with_category_specified = mildom.search("query", category="user")
```
SearchResultオブジェクトの値一覧  
List of variables of SearchResult object.
```python
SearchResult.clip_videos: list
SearchResult.live_streams: list
SearchResult.recommended_live_streams: list
SearchResult.videos: list
SearchResult.users: list
SearchResult.playbacks: list
```