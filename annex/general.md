# Documentation Générale - SimChemistry

## Vue d'ensemble

**SimChemistry** est un projet passionnant qui combine la chimie computationnelle et l'apprentissage par renforcement (Reinforcement Learning - RL).

## Objectifs du projet

Ce projet vise à :
- Modéliser des structures moléculaires et des composés organiques
- Implémenter des simulations de réactions chimiques
- Utiliser l'apprentissage par renforcement pour optimiser les processus chimiques

## Architecture du projet

Le projet est organisé en plusieurs modules :

### Modules principaux

- **`formula.py`** : Contient les classes fondamentales pour représenter les atomes et les molécules
  - `Atom` : Représente un atome avec ses propriétés de base
  - `Molecule` : Représente une molécule composée d'atomes et de leurs connexions

- **`myClass.py`** : Contient la hiérarchie des classes de composés organiques
  - Hydrocarbures (Alcanes, Alcènes, Alcynes, Aromatiques)
  - Composés oxygénés (Alcools, Éthers, Phénols)
  - Composés azotés (Amines, Amides, Cétones)
  - Acides carboxyliques et leurs dérivés

## Structure du projet

```
simchemistry/
├── src/
│   ├── formula.py      # Classes Atom et Molecule
│   └── myClass.py      # Hiérarchie des composés organiques
├── annex/
│   ├── general.md      # Documentation générale
│   ├── formula.md      # Documentation des formules
│   └── MyClass.md      # Documentation des classes
├── test/               # Tests unitaires
└── README.md           # Fichier principal du projet
```

## Prochaines étapes

- [ ] Implémentation complète des classes de composés organiques
- [ ] Développement des algorithmes de validation moléculaire
- [ ] Intégration de l'apprentissage par renforcement
- [ ] Création de tests unitaires complets

