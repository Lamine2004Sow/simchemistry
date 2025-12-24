class Atom:
    def __init__(self, name, symbol, atomic_number, valence):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.valence = valence

    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol
    
    def get_atomic_number(self):
        return self.atomic_number
    
    def get_valence(self):
        return self.valence

    def __str__(self):
        return f"{self.name} ({self.symbol}) {self.atomic_number} {self.valence}"

class Molecule:
    def __init__(self, name, atoms, connections):
        self.name = name
        self.atoms = atoms
        self.connections = connections

    def check_validity(self):
        for atom in self.atoms:
            if atom.valence != len([a for connection in self.connections for a in connection if a == atom]):
                return False
        return True
    
    def get_atoms(self):
        return self.atoms
    
    def get_connections(self):
        return self.connections
    
    def get_name(self):
        return self.name
    
    def get_valence_restant(self, atom):
        return atom.valence - len([a for connection in self.connections for a in connection if a == atom])
    
    def __str__(self):
        return f"{self.name} ({self.atoms}) {self.connections}"

    def add_atom(self, atom):
        self.atoms.append(atom)
    
    def add_connection(self, atom1, atom2):
        try:
            self.connections.append((atom1, atom2))
        except ValueError:
            raise ValueError(f"Connection between {atom1} and {atom2} already exists")
        except Exception as e:
            raise ValueError(f"Error adding connection between {atom1} and {atom2}: {e}")

    def delete_connection(self, atom1, atom2):
        try:
            t1 = (atom1, atom2)
            t2 = (atom2, atom1)
            if t1 in self.connections:
                self.connections.remove(t1)
            elif t2 in self.connections:
                self.connections.remove(t2)
            else:
                raise ValueError(f"Connection between {atom1} and {atom2} not found")
        
        except Exception as e:
            raise ValueError(f"Error deleting connection between {atom1} and {atom2}: {e}")
    
    def delete_atom(self,atom):
        try:
            self.atoms.remove(atom)
        except ValueError:
            raise ValueError(f"Atom {atom} not found")
        except Exception as e:
            raise ValueError(f"Error deleting atom {atom}: {e}")