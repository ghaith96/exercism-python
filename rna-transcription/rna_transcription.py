dna_to_rna = dict(
    G="C",
    C="G",
    T="A",
    A="U",
)


def to_rna(dna_strand):
    return "".join([dna_to_rna[letter] for letter in dna_strand])
