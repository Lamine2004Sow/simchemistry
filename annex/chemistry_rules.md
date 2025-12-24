# Documentation - Module Chemistry Rules

## Introduction

Le module `chemistry_rules.py` contient des fonctions de validation permettant d'identifier le type de composé organique d'une molécule donnée. Ces fonctions vérifient la structure moléculaire selon les règles de la chimie organique.

## Fonctions de validation

### `is_alkane(molecule: Molecule) -> bool`

Vérifie si une molécule est un alcane.

#### Critères de validation

1. **Molécule complète** : Toutes les valences doivent être saturées (la molécule doit être complète)
2. **Composition atomique** : La molécule ne doit contenir que des atomes de carbone (C) et d'hydrogène (H)
3. **Formule générale** : Doit respecter la formule CnH2n+2 pour un alcane acyclique

#### Retourne

- `True` si la molécule est un alcane
- `False` sinon

#### Exemple

```python
from src.myClass import Atom, Molecule
from src.chemistry_rules import is_alkane

# Créer le méthane (CH4)
c = Atom("Carbon", "C", 6, 4)
h1 = Atom("Hydrogen", "H", 1, 1)
h2 = Atom("Hydrogen", "H", 1, 1)
h3 = Atom("Hydrogen", "H", 1, 1)
h4 = Atom("Hydrogen", "H", 1, 1)

methane = Molecule("Methane", [c, h1, h2, h3, h4], 
                   [(c, h1), (c, h2), (c, h3), (c, h4)])

print(is_alkane(methane))  # True
```

---

### `is_alkene(molecule: Molecule) -> bool`

Vérifie si une molécule est un alcène.

#### Critères de validation

1. **Molécule complète** : Toutes les valences doivent être saturées
2. **Composition atomique** : La molécule ne doit contenir que des atomes de carbone (C) et d'hydrogène (H)
3. **Formule générale** : Doit respecter la formule CnH2n pour un alcène acyclique

#### Retourne

- `True` si la molécule est un alcène
- `False` sinon

#### Exemple

```python
from src.chemistry_rules import is_alkene

# Créer l'éthylène (C2H4)
# ... (construction de la molécule avec double liaison)

print(is_alkene(ethylene))  # True
```

---

### `is_alkyne(molecule: Molecule) -> bool`

Vérifie si une molécule est un alcyne.

#### Critères de validation

1. **Molécule complète** : Toutes les valences doivent être saturées
2. **Composition atomique** : La molécule ne doit contenir que des atomes de carbone (C) et d'hydrogène (H)
3. **Formule générale** : Doit respecter la formule CnH2n-2 pour un alcyne acyclique

#### Retourne

- `True` si la molécule est un alcyne
- `False` sinon

#### Exemple

```python
from src.chemistry_rules import is_alkyne

# Créer l'acétylène (C2H2)
# ... (construction de la molécule avec triple liaison)

print(is_alkyne(acetylene))  # True
```

---

### `is_alcohol(molecule: Molecule) -> bool`

Vérifie si une molécule est un alcool.

#### Critères de validation

1. **Molécule complète** : Toutes les valences doivent être saturées
2. **Composition atomique** : La molécule doit contenir exactement un atome d'oxygène (O), et le reste doit être uniquement des atomes de carbone (C) et d'hydrogène (H)
3. **Structure du groupe -OH** : L'atome d'oxygène doit avoir exactement deux voisins :
   - Un atome de carbone (C)
   - Un atome d'hydrogène (H)

#### Retourne

- `True` si la molécule est un alcool
- `False` sinon

#### Exemple

```python
from src.chemistry_rules import is_alcohol

# Créer le méthanol (CH3OH)
c = Atom("Carbon", "C", 6, 4)
h1 = Atom("Hydrogen", "H", 1, 1)
h2 = Atom("Hydrogen", "H", 1, 1)
h3 = Atom("Hydrogen", "H", 1, 1)
o = Atom("Oxygen", "O", 8, 2)
h_oh = Atom("Hydrogen", "H", 1, 1)

methanol = Molecule("Methanol", [c, h1, h2, h3, o, h_oh],
                    [(c, h1), (c, h2), (c, h3), (c, o), (o, h_oh)])

print(is_alcohol(methanol))  # True
```

---

## Notes importantes

### Limitations actuelles

- Les fonctions vérifient uniquement les formules générales pour les composés acycliques
- La détection des doubles et triples liaisons n'est pas encore implémentée dans la structure de `Molecule`
- Les fonctions supposent que les molécules sont complètes (toutes valences saturées)

### Prochaines améliorations

- [ ] Implémentation de la détection des doubles liaisons
- [ ] Implémentation de la détection des triples liaisons
- [ ] Support des composés cycliques
- [ ] Validation des éthers, amines, cétones, etc.
- [ ] Détection des groupes fonctionnels spécifiques

### Utilisation avec les classes de composés

Ces fonctions de validation peuvent être utilisées pour vérifier si une instance de `Molecule` correspond à un type de composé organique spécifique, avant de créer une instance de la classe correspondante (par exemple, `Alkane`, `Alkene`, etc.).

## Tests

Des tests unitaires sont disponibles dans `test/test_chemistryRules.py` pour valider le comportement de ces fonctions.

