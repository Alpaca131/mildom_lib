import requests


class User:
    def __init__(self, user_id: int):
        if type(user_id) is not int:
            raise TypeError(f'must be int, not {type(user_id).__name__}')
        response = profile_v2_request(user_id)
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
        self.gift_revenue_history = user_info['gift_revenue_history']
        self.avatar_url = user_info['avatar']
        self.fans = user_info['fans']
        self.is_live = live
        self.level = user_info['level']
        self.name = user_info['loginname']
        self.official = official
        self.live_description = user_info['intro']
        self.exp = user_info['exp']
        self.country = user_info['country']
        self.id = user_info['user_id']
        self.sex = user_info['sex']
        self.status = user_info['status']
        self.user_album = user_info['user_album']
        self.viewers = user_info['viewers']
        self.gift_revenue = user_info['gift_revenue_history']
        self.latest_live_name = user_info['anchor_intro']
        self.birth = user_info['birth']


def is_live(user_id: int) -> bool:
    if type(user_id) is not int:
        raise TypeError(f'must be int, not {type(user_id).__name__}')
    response = profile_v2_request(user_id)
    anchor_live = response['body']['user_info']['anchor_live']
    if anchor_live == 11:
        return True
    else:
        return False


def profile_v2_request(user_id: int) -> dict:
    url = f"https://cloudac.mildom.com/nonolive/gappserv/user/profileV2?user_id={user_id}&__platform=web"
    response = requests.get(url).json()
    return response
