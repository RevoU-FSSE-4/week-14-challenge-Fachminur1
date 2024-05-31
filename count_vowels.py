def count_vowels(word: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Example usage:
word = "Lorem Impun das bgilit ini di biningging"
print(count_vowels(word)) 