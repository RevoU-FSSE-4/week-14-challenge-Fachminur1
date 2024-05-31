def are_anagrams(word1: str, word2: str) -> bool:
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    return sorted(word1) == sorted(word2)

word1 = "Total"
word2 = "Football"
print(are_anagrams(word1, word2))