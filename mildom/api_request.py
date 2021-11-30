import requests


def profile_v2_request(user_id: int) -> dict:
    url = f"https://cloudac.mildom.com/nonolive/gappserv/user/profileV2?user_id={user_id}&__platform=web"
    response = requests.get(url).json()
    if response["code"] == 1:
        raise ConnectionRefusedError("rate limit exceeded. code: 1")
    return response


def playback_request(user_id: int, limit, page=None) -> dict:
    if page is not None:
        url = f"https://cloudac.mildom.com/nonolive/videocontent/profile/playbackList" \
              f"?__platform=web&user_id={user_id}&limit={limit}&page={page}"
    else:
        url = f"https://cloudac.mildom.com/nonolive/videocontent/profile/playbackList" \
              f"?__platform=web&user_id={user_id}&limit={limit}"
    response = requests.get(url).json()
    if response["code"] == 1:
        raise ConnectionRefusedError("rate limit exceeded. code: 1")
    return response


def live_info_request(user_id: int) -> dict:
    url = f"https://cloudac.mildom.com/nonolive/gappserv/live/enterstudio?__platform=web&user_id={user_id}"
    response = requests.get(url).json()
    if response["code"] == 1:
        raise ConnectionRefusedError("rate limit exceeded. code: 1")
    return response


def search_request(query: str, type_code: int = None) -> dict:
    # PlayBack同様、pageとlimitのクエリが使えるが未実装
    if type_code is None:
        url = f"https://cloudac-cf-jp.mildom.com/nonolive/gsearch/search?type=7&query={query}"
    else:
        url = f"https://cloudac-cf-jp.mildom.com/nonolive/gsearch/search?type=7&query={query}&type={type_code}"
    response = requests.get(url).json()
    if response["code"] == 1:
        raise ConnectionRefusedError("rate limit exceeded. code: 1")
    return response
