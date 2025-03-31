# 🧠 Sudoku Solver
Bienvenue dans **Sudoku Solver**, un projet Python ambitieux réalisé dans le cadre de ma formation en **Bachelor Intelligence Artificielle & Data Analytics**.

Ce projet propose une solution complète et interactive pour résoudre des grilles de Sudoku grâce à deux algorithmes puissants : la **Force Brute** et le **Backtracking**. Il comprend également une analyse approfondie des performances des deux approches, ainsi qu'une interface graphique dynamique réalisée avec **Pygame** pour visualiser les résultats de façon claire et intuitive.

## 🎯 Objectifs du projet
Implémenter et comparer deux algorithmes fondamentaux de résolution de Sudoku :

- Force brute
- Backtracking

Étudier la complexité algorithmique et mesurer précisément les temps d’exécution.

Créer une interface terminale détaillée et une interface graphique interactive (Pygame).

Documenter intégralement et clairement l'ensemble du projet.

Structurer le projet de manière professionnelle et modulaire.

## 📂 Structure détaillée du projet
```bash
sudoku-solver/
├── core/
│   ├── sudoku_grid.py       # Gestion de la grille (importation, validation, affichage)
│   └── solver.py            # Algorithmes de résolution (Force Brute et Backtracking)
├── interface/
│   └── visualizer.py        # Interface graphique interactive (Pygame)
├── utils/
│   └── tools.py             # Fonctions utilitaires (chronométrage, affichage résultats)
├── sudokus/                 # Grilles exemples de difficulté variée
│   ├── exemple1.txt
│   ├── exemple2.txt
│   ├── exemple3.txt
│   ├── exemple4.txt
│   └── exemple5.txt
├── main_terminal.py         # Exécution des résolutions via terminal
├── main_interface.py        # Lancement de l'interface graphique
├── requirements.txt         # Dépendances nécessaires au projet
├── presentation.pptx        # Présentation complète du projet
└── README.md                # Documentation intégrale du projet
```

## 🧩 Algorithmes implémentés

### 🔄 Force Brute
Principe : Parcourt toutes les combinaisons possibles jusqu'à trouver une solution valide.

Complexité : exponentielle (O(9^(n²)))

Avantages : Facile à comprendre et implémenter

Inconvénients : Temps de résolution très élevé pour les grilles complexes

### 🔍 Backtracking (Retour sur trace)
Principe : Choisit des chiffres valides récursivement, revient en arrière si nécessaire.

Complexité : beaucoup plus efficace (O(n^k) selon les cas)

Avantages : Rapide, efficace, et performant même sur les grilles difficiles

Inconvénients : Nécessite une gestion intelligente de la récursivité

## 📊 Analyse comparative détaillée
| Méthode      | Succès | Temps moyen | Complexité théorique | Avantages                  | Inconvénients             |
|--------------|--------|-------------|----------------------|----------------------------|---------------------------|
| Backtracking | ✅     | ~0.001 s    | O(n^k)               | Très rapide et efficace    | Plus complexe à implémenter |
| Force Brute  | ✅     | ~0.01 s     | O(9^81)              | Très simple à comprendre   | Très lent sur grilles difficiles |

Conclusion : Le Backtracking est significativement plus performant et recommandé pour ce type de problème.

## 🖥️ Interface terminale
Exécution via terminal, avec affichage clair des résultats :

- Différenciation visuelle entre chiffres initiaux (en gras) et chiffres générés
- Chronométrage précis des algorithmes
- Tableau comparatif des performances clairement affiché

```bash
python main_terminal.py
```

## 🎨 Interface graphique interactive (Pygame)
Une visualisation interactive, ergonomique et pédagogique du Sudoku :

- Choix parmi 5 grilles de difficulté croissante
- Animation dynamique de la résolution par Backtracking
- Chiffres initiaux clairement distingués en bleu gras
- Interface intuitive, conviviale et fluide

Exécution :

```bash
python main_interface.py
```

## 🧪 Grilles de test fournies
Le projet inclut 5 grilles test dans sudokus/ pour évaluer et démontrer les capacités des algorithmes :

- exemple1.txt – Facile
- exemple2.txt – Moyen
- exemple3.txt – Difficile
- exemple4.txt – Expert
- exemple5.txt – Quasi-vide (extrêmement complexe)

Format des fichiers grille :
```
_729___3_
__1__6_8_
____4__6_
...
```

## 🔗 Ressources et veille technologique
Quelques ressources clés explorées et utilisées dans le cadre du projet :

- [Backtracking – Wikipédia](https://en.wikipedia.org/wiki/Backtracking)
- [Brute Force Algorithms – Codecademy](https://www.codecademy.com/learn/learn-data-structures-and-algorithms-with-python/modules/brute-force-algorithms/cheatsheet)
- [Analyse de complexité – Mon Lycée Numérique](http://www.monlyceenumerique.fr/nsi_premiere/algo_a/a2_complexite.php)
- [Documentation officielle Pygame](https://www.pygame.org/wiki/GettingStarted)

## 🚀 Installation et prérequis
Cloner ce dépôt puis installer les dépendances nécessaires :

```bash
git clone https://github.com/username/sudoku-solver.git
cd sudoku-solver
pip install -r requirements.txt
```

## 🏁 Conclusion & perspectives
Ce projet m’a permis de renforcer concrètement mes compétences en :

- Algorithmique avancée
- Programmation orientée objet
- Visualisation interactive
- Gestion de projet structuré et modulaire
- Documentation technique claire

Il constitue désormais une base solide pour la réalisation future de projets plus complexes en Intelligence Artificielle, algorithmique avancée, et visualisation interactive.

Réalisé par : [Ton Nom]  
Bachelor Intelligence Artificielle & Data Analytics – 1ère année  
[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)
