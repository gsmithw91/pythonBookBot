

file_path = './books/frankenstein.txt'

def textCount(text: str) -> int:
    """
    Returns the total number of words in the text.
    """
    words = text.split()
    return len(words)

def characterCount(text: str) -> dict:
    """
    Returns a dictionary with the count of each letter (a-z) in the text.
    """
    character_count_dict = {}
    for char in text.lower():
        # Only count alphabetic characters if that's desired
        if char.isalpha():
            if char not in character_count_dict:
                character_count_dict[char] = 1
            else:
                character_count_dict[char] += 1
    return character_count_dict

def reportCharCount(text: str, file_path: str):
    """
    Prints the final report, including:
    - Total word count
    - Character counts (sorted by most frequent)
    """
    # 1. Print the heading
    print(f"--- Begin report of {file_path} ---")
    
    # 2. Print the word count
    word_count = textCount(text)
    print(f"{word_count} words found in the document\n")
    
    # 3. Print the character counts (sorted by frequency)
    char_dict = characterCount(text)
    # Sort the dictionary by descending frequency
    sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    
    # 4. Print each character count
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    # 5. Print the closing line
    print("--- End report ---")

def main():
    with open(file_path, encoding='utf-8') as f:
        file_contents = f.read()
    
    reportCharCount(file_contents, file_path)

if __name__ == '__main__':
    main()

