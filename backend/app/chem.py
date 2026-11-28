from rdkit import Chem
from rdkit.Chem import AllChem


def smiles_to_molblock(smiles):
    """Return a 3D molecule as a mol block string, or None if it can't be built."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    mol = Chem.AddHs(mol)
    if AllChem.EmbedMolecule(mol, randomSeed=42) == -1:
        return None

    return Chem.MolToMolBlock(mol)
