# これは何？
Python用Mildom APIの非公式ライブラリです。
開発途中です。

# 対応状況
- ProfileV2 API

# 対応予定
- Playback API

# 注意
あくまでも**非公式APIの非公式ラッパー**です。開発が継続される保証はありません。
開発者は募集中です。

# 使い方
- ユーザーオブジェクトを作成して詳細を取得<br>
情報を更新する時は、Userオブジェクトを再作成してください。updateメソッドも追加予定。
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