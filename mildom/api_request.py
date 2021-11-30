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
    return response


def live_info_request(user_id: int) -> dict:
    url = f"https://cloudac.mildom.com/nonolive/gappserv/live/enterstudio?__platform=web&user_id={user_id}"
    response = requests.get(url).json()
    return response
