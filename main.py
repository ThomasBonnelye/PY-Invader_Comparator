import pandas as pd
from flashinvaders import fetch_player_data
from google_sheets import read_uids, write_comparatif

def main():
    uids = read_uids()
    all_invaders = set()
    player_invaders = {}

    for uid in uids:
        name, invaders = fetch_player_data(uid)
        player_invaders[name] = invaders
        all_invaders.update(invaders)

    # Construire le DataFrame croisé
    invader_list = sorted(all_invaders)
    df = pd.DataFrame(index=invader_list)

    for player, invaders in player_invaders.items():
        df[player] = df.index.map(lambda x: "✔️" if x in invaders else "❌")

    write_comparatif(df)

if __name__ == "__main__":
    main()
