# DOOM Style 3D Game - Raycasting Engine

Un jeu de tir à la première personne en style DOOM construit avec **raycasting** en Python, inspiré par Wolfenstein 3D.

## ?? Caractèristiques

- **Moteur Raycasting** : Rendu 3D temps réel basé sur la géométrie
- **Carte 100x100** : Monde explorable entièrement généré
- **Système de Combat** : Arme à feu avec rechargement
- **IA Ennemis** : 30+ ennemis avec pathfinding et détection du joueur
  - **Soldat** : Ennemi standard rapide
  - **Caco-Démon** : Ennemi puissant et agressif
  - **Cyber-Démon** : Boss ultime
- **Système de Santé** : Barre de vie, dégàts, régénération
- **Menu Principal** : Interface pour démarrer ou quitter
- **Son & Musique** : Effets sonores et musique de fond

## ??? Contr�les

### Mouvement
- **Z / W / ?** : Avancer
- **S / ?** : Reculer
- **Q / A / ?** : Se tourner à gauche
- **D / ?** : Se tourner à droite

### Combat & Interface
- **Clic Gauche** : Tirer
- **Echap** : Retour au menu
- **Souris** : Tourner la vue (gauche/droite)

## ?? Installation

### Pr�requis
- Python 3.10+
- Pygame

### Installation des d�pendances
```bash
pip install -r requirements.txt
```

## ?? Lancement du Jeu

```bash
python main.py
```

Le jeu démarre avec le menu principal.

## ??? Structure du Projet

```
+-- main.py              # Point d'entrée principal
+-- menu.py              # Menu principal
+-- map.py               # Génération et gestion de la carte
+-- player.py            # Classe joueur et mouvements
+-- raycasting.py        # Moteur de rendu raycasting
+-- npc.py               # Système d'IA des ennemis
+-- object_handler.py    # Gestion des sprites et NPCs
+-- weapon.py            # Système de combat
+-- pathfinding.py       # Algorithme A* pour l'IA
+-- object_renderer.py   # Rendu des objets et HUD
+-- sprite_object.py     # Sprites animés
+-- sound.py             # Gestion du son
+-- settings.py          # Configuration globale
+-- resources/           # Assets (textures, sprites, sons)
    +-- textures/        # Textures murales et HUD
    +-- sprites/         # Sprites des ennemis et objets
    +-- sound/           # Effets sonores et musique
```

## ?? Configuration

Modifier `settings.py` pour ajuster :
- **RES** : Résolution
- **FULLSCREEN** : Mode plein écran
- **FPS** : Images par seconde
- **PLAYER_MAX_HEALTH** : Santé maximale du joueur
- **MAX_DEPTH** : Distance de rendu

## ?? Personnalisation

### Changer les Textures
Remplace les fichiers PNG dans `resources/textures/` :
- `1.png` à `5.png` : Textures murales
- `sky.png` : Ciel
- `blood_screen.png` : Effet dégat

### Modifier la Carte
La carte est générée aléatoirement chaque partie dans `map.py`. Tu peux :
- Augmenter la densité des murs en modifiant le pourcentage dans `generate_static_map()`
- Changer les dimensions en modifiant `MAP_SIZE`

## ?? M�canique de Jeu

### Sant� du Joueur
- Santé max : 100 points
- Régénération : +1 HP toutes les 0.7 secondes (si hors combat)
- Les ennemis infligent 10-25 dégats par coup

### Syst�me d'IA
- **D�tection** : Les NPCs te détectent visuellement via raycasting
- **Pathfinding** : Recherche de chemin BFS pour approcher le joueur
- **Distance d'attaque** : Varie selon le type d'ennemi (3-6 unités)

## ?? Objectif

Survive et élimine tous les ennemis. Le message "YOU WIN" apparait quand tous les NPCs sont morts.

## ?? Licence

Libre d'utilisation et de modification.

## ????? Développement

Built with Python + Pygame. Techniques inspirées des jeux classiques de raycasting.

---

**Bon jeu ! ??**
