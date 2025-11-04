from Bio import AlignIO

alignment = AlignIO.read("all_aligned.fasta", "fasta")
ref = alignment[0].seq

print("Reference:", alignment[0].id)
print("Comparing with other sequences...\n")

for record in alignment[1:]:
    print(f"Mutations in {record.id}:")
    for i, (a, b) in enumerate(zip(ref, record.seq)):
        if a != b and a != "-" and b != "-":
            print(f"  Position {i+1}: {a} → {b}")
    print()
