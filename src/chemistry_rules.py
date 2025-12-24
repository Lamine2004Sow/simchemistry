from operator import iconcat
from src.myClass import Molecule, Atom

def is_alkane(molecule: Molecule):
    #un alcane est tjrs saturer, donc toutes les valences sont utilisées
    if not molecule.is_complete():
        return False
    
    #on doit aussi verifier qu'il n'y a que des atomes de carbone et d'hydrogene
    c_count = sum(1 for atom in molecule.atoms if atom.symbol == "C")
    h_count = sum(1 for atom in molecule.atoms if atom.symbol == "H")

    if c_count + h_count != len(molecule.atoms):
        return False
    
    #forme acyclique CnH2n+2
    return h_count == 2 * c_count + 2

def is_alkene(molecule: Molecule):
    #un alcene est tjrs sature, donc toutes les valences sont utilisées
    if not molecule.is_complete():
        return False
    
    #on doit aussi verifier qu'il n'y a que des atomes de carbone et d'hydrogene
    c_count = sum(1 for atom in molecule.atoms if atom.symbol == "C")
    h_count = sum(1 for atom in molecule.atoms if atom.symbol == "H")
    
    if c_count + h_count != len(molecule.atoms):
        return False
    
    #forme acyclique CnH2n
    return h_count == 2 * c_count

def is_alkyne(molecule: Molecule):
    #un alkyne est tjrs sature, donc toutes les valences sont utilisées
    if not molecule.is_complete():
        return False
    
    #on doit aussi verifier qu'il n'y a que des atomes de carbone et d'hydrogene
    c_count = sum(1 for atom in molecule.atoms if atom.symbol == "C")
    h_count = sum(1 for atom in molecule.atoms if atom.symbol == "H")

    if c_count + h_count != len(molecule.atoms):
        return False
    
    #forme acyclique CnH2n-2
    return h_count == 2 * c_count - 2

def is_alcohol(molecule: Molecule):
    #un alcool aussi est sature, donc toutes les valences sont utilisées
    if not molecule.is_complete():
        return False
    
    #on doit aussi verifier qu'il n'y a que des atomes de carbone et d'hydrogene
    c_count = sum(1 for atom in molecule.atoms if atom.symbol == "C")
    h_count = sum(1 for atom in molecule.atoms if atom.symbol == "H")
    o_atoms = [atom for atom in molecule.atoms if atom.symbol == "O"]
    
    if len(o_atoms) != 1:
        return False

    if c_count + h_count +1 != len(molecule.atoms):
        return False
    
    oxygene = o_atoms[0]
    o_neighbor = molecule._neighbors(oxygene) 

    if len(o_neighbor) != 2:
        return False

    #je dois verifier que ces deux voisin ne sont que C et H
    symbols = {atom.symbol for atom in o_neighbor}

    if not symbols.issubset({"C", "H"}):
        return False

    if "C" not in symbols:
        return False
    if "H" not in symbols:
        return False

    return True