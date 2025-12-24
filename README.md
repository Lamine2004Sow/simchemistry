# SimChemistry

Un projet passionnant qui combine la chimie computationnelle et l'apprentissage par renforcement (Reinforcement Learning - RL).

## Description

SimChemistry est un projet de simulation et modélisation moléculaire qui permet de :
- Représenter des structures atomiques et moléculaires
- Valider la cohérence chimique des molécules
- Identifier automatiquement le type de composé organique
- Simuler des réactions chimiques (en développement)

## Installation

```bash
# Cloner le projet
git clone <repository-url>
cd simchemistry

# Installer les dépendances (si nécessaire)
pip install pytest  # Pour les tests
```

## Structure du projet

```
simchemistry/
├── src/
│   ├── myClass.py          # Classes Atom et Molecule
│   ├── formula.py          # Hiérarchie des composés organiques
│   └── chemistry_rules.py  # Fonctions de validation
├── annex/
│   ├── general.md          # Documentation générale
│   ├── MyClass.md          # Documentation des classes
│   └── chemistry_rules.md  # Documentation des règles de validation
├── test/                   # Tests unitaires
│   ├── test_myClass.py
│   └── test_chemistryRules.py
└── README.md
```

## Utilisation rapide

### Créer un atome

```python
from src.myClass import Atom

# Créer un atome de carbone
carbon = Atom("Carbon", "C", 6, 4)
print(carbon)  # Carbon (C) 6 4
```

### Créer une molécule

```python
from src.myClass import Atom, Molecule

# Créer le méthane (CH4)
c = Atom("Carbon", "C", 6, 4)
h1 = Atom("Hydrogen", "H", 1, 1)
h2 = Atom("Hydrogen", "H", 1, 1)
h3 = Atom("Hydrogen", "H", 1, 1)
h4 = Atom("Hydrogen", "H", 1, 1)

methane = Molecule("Methane")
methane.add_atom(c)
methane.add_atom(h1)
methane.add_atom(h2)
methane.add_atom(h3)
methane.add_atom(h4)

methane.add_connection(c, h1)
methane.add_connection(c, h2)
methane.add_connection(c, h3)
methane.add_connection(c, h4)

# Vérifier la validité
print(methane.check_validity())  # True
print(methane.is_complete())     # True
```

### Valider le type de composé

```python
from src.chemistry_rules import is_alkane

# Vérifier si la molécule est un alcane
print(is_alkane(methane))  # True
```

## Fonctionnalités

### Implémenté

- Classes `Atom` et `Molecule` avec validation
- Gestion des connexions entre atomes
- Validation de la cohérence des valences
- Identification des alcanes, alcènes, alcynes et alcools
- Tests unitaires

### En développement

- Implémentation complète des classes de composés organiques
- Détection des doubles et triples liaisons
- Support des composés cycliques
- Simulation de réactions chimiques
- Intégration de l'apprentissage par renforcement

## Tests

Exécuter les tests unitaires :

```bash
pytest test/
```

## Documentation

Consultez les fichiers dans le dossier `annex/` pour une documentation détaillée :
- `general.md` : Vue d'ensemble du projet
- `MyClass.md` : Documentation des classes Atom, Molecule et composés organiques
- `chemistry_rules.md` : Documentation des fonctions de validation

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## Licence


