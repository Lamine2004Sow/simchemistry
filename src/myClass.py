class Atom:
    """Atome minimal avec quelques garde-fous."""

    def __init__(self, name, symbol, atomic_number, valence):
        if atomic_number <= 0:
            raise ValueError("Le numéro atomique doit être positif.")
        if valence < 0:
            raise ValueError("La valence ne peut pas être négative.")
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.valence = valence

    def __str__(self):
        return f"{self.name} ({self.symbol}) {self.atomic_number} {self.valence}"


class Molecule:
    """Version simple : liste d'atomes + liaisons non orientées."""

    def __init__(self, name, atoms=None, connections=None):
        self.name = name
        self.atoms = []
        self.connections = []  # liste de tuples (atom1, atom2) triés pour éviter les doublons

        atoms = atoms or []
        for atom in atoms:
            self.add_atom(atom)

        connections = connections or []
        for a1, a2 in connections:
            self.add_connection(a1, a2)

    def _normalize(self, atom1, atom2):
        if atom1 == atom2:
            raise ValueError("Pas de boucle sur soi-même.")
        if atom1 not in self.atoms or atom2 not in self.atoms:
            raise ValueError("Les atomes doivent appartenir à la molécule.")
        # tri simple pour rendre la liaison non orientée
        return tuple(sorted((atom1, atom2), key=id))

    def _neighbors(self, atom):
        return [
            b if a == atom else a
            for (a, b) in self.connections
            if atom in (a, b)
        ]

    def check_validity(self):
        for atom in self.atoms:
            if len(self._neighbors(atom)) > atom.valence:
                return False
        return True

    def get_valence_restant(self, atom):
        if atom not in self.atoms:
            raise ValueError("Atome absent de la molécule.")
        return atom.valence - len(self._neighbors(atom))

    def add_atom(self, atom):
        if atom in self.atoms:
            raise ValueError(f"Atome déjà présent: {atom}")
        self.atoms.append(atom)

    def add_connection(self, atom1, atom2):
        link = self._normalize(atom1, atom2)
        if link in self.connections:
            raise ValueError(f"Liaison déjà présente: {link}")
        self.connections.append(link)
        if not self.check_validity():
            self.connections.remove(link)
            raise ValueError("Ajout invalide: valence dépassée.")

    def delete_connection(self, atom1, atom2):
        link = self._normalize(atom1, atom2)
        if link not in self.connections:
            raise ValueError(f"Liaison introuvable: {link}")
        self.connections.remove(link)

    def delete_atom(self, atom):
        if atom not in self.atoms:
            raise ValueError(f"Atome introuvable: {atom}")
        self.connections = [c for c in self.connections if atom not in c]
        self.atoms.remove(atom)

    def __str__(self):
        return f"{self.name} (atoms={self.atoms}) connections={self.connections}"