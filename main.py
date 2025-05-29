import json
import requests
import pandas as pd

# Fonction pour récupérer le nom du joueur et les noms des invaders
def get_player_and_invader_names(url):
    data = requests.get(url).json()
    player_name = data.get("player", {}).get("name", "Unknown")
    invaders = data.get("invaders", {})
    invader_names = set(info["name"] for info in invaders.values())
    return player_name, invader_names

# URLs à comparer
url1 = "https://api.space-invaders.com/flashinvaders_v3_pas_trop_predictif/api/gallery?uid=FAFDC163-BD97-4372-A647-1A063028E579"
url2 = "https://api.space-invaders.com/flashinvaders_v3_pas_trop_predictif/api/gallery?uid=627F176F-54C3-4D32-90EF-C4C80462A2C3"

# Extraction des noms de joueurs et noms d'invaders
player1, names1 = get_player_and_invader_names(url1)
player2, names2 = get_player_and_invader_names(url2)

# Détection des invaders exclusifs à chaque joueur
only_in_1 = sorted(names1 - names2)
only_in_2 = sorted(names2 - names1)

# Création du tableau
max_len = max(len(only_in_1), len(only_in_2))
df = pd.DataFrame({
    f"{player1}": only_in_1 + [''] * (max_len - len(only_in_1)),
    f"{player2}": only_in_2 + [''] * (max_len - len(only_in_2))
})

# Affichage du tableau
print(df.to_string(index=False))

# Export optionnel
df.to_csv("comparatif_invader_names.csv", index=False)
