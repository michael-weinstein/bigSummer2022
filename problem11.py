import rosalindSupport


if __name__ == "__main__":
    largeString = rosalindSupport.dnaHandler.DNASequence("CAATGCATCTATGCATCTATGCATCGATGCATCGCATGCATCTAATCGTCGATGCATCTCTATGCATCCTATGCATCATGCATCCAGAATGCATCAGACGAGTATGCATCATGCATCATGCATCATTCTGAATGCATCGGGTATGCATCATGCATCATGCATCATGCATCATGCATCATGCATCCTCCACATGCATCCATGCATCAAAGTCGGCTATGCATCACATGCATCCCAATGCATCGGGATGCATCAATGCATCAATATGCATCATGCATCATGCATCCTAGATGCATCCAAATGCATCGAATGCATCATGCATCCTAATGCATCACAGATGCATCGATGCATCGATGCATCATGCATCTCATCGATGCATCAATGCATCATGCATCATGCATCATGCATCAATGCATCTGGGTGTTAATGCATCCATGCATCGCTTTATGCATCACGTCAAAAATGCATCATGCATCAATGCATCATGCATCCCATGCATCATGCATCAAATGCATCACGATGCATCTAATGCATCGATGCATCCACATGCATCTTCATGCATCATGCATCAGCGATGCATCATGCATCACGTGCATGCATCATGCATCAATCTATGCATCAATGCATCATGCATCGCTTGACTCATGCATCATGCATCGTGGCCTCCATGCATCATGCATCAATTCAGCTGTTATATGCATCGAATGCATCATGCATCATGCATCACACATGCATCGCCTCACGGTCGTGATGCATCATGCATCACTGATGCATCACCGTTATGCATCAACCATGCATCATGCATCGTAATGCATCCTTAGAGATTTCACTCCGTGGTATGCATCATGCATCCTTAATGCATCATGCATCATGCATCCATGCATCATGCATCGATGCATCATGCATCTTGTAAATGCATCTCTAGATGCATCCATGCATCAACGATGCATCAAATGCATCTTATGCATC")
    substring = "ATGCATCAT"
    starts = largeString.findSubstring(substring)
    print(" ".join([str(item) for item in starts]))
