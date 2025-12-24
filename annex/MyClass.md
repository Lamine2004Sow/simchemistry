# Documentation - Module MyClass

## Introduction

Le module `myClass.py` définit une hiérarchie de classes représentant différents types de composés organiques. Cette structure permet de modéliser et de catégoriser les molécules organiques selon leurs groupes fonctionnels.

## Hiérarchie des classes

```
Hydrocabon (classe de base)
├── Alkane
├── Alkene
├── Alkyne
├── Aromatic
├── Alcohol
├── Ether
├── Phenol
├── Amine
├── Amide
├── Cetone
├── CarboxylicAcid
└── CarboxylicAcidDerivative
```

## Classes

### Classe de base : `Hydrocabon`

Classe parente pour tous les composés organiques. Actuellement, cette classe est vide et sert de point de départ pour la hiérarchie d'héritage.

**Note :** Il y a une faute de frappe dans le nom de la classe (`Hydrocabon` au lieu de `Hydrocarbon`). Cette faute est présente dans le code source.

---

### Hydrocarbures

#### `Alkane`
Représente les alcanes, hydrocarbures saturés avec uniquement des liaisons simples C-C.

**Caractéristiques :**
- Formule générale : CₙH₂ₙ₊₂
- Liaisons : uniquement des liaisons simples
- Exemples : Méthane (CH₄), Éthane (C₂H₆), Propane (C₃H₈)

#### `Alkene`
Représente les alcènes, hydrocarbures insaturés avec au moins une double liaison C=C.

**Caractéristiques :**
- Formule générale : CₙH₂ₙ
- Contient au moins une double liaison
- Exemples : Éthylène (C₂H₄), Propène (C₃H₆)

#### `Alkyne`
Représente les alcynes, hydrocarbures insaturés avec au moins une triple liaison C≡C.

**Caractéristiques :**
- Formule générale : CₙH₂ₙ₋₂
- Contient au moins une triple liaison
- Exemples : Acétylène (C₂H₂), Propyne (C₃H₄)

#### `Aromatic`
Représente les composés aromatiques, caractérisés par des cycles avec des liaisons conjuguées.

**Caractéristiques :**
- Structure cyclique avec délocalisation électronique
- Exemples : Benzène (C₆H₆), Toluène (C₇H₈)

---

### Composés oxygénés

#### `Alcohol`
Représente les alcools, composés contenant un groupe fonctionnel -OH.

**Caractéristiques :**
- Groupe fonctionnel : R-OH
- Exemples : Méthanol (CH₃OH), Éthanol (C₂H₅OH)

#### `Ether`
Représente les éthers, composés avec un atome d'oxygène lié à deux groupes alkyle.

**Caractéristiques :**
- Groupe fonctionnel : R-O-R'
- Exemples : Éther diéthylique (C₄H₁₀O)

#### `Phenol`
Représente les phénols, composés aromatiques avec un groupe -OH directement lié au cycle.

**Caractéristiques :**
- Groupe fonctionnel : Ar-OH (où Ar est un groupe aromatique)
- Exemples : Phénol (C₆H₅OH)

---

### Composés azotés

#### `Amine`
Représente les amines, composés contenant un groupe fonctionnel -NH₂, -NHR, ou -NR₂.

**Caractéristiques :**
- Groupe fonctionnel : R-NH₂, R-NHR', ou R-NR'R''
- Exemples : Méthylamine (CH₃NH₂)

#### `Amide`
Représente les amides, composés avec un groupe fonctionnel -CONH₂.

**Caractéristiques :**
- Groupe fonctionnel : R-CONH₂
- Exemples : Acétamide (CH₃CONH₂)

#### `Cetone`
Représente les cétones, composés avec un groupe carbonyle C=O.

**Caractéristiques :**
- Groupe fonctionnel : R-COR'
- Exemples : Acétone (CH₃COCH₃)

**Note :** Il y a une faute de frappe dans le nom de la classe (`Cetone` au lieu de `Ketone`).

---

### Acides carboxyliques

#### `CarboxylicAcid`
Représente les acides carboxyliques, composés avec un groupe fonctionnel -COOH.

**Caractéristiques :**
- Groupe fonctionnel : R-COOH
- Exemples : Acide acétique (CH₃COOH), Acide formique (HCOOH)

#### `CarboxylicAcidDerivative`
Représente les dérivés d'acides carboxyliques (esters, anhydrides, halogénures d'acyle, etc.).

**Caractéristiques :**
- Dérivés du groupe -COOH
- Exemples : Esters, Anhydrides, Amides

---

## État actuel

Toutes les classes sont actuellement des classes vides (stubs) héritant de `Hydrocabon`. Elles sont prêtes pour l'implémentation future de leurs fonctionnalités spécifiques.

## Prochaines étapes d'implémentation

Pour chaque classe, il serait utile d'implémenter :

1. **Constructeur** : Initialisation avec les paramètres spécifiques au type de composé
2. **Méthodes de validation** : Vérification de la structure moléculaire
3. **Méthodes de calcul** : Propriétés physico-chimiques (masse molaire, point d'ébullition, etc.)
4. **Méthodes de représentation** : Affichage de la structure (formule développée, SMILES, etc.)
5. **Méthodes de réaction** : Simulation de réactions chimiques spécifiques

## Notes importantes

- Toutes les classes héritent actuellement de `Hydrocabon`, ce qui peut ne pas être sémantiquement correct pour tous les composés (par exemple, les alcools ne sont pas des hydrocarbures purs)
- Une refactorisation future pourrait introduire des classes intermédiaires plus appropriées
- Les fautes de frappe dans les noms de classes (`Hydrocabon`, `Cetone`) devraient être corrigées pour maintenir la cohérence du code

