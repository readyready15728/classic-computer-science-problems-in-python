import sys

class CompressedGene:
    def __init__(self, gene):
        self.__compress(gene)

    def __compress(self, gene):
        self.bit_string = 0

        for nucleotide in gene.upper():
            self.bit_string <<= 2

            if nucleotide == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError(f'Invalid nucleotide: {nucleotide}')

    def decompress(self):
        gene = ''

        for i in range(0, self.bit_string.bit_length(), 2):
            bits = self.bit_string >> i & 0b11

            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                raise ValueError(f'Invalid bits {bits}')

        return gene[::-1]

    def __str__(self):
        return self.decompress()

original = 'TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA' * 100
compressed = CompressedGene(original)

print(f'Original is {sys.getsizeof(original)} bytes')
print(f'Compressed is {sys.getsizeof(compressed.bit_string)}')
print(compressed)
print(f'Original and decompressed are the same: {original == compressed.decompress()}')
