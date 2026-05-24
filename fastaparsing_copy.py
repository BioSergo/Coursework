from pathlib import Path

folder =  Path('D:\\fasta-coursework-copy')
structure_id = []
dna = []

extensions = ["*.fna",
              "*.faa",
              "*.fasta"
            ]
fasta_d = {}
fasta_index = {}

for pattern in extensions:
    for file in folder.glob(pattern):
        with open(file, "r") as fasta:
            header_checker = False
            structures = []
            current_header = None

            for data in iter(fasta.readline, ""):

                if data.startswith(">"):

                    if header_checker and structures:
                        structure_num = len(structures)
                        fasta_d[current_header] = structures
                        index_info = current_header[1:].strip().split()[0]
                        fasta_index[index_info] = {
                            'filepath': str(file),
                            'position': line_end,
                            'str_num': structure_num
                        }

                    line_end = fasta.tell()
                    header = data.rstrip('\n')
                    current_header = header
                    structure_id.append(header)
                    structures = []
                    header_checker = True


                else:
                    structure = data.rstrip('\n')
                    structures.append(structure)
                    dna.append(structure)



            if header_checker and structures:
                structure_num = len(structures)
                fasta_d[current_header] = structures
                index_info = current_header[1:].strip().split()[0]
                fasta_index[index_info] = {
                    'filepath': str(file),
                    'position': line_end,
                    'str_num': structure_num
                }

def get_sequence(id):
    info = fasta_index[id]

    if id not in fasta_index:
        return 'Wrong id'

    with open(info['filepath'], 'r') as f:
        f.seek(info['position'])

        seq = []
        for i in range(info['str_num']):
             flow = f.readline().strip()
             seq.append(flow)
             result = "".join(seq)
        return result

print(get_sequence('NC_028841.1:1-120'))
print(fasta_index['WP_010883950.1'])


# размер словаря
print(f'length: {len(fasta_d)}')
print(f'length: {len(fasta_index)}')

# из GCF_020546685.1_ASM2054668v1_protein.faa(Multi-fasta)
print(f'protein_first: {get_sequence('WP_010883950.1')}') #Первый
print(f'protein_rn: {get_sequence('WP_010889582.1')}') #Случайный
print(f'protein_last: {get_sequence('WP_415577435.1')}') #Последний

# из GCA_020484125.1_ASM2048412v1_genomic.fna(Fasta)
print(f'genomic: {get_sequence('MZ326863.1')}')

# из Phage_Lily.fna и Phage_Lishaka.fna(Fasta)
print(f'complete genome phage1: {get_sequence('NC_028841.1:1-120')}')
print(f'complete genome phage2: {get_sequence('NC_011551.1:1-120')}')
