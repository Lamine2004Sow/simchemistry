import pytest
from src.myClass import *


def test_add_atom_unique():
    h = Atom("Hydrogen", "H", 1, 1)
    mol = Molecule("H2")
    mol.add_atom(h)
    with pytest.raises(ValueError):
        mol.add_atom(h)


def test_add_connection_normalized_and_valid():
    h1 = Atom("Hydrogen", "H", 1, 1)
    h2 = Atom("Hydrogen", "H", 1, 1)
    mol = Molecule("H2", atoms=[h1, h2])
    mol.add_connection(h1, h2)
    # la liaison doit être présente et unique
    assert len(mol.connections) == 1
    assert mol.check_validity()


def test_valence_restant_and_overflow():
    o = Atom("Oxygen", "O", 8, 2)
    h1 = Atom("Hydrogen", "H", 1, 1)
    h2 = Atom("Hydrogen", "H", 1, 1)
    mol = Molecule("Water", atoms=[o, h1, h2])
    mol.add_connection(o, h1)
    mol.add_connection(o, h2)
    assert mol.get_valence_restant(o) == 0
    with pytest.raises(ValueError):
        # dépassement de valence
        mol.add_connection(h1, h2)


def test_delete_atom_removes_links():
    c = Atom("Carbon", "C", 6, 4)
    h = Atom("Hydrogen", "H", 1, 1)
    mol = Molecule("CH", atoms=[c, h])
    mol.add_connection(c, h)
    mol.delete_atom(h)
    assert h not in mol.atoms
    assert len(mol.connections) == 0


def test_invalid_parameters():
    with pytest.raises(ValueError):
        Atom("Bad", "B", 0, 1)
    with pytest.raises(ValueError):
        Atom("BadValence", "BV", 10, -1)
