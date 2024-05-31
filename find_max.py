def find_max(numbers: list) -> int:
    if not numbers:
        return None  # Return None if the list is empty
    
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Example usage:
numbers = [3, 3, 3, 1, 5, 8]
print(find_max(numbers))