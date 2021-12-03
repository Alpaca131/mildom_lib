from _warnings import warn
from datetime import datetime

import mildom
from mildom import api_request


class User:
    def __init__(self, user_id: int):
        if not isinstance(user_id, int):
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
        self.avatar_url: str = user_info.get('avatar')
        self.fans: int = user_info.get('fans')
        self.is_live: bool = live
        self.level: int = user_info.get('level')
        self.name: str = user_info.get('loginname')
        self.official: bool = official
        self.live_description: str = user_info.get('intro')
        self.exp: float = user_info.get('exp')
        self.country: str = user_info.get('exp')
        self.id: int = user_info.get('user_id')
        self.sex: int = user_info.get('sex')
        self.status: int = user_info.get('status')
        self.user_album: list = user_info.get('user_album')
        self.viewers: int = user_info.get('viewers')
        self.gift_revenue: int = user_info.get('gift_revenue_history')
        self.latest_live_title: str = user_info.get('anchor_intro')
        self.latest_live_thumbnail: str = user_info.get('pic')
        self.latest_live_tags: list = user_info.get('live_tags')
        self.birth: str = user_info.get('birth')

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


class LiveStream:
    def __init__(self, user_id: int):
        if type(user_id) is not int:
            raise TypeError(f'must be int, not {type(user_id).__name__}')
        response = api_request.live_info_request(user_id)["body"]
        # 配信
        if response["anchor_live"] == 11:
            self.is_live = True
        else:
            self.is_live = False
        self.title = response.get("anchor_intro")
        self.description = response.get("live_intro")
        self.resolutions: list = []
        for i in response["ext"]["cmode_params"]:
            self.resolutions.append(str(i["pixel"]) + "p")
        self.special_gift_list = response.get("ext").get("special_gift_list")
        self.started_since = datetime.fromtimestamp(int(str(response.get("live_start_ms"))[:-3]))
        self.thumbnail_url = response.get("pic")
        self.viewers = response.get("viewers")
        self.playback_permission = response.get("playback_permission")
        if response.get("realtime_playback_on") == 1:
            self.is_dvr_enabled = True
            dvr_info = response["realtime_playback_info"]
            self.dvr_audio_url = {"audio_url": dvr_info["audio_url"]}
            self.dvr_videos = dvr_info["video_link"]
        else:
            self.is_dvr_enabled = False
            self.dvr_audio_url = None
            self.dvr_videos = None
        # 配信者
        self.author_id = user_id
        self.author_name = response.get("loginname")
        self.author_avatar_url = response.get("avatar")
        self.author_fans = response.get("fans")
        self.author_level = response.get("level")
        self.author_description = response.get("intro")

    def get_user(self):
        return User(self.author_id)

    def update(self):
        self.__init__(self.author_id)


def is_live(user_id: int) -> bool:
    if type(user_id) is not int:
        raise TypeError(f'must be int, not {type(user_id).__name__}')
    response = api_request.profile_v2_request(user_id)
    anchor_live = response['body']['user_info']['anchor_live']
    if anchor_live == 11:
        return True
    else:
        return False


class SearchResult:
    def __init__(self, res: dict):
        self.clip_videos: list = res.get("clip_video")
        self.live_streams: list = res.get("live_anchors")
        self.recommended_live_streams: list = res.get("rec_live_anchors")
        self.videos: list = res.get("user_video")
        self.users: list = res.get("users")
        self.playbacks: list = res.get("video_list")


def search(query: str, category=None) -> SearchResult:
    category_dict = {"user": 1,
                     "live_stream": 2,
                     "video": 3,
                     "playback": 4,
                     "recommended_live_stream": 5,
                     "clip_video": 6}
    if category is None:
        response = api_request.search_request(query)["body"]
        search_result = SearchResult(response)
    else:
        if category in category_dict:
            type_code = category_dict[category]
            response = api_request.search_request(query, type_code)["body"]
            search_result = SearchResult(response)
        else:
            raise ValueError(
                """
"category" arguments must be one of these: 
["user", "live_stream", "video", "playback", "recommended_live_stream", "clip_video"]
                """
            )
    return search_result
