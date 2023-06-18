from Bio.PDB import *



parser = PDBParser(QUIET=True)

structure = parser.get_structure("PF14331", "PF14331")

print(str(structure.get_residues))

io=PDBIO()



io.set_structure(structure)

io.save("bio-pdb-pdbio-out.pdb")



