from pathlib import Path

folder =  Path('D:\\#fasta-coursework')
structure_id = []
dna = []

extensions = ["*.fna",
              "*.faa",
              "*.fasta"
            ]
fasta_d = {}

for pattern in extensions:
    for file in folder.glob(pattern):
        with open(file, "r") as fasta:
            header_checker = False
            structures = []
            current_header = None

            for data in fasta:

                if data.startswith(">"):
                    header = data.rstrip('\n')
                    current_header = header

                    if header_checker and structures:
                        fasta_d[current_header] = structures

                    structure_id.append(header)
                    structures = []
                    header_checker = True

                else:
                    structure = data.rstrip('\n')
                    structures.append(structure)
                    dna.append(structure)

            if header_checker and structures:
                fasta_d[current_header] = structures



# размер словаря
print(f'length: {len(fasta_d)}')

# из GCF_020546685.1_ASM2054668v1_protein.faa(Multi-fasta)
print(f'protein_first: {fasta_d['>WP_010883953.1 potassium-transporting ATPase subunit KdpB [Deinococcus radiodurans]']}') #Первый
print(f'protein_rn: {fasta_d['>WP_010889582.1 urea ABC transporter ATP-binding protein UrtD [Deinococcus radiodurans]']}') #Случайный
print(f'protein_last: {fasta_d['>WP_415577435.1 EamA family transporter [Deinococcus radiodurans]']}') #Последний

# из GCA_020484125.1_ASM2048412v1_genomic.fna(Fasta)
print(f'genomic_last: {fasta_d['>MZ326863.1 Burkholderia phage Paku, complete genome']}')

# из Phage_Lily.fna и Phage_Lishaka.fna(Fasta)
print(f'complete genome phage1: {fasta_d['>NC_028841.1:1-120 Bacteriophage Lily, complete genome']}')
print(f'complete genome phage2: {fasta_d['>NC_011551.1:1-120 Bacteriophage APSE-2, complete genome']}')