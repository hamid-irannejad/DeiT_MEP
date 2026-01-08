from pdbfixer import PDBFixer
from openmm.app import PDBFile

# Load your protein PDB file
fixer = PDBFixer(filename='tdoA_fixed.pdb')

# Report issues
#print("Missing residues:", fixer.missingResidues)
#print("Missing atoms:", fixer.missingAtoms)
#print("Nonstandard residues:", fixer.nonstandardResidues)

fixer.findMissingResidues()
fixer.findNonstandardResidues()
fixer.replaceNonstandardResidues()
#fixer.removeHeterogens(True)   Comment this line if you want to keep Heme group
fixer.findMissingAtoms()
fixer.addMissingAtoms()
fixer.addMissingHydrogens(7.0)

# Report issues
print("Missing residues:", fixer.missingResidues)
print("Missing atoms:", fixer.missingAtoms)
print("Nonstandard residues:", fixer.nonstandardResidues)


# Save repaired structure
with open('tdoA2_fixed.pdb', 'w') as outfile:
    PDBFile.writeFile(fixer.topology, fixer.positions, outfile)

