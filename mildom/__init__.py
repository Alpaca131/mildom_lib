from _warnings import warn
from datetime import datetime

from mildom.api_request import api_request


class User:
    def __init__(self, user_id: int):
        if type(user_id) is not int:
            raise TypeError(f'must be int, not {type(user_id).__name__}')
        response = api_request.profile_v2_request(user_id)
        if response['code'] == 1:
            raise ValueError('no user found')
        user_info: dict = response['body']['user_info']
        if 'certification_logo' in user_info:
            official = True
        else:
            official = False
        if user_info['anchor_live'] == 11:
            live = True
        else:
            live = False
        self.avatar_url = user_info.get('avatar')
        self.fans = user_info.get('fans')
        self.is_live = live
        self.level = user_info.get('level')
        self.name = user_info.get('loginname')
        self.official = official
        self.live_description = user_info.get('intro')
        self.exp = user_info.get('exp')
        self.country = user_info.get('exp')
        self.id = user_info.get('user_id')
        self.sex = user_info.get('sex')
        self.status = user_info.get('status')
        self.user_album = user_info.get('user_album')
        self.viewers = user_info.get('viewers')
        self.gift_revenue = user_info.get('gift_revenue_history')
        self.latest_live_title = user_info.get('anchor_intro')
        self.latest_live_thumbnail = user_info.get('pic')
        self.birth = user_info.get('birth')

    def fetch_playback(self, limit: int = 30, index: int = None):
        user_id = self.id
        if type(limit) is not int:
            raise TypeError(f'must be int, not {type(index).__name__}')
        if index is not None:
            if type(index) is not int:
                raise TypeError(f'must be int, not {type(index).__name__}')
            if limit != 30:
                warn('The "limit" argument was ignored because the "index" argument has been passed.')
            limit = 1
            response = api_request.playback_request(user_id, limit, index + 1)
            if response['code'] == 1:
                raise ValueError('no user found')
            playback = PlayBack(response['body'][0], user_id, self)
            return playback
        else:
            response = api_request.playback_request(user_id, limit)
            if response['code'] == 1:
                raise ValueError('no user found')
            body = response['body']
            playback_list = []
            for playback in body:
                playback_list.append(PlayBack(playback, user_id, self))
            return playback_list

    def update(self):
        self.__init__(self.id)


class PlayBack:
    def __init__(self, body: dict, user_id, author: User):
        self.v_id = body.get('v_id')
        self.url = f"https://www.mildom.com/playback/{user_id}/{self.v_id}"
        self.source_url = body.get('source_url')
        self.publish_time = datetime.fromtimestamp(int(str(body.get('publish_time'))[:-3]))
        self.game_info = body.get('game_info')
        self.title = body.get('title')
        self.author = author


def is_live(user_id: int) -> bool:
    if type(user_id) is not int:
        raise TypeError(f'must be int, not {type(user_id).__name__}')
    response = api_request.profile_v2_request(user_id)
    anchor_live = response['body']['user_info']['anchor_live']
    if anchor_live == 11:
        return True
    else:
        return False
