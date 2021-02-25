[![Downloads](https://pepy.tech/badge/mildom)](https://pepy.tech/project/mildom)
[![Downloads](https://pepy.tech/badge/mildom/month)](https://pepy.tech/project/mildom)
[![Downloads](https://pepy.tech/badge/mildom/week)](https://pepy.tech/project/mildom)

# これは何？
Python用Mildom APIの非公式ライブラリです。
開発途中です。<br>バグがあればGithubのissueをお願いします。<br>
If you find any bugs, please report it on issues by English or Japanese.

# 対応状況
- ProfileV2 API
- PlayBack API

# 対応予定
- async/await(非同期処理)

# 注意
あくまでも**非公式APIの非公式ラッパー**です。開発が継続される保証はありません。
開発者は募集中です。

# 使い方
- ユーザーオブジェクトを作成して詳細を取得<br>
情報を更新する時は、User.updateで情報を更新できます。
## Userオブジェクト -ProfileV2 API-
```python
import mildom
user_id = 12345678

#8桁のIDを指定してユーザーオブジェクトを作成
user = mildom.User(user_id)

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

## PlayBackオブジェクト -PlayBack API-
```python
import mildom
user_id = 12345678
user = mildom.User(user_id)

playback_list = user.fetch_playback()
for playback in playback_list:
    # タイトル
    print(playback.title)
    
    # 視聴用URL
    print(playback.url)
    
    # MP4のURL
    print(playback.source_url)    
    
    # ゲームの情報
    print(playback.game_info)
    # > {'game_name': 'マインクラフト（Minecraft）(PC&Console)', 'game_type': 'pc'}
    
    # 配信者(Userオブジェクト)
    print(playback.author)
    
    # 配信時刻(datetimeオブジェクト)
    print(playback.publish_time)
    
    # アーカイブのID(v_id)
    print(playback.v_id)
```
## アーカイブダウンロード
```python
import mildom
user_id = 12345678
user = mildom.User(user_id)
playback = user.fetch_playback()[0]

# アーカイブを配信タイトルでダウンロード
playback.download(directory='/download')

# ファイル名を指定してダウンロード
playback.download(directory='/download', name='file.mp4')
```
