def analyze_sentence(sentence):
    # Check if the sentence ends with a point
    if sentence[-1] != '.':
        print("Invalid input. Sentence should end with a point.")
        return
    
    # Initialize counters
    sentence_length = 0
    word_count = 0
    vowel_count = 0
    vowels = 'aeiouAEIOU'
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Increment the sentence length
        sentence_length += 1
        
        # Count vowels
        if char in vowels:
            vowel_count += 1
        
        # Check for word separation
        if char == ' ':
            word_count += 1
    
    # Subtract 1 from word_count to account for the period at the end of the sentence
    word_count += 1
    
    print("Sentence length:", sentence_length)
    print("Number of words:", word_count)
    print("Number of vowels:", vowel_count)

# Example usage
input_sentence = "Hello, world. This is an example sentence."
analyze_sentence(input_sentence)
