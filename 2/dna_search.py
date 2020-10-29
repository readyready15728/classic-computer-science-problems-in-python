gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s):
    gene = []

    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): # Avoids "frameshift mutation"
            return gene

        gene.append(s[i:i+3])

    return gene

def linear_contains(gene, key_codon):
    for codon in gene:
        if codon == key_codon:
            return True

    return False

def binary_contains(gene, key_codon):
    low = 0
    high = len(gene) - 1

    while low <= high:
        mid = (low + high) // 2

        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True

    return True

my_gene = string_to_gene(gene_str)

print(linear_contains(my_gene), 'ACG') # True
print(linear_contains(my_gene), 'GAT') # False

my_sorted_gene = sorted(my_gene))

print(binary_contains(my_gene), 'ACG') # True
print(binary_contains(my_gene), 'GAT') # False
