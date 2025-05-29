# 🛸 FlashInvaders Comparator

Comparer automatiquement les invaders capturés par plusieurs joueurs FlashInvaders à partir de leurs UIDs, et afficher les résultats dans un Google Sheet.

---

## ✅ Fonctionnalités

- 📥 Lire les **UIDs de joueurs** depuis un onglet d'un Google Sheet
- 🔄 Récupérer automatiquement les invaders via l'API FlashInvaders
- 📊 Générer un **tableau comparatif** (invaders x joueurs) dans Google Sheets
- ☁️ Automatiser l'exécution depuis n'importe quelle machine
- 📁 Utiliser une structure de projet propre pour GitHub

---

## 🗂 Structure du projet

```text
flashinvaders-comparator/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── flashinvaders.py
├── google_sheets.py
├── credentials/
│   └── credentials.json
```

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/flashinvaders-comparator.git
cd flashinvaders-comparator
```

### 2. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration de l'accès Google Sheets

### 1. Créer un projet sur Google Cloud Console

1. Aller sur https://console.cloud.google.com/
2. Créer un nouveau projet
3. Activer les APIs suivantes :
   - ✅ **Google Sheets API**
   - ✅ **Google Drive API**

### 2. Créer une clé de service

1. Dans **Identifiants**, cliquer sur **Créer un identifiant** > **Compte de service**
2. Générer une clé JSON
3. Renommer le fichier en `credentials.json` et le placer dans le dossier `credentials/`

### 3. Partager le Google Sheet

1. Ouvrir le Google Sheet à utiliser
2. Cliquer sur **Partager**
3. Inviter l'adresse e-mail du compte de service (visible dans `credentials.json` sous `client_email`)

---

## 📝 Préparation du Google Sheet

### Configuration requise

- **Nom du Google Sheet :** `FlashInvaders Tracker`
- **Créer deux onglets :**

#### Onglet "UIDs"

| UID |
|-----|
| FAFDC163-BD97-4372-A647-1A063028E579 |
| 627F176F-54C3-4D32-90EF-C4C80462A2C3 |

- **Ligne 1 :** Titre `UID`
- **À partir de la ligne 2 :** Ajouter les UIDs à comparer

#### Onglet "Comparatif"

Ne rien faire, le script remplira automatiquement cet onglet (ou le créera s'il n'existe pas).

---

## 🚀 Exécution

### Lancer le script

```bash
python main.py
```

### Processus automatique

Le script effectue les actions suivantes :

1. Récupérer les invaders de chaque UID
2. Créer un tableau croisé avec les invaders en lignes et les joueurs en colonnes
3. Marquer ✔️ si un joueur a flashé l'invader, ❌ sinon
4. Écrire le tableau dans l'onglet "Comparatif"

---