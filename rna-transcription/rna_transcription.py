dna_to_rna = dict(
    G="C",
    C="G",
    T="A",
    A="U",
)


def to_rna(dna_strand):
    mapped_rna = map(lambda letter: dna_to_rna[letter], dna_strand)
    return "".join(mapped_rna)
