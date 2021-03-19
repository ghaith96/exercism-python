seq_to_protein = dict(
    AUG="Methionine",
    UUU="Phenylalanine",
    UUC="Phenylalanine",
    UUA="Leucine",
    UUG="Leucine",
    UCU="Serine",
    UCC="Serine",
    UCA="Serine",
    UCG="Serine",
    UAU="Tyrosine",
    UAC="Tyrosine",
    UGU="Cysteine",
    UGC="Cysteine",
    UGG="Tryptophan",
    UAA="STOP",
    UAG="STOP",
    UGA="STOP",
)


def get_sequences(strand: str):
    sequence_len = 3
    cursor = 0
    while cursor < len(strand):
        cursor += sequence_len
        yield strand[cursor - sequence_len : cursor]


def proteins(strand):
    result = []
    for seq in get_sequences(strand):
        mapped_seq = seq_to_protein[seq]
        if mapped_seq == "STOP":
            return result
        result.append(mapped_seq)

    return result