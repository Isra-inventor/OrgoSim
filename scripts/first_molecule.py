from rdkit import Chem
from rdkit.Chem import AllChem, rdMolTransforms

smiles = "CCCC"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, randomSeed=42)

conf = mol.GetConformer()

print(f"{smiles}: {mol.GetNumAtoms()} atoms")
for atom in mol.GetAtoms():
    pos = conf.GetAtomPosition(atom.GetIdx())
    print(f"{atom.GetIdx():>2} {atom.GetSymbol():<2} {pos.x:7.3f} {pos.y:7.3f} {pos.z:7.3f}")

angle = rdMolTransforms.GetDihedralDeg(conf, 0, 1, 2, 3)
print(f"C0-C1-C2-C3 dihedral: {angle:.1f} degrees")
