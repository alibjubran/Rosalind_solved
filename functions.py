def countnucleotides (DNA):
    nucleotides=list(set(DNA))
    nucleotides.sort()
    counts=[]
    for i in nucleotides:
        counts.append(DNA.count(i))
    counted_nucleotides=list(zip(nucleotides,counts))
    return (counted_nucleotides)
