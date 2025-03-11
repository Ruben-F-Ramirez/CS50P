def main():
    word_in = input("Enter your string: ")
    print(shorten(word_in))

# correct version
"""
def shorten(word):
    vowels = "aeiou"
    twttr = ""
    for c in word:
        if c.lower() not in vowels:
            twttr = twttr + c
    return twttr
"""
# bugged version
def shorten(word):
    vowels = "aeiou"
    twttr = ""
    for c in word:
        if c not in vowels:
            twttr = twttr + c
    return twttr


if __name__ == "__main__":
    main()