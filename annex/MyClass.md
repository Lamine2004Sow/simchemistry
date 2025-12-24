# Documentation - Module MyClass

## Introduction

Le module `myClass.py` contient les classes fondamentales pour représenter et manipuler des structures atomiques et moléculaires, ainsi que la hiérarchie des classes de composés organiques.

## Classes fondamentales

### Classe `Atom`

La classe `Atom` représente un atome avec ses propriétés essentielles.

#### Attributs

- `name` (str) : Nom complet de l'atome (ex: "Hydrogen", "Carbon")
- `symbol` (str) : Symbole chimique (ex: "H", "C")
- `atomic_number` (int) : Numéro atomique (doit être positif)
- `valence` (int) : Valence de l'atome - nombre de liaisons possibles (ne peut pas être négative)

#### Méthodes

##### `__init__(self, name, symbol, atomic_number, valence)`
Constructeur de la classe Atom avec validation.

**Paramètres :**
- `name` : Nom de l'atome
- `symbol` : Symbole chimique
- `atomic_number` : Numéro atomique (doit être > 0)
- `valence` : Valence de l'atome (doit être >= 0)

**Lève :**
- `ValueError` : Si le numéro atomique est <= 0 ou si la valence est négative

##### `__str__(self) -> str`
Représentation sous forme de chaîne de caractères.
Format : `"{name} ({symbol}) {atomic_number} {valence}"`

#### Exemple d'utilisation

```python
from src.myClass import Atom

# Créer un atome de carbone
carbon = Atom("Carbon", "C", 6, 4)
print(carbon)  # Affiche: Carbon (C) 6 4

# Créer un atome d'hydrogène
hydrogen = Atom("Hydrogen", "H", 1, 1)
```

---

### Classe `Molecule`

La classe `Molecule` représente une molécule composée d'atomes et de leurs connexions (liaisons).

#### Attributs

- `name` (str) : Nom de la molécule
- `atoms` (list) : Liste des atomes constituant la molécule
- `connections` (list) : Liste des connexions entre atomes (paires d'atomes normalisées)

#### Méthodes principales

##### `__init__(self, name, atoms=None, connections=None)`
Constructeur de la classe Molecule.

**Paramètres :**
- `name` : Nom de la molécule
- `atoms` : Liste optionnelle des atomes (par défaut : liste vide)
- `connections` : Liste optionnelle des connexions (par défaut : liste vide)

##### `add_atom(self, atom)`
Ajoute un atome à la molécule.

**Paramètres :**
- `atom` : L'atome à ajouter

**Lève :**
- `ValueError` : Si l'atome est déjà présent dans la molécule

##### `add_connection(self, atom1, atom2)`
Ajoute une connexion (liaison) entre deux atomes.

**Paramètres :**
- `atom1`, `atom2` : Les deux atomes à connecter

**Lève :**
- `ValueError` : Si les atomes sont identiques, s'ils n'appartiennent pas à la molécule, si la liaison existe déjà, ou si l'ajout dépasse la valence d'un atome

##### `delete_connection(self, atom1, atom2)`
Supprime une connexion entre deux atomes.

**Paramètres :**
- `atom1`, `atom2` : Les deux atomes dont la connexion doit être supprimée

**Lève :**
- `ValueError` : Si la liaison n'existe pas

##### `delete_atom(self, atom)`
Supprime un atome de la molécule et toutes ses connexions.

**Paramètres :**
- `atom` : L'atome à supprimer

**Lève :**
- `ValueError` : Si l'atome n'existe pas dans la molécule

##### `check_validity(self) -> bool`
Vérifie si la molécule est valide en s'assurant qu'aucun atome ne dépasse sa valence.
Retourne `True` si la molécule est valide, `False` sinon.

##### `get_valence_restant(self, atom) -> int`
Calcule la valence restante d'un atome donné (valence totale - nombre de liaisons).

**Paramètres :**
- `atom` : L'atome dont on veut connaître la valence restante

**Retourne :**
- La valence restante de l'atome

**Lève :**
- `ValueError` : Si l'atome n'appartient pas à la molécule

##### `get_atoms_with_free_valence(self) -> list`
Retourne la liste des atomes ayant encore une valence disponible.

**Retourne :**
- Liste des atomes avec valence restante > 0

##### `get_possible_connections(self) -> list`
Retourne la liste de toutes les connexions possibles entre atomes ayant une valence disponible.

**Retourne :**
- Liste de tuples (atom1, atom2) représentant les connexions possibles

##### `is_complete(self) -> bool`
Vérifie si la molécule est complète (toutes les valences sont saturées).

**Retourne :**
- `True` si toutes les valences sont utilisées, `False` sinon

##### `_neighbors(self, atom) -> list`
Méthode privée qui retourne la liste des voisins d'un atome.

**Paramètres :**
- `atom` : L'atome dont on veut connaître les voisins

**Retourne :**
- Liste des atomes connectés à l'atome donné

##### `_normalize(self, atom1, atom2) -> tuple`
Méthode privée qui normalise une paire d'atomes pour représenter une connexion non orientée.

**Paramètres :**
- `atom1`, `atom2` : Les deux atomes

**Retourne :**
- Tuple normalisé (trié par id)

**Lève :**
- `ValueError` : Si les atomes sont identiques ou n'appartiennent pas à la molécule

##### `__str__(self) -> str`
Représentation sous forme de chaîne de caractères.
Format : `"{name} (atoms={atoms}) connections={connections}"`

#### Exemple d'utilisation

```python
from src.myClass import Atom, Molecule

# Créer des atomes
c = Atom("Carbon", "C", 6, 4)
h1 = Atom("Hydrogen", "H", 1, 1)
h2 = Atom("Hydrogen", "H", 1, 1)
h3 = Atom("Hydrogen", "H", 1, 1)
h4 = Atom("Hydrogen", "H", 1, 1)

# Créer une molécule de méthane
methane = Molecule("Methane")
methane.add_atom(c)
methane.add_atom(h1)
methane.add_atom(h2)
methane.add_atom(h3)
methane.add_atom(h4)

# Ajouter les connexions
methane.add_connection(c, h1)
methane.add_connection(c, h2)
methane.add_connection(c, h3)
methane.add_connection(c, h4)

# Vérifier la validité et la complétude
print(f"Valide : {methane.check_validity()}")  # True
print(f"Complète : {methane.is_complete()}")   # True
```

---

## Hiérarchie des composés organiques

Le module `formula.py` définit une hiérarchie de classes représentant différents types de composés organiques. Actuellement, toutes ces classes sont des stubs (classes vides) héritant de `Hydrocabon`.

### Classe de base : `Hydrocabon`

Classe parente pour tous les composés organiques. Actuellement vide, sert de point de départ pour la hiérarchie d'héritage.

**Note :** Il y a une faute de frappe dans le nom de la classe (`Hydrocabon` au lieu de `Hydrocarbon`).

### Hydrocarbures

#### `Alkane`
Représente les alcanes, hydrocarbures saturés avec uniquement des liaisons simples C-C.
- Formule générale : CₙH₂ₙ₊₂
- Exemples : Méthane (CH₄), Éthane (C₂H₆), Propane (C₃H₈)

#### `Alkene`
Représente les alcènes, hydrocarbures insaturés avec au moins une double liaison C=C.
- Formule générale : CₙH₂ₙ
- Exemples : Éthylène (C₂H₄), Propène (C₃H₆)

#### `Alkyne`
Représente les alcynes, hydrocarbures insaturés avec au moins une triple liaison C≡C.
- Formule générale : CₙH₂ₙ₋₂
- Exemples : Acétylène (C₂H₂), Propyne (C₃H₄)

#### `Aromatic`
Représente les composés aromatiques, caractérisés par des cycles avec des liaisons conjuguées.
- Exemples : Benzène (C₆H₆), Toluène (C₇H₈)

### Composés oxygénés

#### `Alcohol`
Représente les alcools, composés contenant un groupe fonctionnel -OH.
- Groupe fonctionnel : R-OH
- Exemples : Méthanol (CH₃OH), Éthanol (C₂H₅OH)

#### `Ether`
Représente les éthers, composés avec un atome d'oxygène lié à deux groupes alkyle.
- Groupe fonctionnel : R-O-R'
- Exemples : Éther diéthylique (C₄H₁₀O)

#### `Phenol`
Représente les phénols, composés aromatiques avec un groupe -OH directement lié au cycle.
- Groupe fonctionnel : Ar-OH
- Exemples : Phénol (C₆H₅OH)

### Composés azotés

#### `Amine`
Représente les amines, composés contenant un groupe fonctionnel -NH₂, -NHR, ou -NR₂.
- Groupe fonctionnel : R-NH₂, R-NHR', ou R-NR'R''
- Exemples : Méthylamine (CH₃NH₂)

#### `Amide`
Représente les amides, composés avec un groupe fonctionnel -CONH₂.
- Groupe fonctionnel : R-CONH₂
- Exemples : Acétamide (CH₃CONH₂)

#### `Cetone`
Représente les cétones, composés avec un groupe carbonyle C=O.
- Groupe fonctionnel : R-COR'
- Exemples : Acétone (CH₃COCH₃)

**Note :** Il y a une faute de frappe dans le nom de la classe (`Cetone` au lieu de `Ketone`).

### Acides carboxyliques

#### `CarboxylicAcid`
Représente les acides carboxyliques, composés avec un groupe fonctionnel -COOH.
- Groupe fonctionnel : R-COOH
- Exemples : Acide acétique (CH₃COOH), Acide formique (HCOOH)

#### `CarboxylicAcidDerivative`
Représente les dérivés d'acides carboxyliques (esters, anhydrides, halogénures d'acyle, etc.).
- Dérivés du groupe -COOH
- Exemples : Esters, Anhydrides, Amides

## Notes importantes

- Les classes de composés organiques sont actuellement des stubs et nécessitent une implémentation complète
- La validation des types de composés est effectuée par les fonctions du module `chemistry_rules.py`
- Toutes les classes héritent de `Hydrocabon`, ce qui peut ne pas être sémantiquement correct pour tous les composés
- Une refactorisation future pourrait introduire des classes intermédiaires plus appropriées
