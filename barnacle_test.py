from Barnacle import Barnacle

# from http://www.rcsb.org/pdb/explore/explore.do?structureId=4tna
model = Barnacle("GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA")

model.sample()

print(model.get_angles())

import os
os.makedirs('output', exist_ok=True)
model.save_structure("output/output.pdb")
