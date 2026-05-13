files = [#'GCA_020484125.1_ASM2048412v1_genomic.fna',
         #'GCF_020546685.1_ASM2054668v1_cds_from_genomic.fna',
         #'GCF_020546685.1_ASM2054668v1_genomic.fna',
         #'GCF_020546685.1_ASM2054668v1_protein.faa',
         'Phage Lily.fna',
         'Phage Lishaka.fna'
]

#как читать список всех файлов в директории
#получить словарь для имен посл и самих послед до чт

structure_id = []
dna = []

for file in files:
    with open(file) as fasta:
        for data in fasta:
            if data.startswith(">"):
                header = data.rstrip('\n')
                structure_id.append(header)
            else:
                structure = data.rstrip('\n')
                dna.append(structure)
        print(structure_id)
        print(dna)
print(f'Dna: {dna}')
print(f'structure_id: {structure_id}')