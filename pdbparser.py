def parse_rosetta(file):
    amino_acids = []
    reading = False
    with open(file, 'r') as f:
        for line in f:
            if line.startswith("# All scores below are weighted scores, not raw scores."):
                reading = True
                continue
            if reading:
                amino_acid = line.split()[0]
                if amino_acid != 'label' and amino_acid != 'weights' and amino_acid != 'pose':
                    amino_acids.append(amino_acid)
    return amino_acids

amino_acids = parse_rosetta('your_file.pdb')
print(amino_acids)
