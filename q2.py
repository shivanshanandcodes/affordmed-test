#Author : Shivansh Anand
#Compression algorithm : Simple run length compression algorithm ( satifies the given sample strings )


def compress(str):
    i = 0
    compressed_str = {}
    while i < len(str):
        count = 1
        while i + 1 < len(str) and str[i] == str[i + 1]:
            count = count + 1
            i = i + 1
        i += 1
        compressed_str[str[i - 1]] = count
    return compressed_str


def decompress(compressed_str):
    decompressed_str = ""
    for letter in compressed_str:
        decompressed_str = decompressed_str + letter * compressed_str[letter]
    return decompressed_str


og_str = "aaabbbbbbbbbbbbCCd"
compressed_str = compress(og_str)
decompressed_str = decompress(compressed_str)
print("Original string :", og_str, "\nCompressed data as :", compressed_str, "\nDecompressed string :", decompressed_str)