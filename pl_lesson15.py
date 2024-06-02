
def analyze_text(passage):
    vowels = "aeiou"

    # Getting the number of words in the passage
    countOfWords = len(passage.split())
    print("Count of Words in the given Sentence:", countOfWords)

    # Count the number of vowels and consonants in the passage
    countOfVowels = 0
    countOfConsonants = 0
    for character in passage:
        if character.isalpha():
            if character in vowels:
                countOfVowels += 1
            else:
                countOfConsonants += 1
    print("Count of Vowels in the given Sentence:", countOfVowels)
    print("Count of Consonants in the given Sentence:", countOfConsonants)


########################################################################
passage = input("Please enter: ")
analyze_text(passage)

