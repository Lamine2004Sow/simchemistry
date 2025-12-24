# Documentation - Module Formula

## Introduction

Le module `formula.py` contient les classes fondamentales pour représenter et manipuler des structures atomiques et moléculaires dans le cadre de simulations chimiques.

## Classes

### Classe `Atom`

La classe `Atom` représente un atome avec ses propriétés essentielles.

#### Attributs

- `name` (str) : Nom complet de l'atome (ex: "Hydrogen", "Carbon")
- `symbol` (str) : Symbole chimique (ex: "H", "C")
- `atomic_number` (int) : Numéro atomique
- `valence` (int) : Valence de l'atome (nombre de liaisons possibles)

#### Méthodes

##### `__init__(self, name, symbol, atomic_number, valence)`
Constructeur de la classe Atom.

**Paramètres :**
- `name` : Nom de l'atome
- `symbol` : Symbole chimique
- `atomic_number` : Numéro atomique
- `valence` : Valence de l'atome

##### `get_name(self) -> str`
Retourne le nom de l'atome.

##### `get_symbol(self) -> str`
Retourne le symbole chimique de l'atome.

##### `get_atomic_number(self) -> int`
Retourne le numéro atomique.

##### `get_valence(self) -> int`
Retourne la valence de l'atome.

##### `__str__(self) -> str`
Représentation sous forme de chaîne de caractères.
Format : `"{name} ({symbol}) {atomic_number} {valence}"`

#### Exemple d'utilisation

```python
from src.formula import Atom

# Créer un atome de carbone
carbon = Atom("Carbon", "C", 6, 4)
print(carbon)  # Affiche: Carbon (C) 6 4
print(carbon.get_symbol())  # Affiche: C
```

---

### Classe `Molecule`

La classe `Molecule` représente une molécule composée d'atomes et de leurs connexions (liaisons).

#### Attributs

- `name` (str) : Nom de la molécule
- `atoms` (list) : Liste des atomes constituant la molécule
- `connections` (list) : Liste des connexions entre atomes (paires d'atomes)

#### Méthodes

##### `__init__(self, name, atoms, connections)`
Constructeur de la classe Molecule.

**Paramètres :**
- `name` : Nom de la molécule
- `atoms` : Liste des atomes
- `connections` : Liste des connexions (chaque connexion est une paire d'atomes)

##### `check_validity(self) -> bool`
Vérifie si la molécule est valide en s'assurant que chaque atome respecte sa valence.
Retourne `True` si la molécule est valide, `False` sinon.

##### `get_atoms(self) -> list`
Retourne la liste des atomes de la molécule.

##### `get_connections(self) -> list`
Retourne la liste des connexions entre atomes.

##### `get_name(self) -> str`
Retourne le nom de la molécule.

##### `get_valence_restant(self, atom) -> int`
Calcule la valence restante d'un atome donné (valence totale - nombre de liaisons).

**Paramètres :**
- `atom` : L'atome dont on veut connaître la valence restante

**Retourne :**
- La valence restante de l'atome

##### `__str__(self) -> str`
Représentation sous forme de chaîne de caractères.
Format : `"{name} ({atoms}) {connections}"`

#### Exemple d'utilisation

```python
from src.formula import Atom, Molecule

# Créer des atomes
h1 = Atom("Hydrogen", "H", 1, 1)
h2 = Atom("Hydrogen", "H", 1, 1)
c = Atom("Carbon", "C", 6, 4)

# Créer une molécule de méthane (CH4)
methane = Molecule(
    name="Methane",
    atoms=[c, h1, h2, Atom("Hydrogen", "H", 1, 1), Atom("Hydrogen", "H", 1, 1)],
    connections=[(c, h1), (c, h2), (c, h1), (c, h2)]  # Exemple simplifié
)

# Vérifier la validité
is_valid = methane.check_validity()
print(f"La molécule est valide : {is_valid}")
```

## Notes importantes

- La méthode `check_validity()` vérifie que le nombre de connexions pour chaque atome correspond à sa valence
- Les connexions sont représentées comme des paires d'atomes dans une liste
- La validation moléculaire est essentielle pour s'assurer que les structures sont chimiquement cohérentes

