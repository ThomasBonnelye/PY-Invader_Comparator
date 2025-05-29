import requests

BASE_URL = "https://api.space-invaders.com/flashinvaders_v3_pas_trop_predictif/api/gallery?uid="

def fetch_player_data(uid):
    url = f"{BASE_URL}{uid}"
    data = requests.get(url).json()
    player = data.get("player", {}).get("name", uid)
    invaders = data.get("invaders", {})
    invader_names = set(inv["name"] for inv in invaders.values())
    return player, invader_names
