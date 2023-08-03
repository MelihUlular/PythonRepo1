def find_longest_unique_substring(s):
    max_length = 0
    max_substring = ""
    start = 0
    char_index_map = {}

    for i, char in enumerate(s): # Check if the character is already in the char_index_map and its index is greater than or equal to the start index.
        
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        # Update the index of the current character in the char_index_map.
        char_index_map[char] = i

        # Calculating the length of the current substring without duplicates and update max_length and max_substring accordingly.
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_substring = s[start:i+1]

    return max_substring, max_length


if __name__ == "__main__":
    #input string to console from the user.
    input_string = input("input: ")

    # Find the longest unique substring and its length using the find_longest_unique_substring function.
    substring, length = find_longest_unique_substring(input_string)

    print(f"output: {substring} length: {length}")