# Documentation Générale - SimChemistry

## Vue d'ensemble

**SimChemistry** est un projet passionnant qui combine la chimie computationnelle et l'apprentissage par renforcement (Reinforcement Learning - RL).

## Objectifs du projet

Ce projet vise à :
- Modéliser des structures moléculaires et des composés organiques
- Implémenter des simulations de réactions chimiques
- Valider la structure et le type de molécules selon les règles de la chimie organique
- Utiliser l'apprentissage par renforcement pour optimiser les processus chimiques

## Architecture du projet

Le projet est organisé en plusieurs modules :

### Modules principaux

- **`myClass.py`** : Contient les classes fondamentales pour représenter les atomes et les molécules
  - `Atom` : Représente un atome avec ses propriétés de base (nom, symbole, numéro atomique, valence)
  - `Molecule` : Représente une molécule composée d'atomes et de leurs connexions, avec validation de la structure

- **`formula.py`** : Contient la hiérarchie des classes de composés organiques
  - Hydrocarbures (Alcanes, Alcènes, Alcynes, Aromatiques)
  - Composés oxygénés (Alcools, Éthers, Phénols)
  - Composés azotés (Amines, Amides, Cétones)
  - Acides carboxyliques et leurs dérivés

- **`chemistry_rules.py`** : Contient les fonctions de validation pour identifier le type de composé organique
  - `is_alkane()` : Vérifie si une molécule est un alcane
  - `is_alkene()` : Vérifie si une molécule est un alcène
  - `is_alkyne()` : Vérifie si une molécule est un alcyne
  - `is_alcohol()` : Vérifie si une molécule est un alcool

## Structure du projet

```
simchemistry/
├── src/
│   ├── myClass.py          # Classes Atom et Molecule
│   ├── formula.py          # Hiérarchie des composés organiques
│   └── chemistry_rules.py  # Fonctions de validation des types de composés
├── annex/
│   ├── general.md          # Documentation générale (ce fichier)
│   ├── MyClass.md          # Documentation des classes Atom, Molecule et composés organiques
│   └── chemistry_rules.md  # Documentation des règles de validation
├── test/                   # Tests unitaires
│   ├── test_myClass.py     # Tests pour Atom et Molecule
│   └── test_chemistryRules.py  # Tests pour les fonctions de validation
└── README.md               # Fichier principal du projet
```

## Fonctionnalités principales

### Gestion des atomes et molécules

- Création et manipulation d'atomes avec validation des propriétés
- Construction de molécules avec gestion des connexions entre atomes
- Validation automatique de la cohérence des valences
- Vérification de la complétude d'une molécule (toutes valences saturées)
- Calcul des valences restantes et des connexions possibles

### Validation des types de composés

- Identification automatique des alcanes (formule CnH2n+2)
- Identification des alcènes (formule CnH2n)
- Identification des alcynes (formule CnH2n-2)
- Identification des alcools (présence d'un groupe -OH)

## Prochaines étapes

- [x] Implémentation des classes Atom et Molecule
- [x] Développement des algorithmes de validation moléculaire
- [x] Création des fonctions de validation pour les types de composés
- [ ] Implémentation complète des classes de composés organiques
- [ ] Ajout de plus de règles de validation (éthers, amines, etc.)
- [ ] Intégration de l'apprentissage par renforcement
- [ ] Extension des tests unitaires
