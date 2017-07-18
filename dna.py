sample = ['GTA', 'GGG', 'CAC']


def read_dna(dna_file):
    """Reads DNA file."""
    dna_data = ''

    with open(dna_file, 'r') as f:
        for line in f:
            dna_data += line

    return dna_data


def dna_codons(dna):
    """Creates a list of codons."""
    codons = []

    with open(dna) as dna_file:
        for f in dna_file:
            for i in range(0, len(f), 3):
                if (i + 3) < len(f):
                    codons.append(f[i:i + 3])
    return codons


def match_dna(dna):
    """Counts matching codons."""
    matches = 0

    for codon in dna:
        if codon in sample:
            matches += 1

    return matches


def is_criminal(dna_sample):
    """Determines highest number of codon matches."""
    dna_data = read_dna(dna_sample)
    codons = dna_codons(dna_sample)
    num_matches = match_dna(codons)

    if num_matches >= 3:
        print 'There were %d matches, investigation should continue.' % (num_matches)
    else:
        print 'There were %d matches, not enough to warrant further investigation.' % (num_matches)


is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')
