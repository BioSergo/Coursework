from pathlib import Path

folder =  Path('D:\\#fasta-coursework')
structure_id = []
dna = []
#как читать список всех файлов в директории
#получить словарь для имен посл и самих послед до чт
#подправить код для иницилизации словаря с использованием флагов(True <=> False).
#> флаг меняется в двух случаях

extensions = ["*.fna",
              "*.faa",
              "*.fasta"
            ]
fasta_d = {}

for pattern in extensions:
    for file in folder.glob(pattern):
        with open(file, "r") as fasta:
            header_checker = True
            structures = []
            current_header = ""
            for data in fasta:
                if data.startswith(">"):
                    header = data.rstrip('\n')
                    current_header = header
                    if header_checker and structures:
                        fasta_d.update({current_header: structures})
                        structures.clear()
                    structure_id.append(header)
                    header_checker = False

                else:
                    structure = data.rstrip('\n')
                    structures.append(structure)
                    dna.append(structure)
                    header_checker = True

print(f'Dna: {dna}')
print(f'structure_id: {structure_id}')
print(f'protein: {fasta_d['>WP_415577435.1 EamA family transporter [Deinococcus radiodurans]']}')