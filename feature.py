import re
def pig_latin(text: str) -> str:
    def convert(token: str) -> str:
        if not token:
            return token

        lower = token.lower()
        m = re.match(r"^([^aeiou]*)([a-z]+)$", lower)
        if not m:
            return token

        head, tail = m.groups()
        out = f"{tail}{head}ay" if head else f"{tail}way"

        if token.isupper():
            return out.upper()
        if token[0].isupper():
            return out.capitalize()
        return out

    return re.sub(r"[A-Za-z]+", lambda m: convert(m.group(0)), text)

def pig_latin_advanced(text):
    def convert_word(word):
    # 1. Keep 'qu' together and detect when 'y' is used as a consonant vs. as a vowel:
        # Regex Breakdown:
        # ^                 : Start at the beginning of the word.
        # (                 : START GROUP 1 (The Consonant Cluster)
        # [^aeiouy]*qu      : Case 1: Match any consonants + 'qu' except the vowels in brackets
        #   |               : OR
        #   [y](?=[aeiou])  : Case 2: Match 'y' ONLY if a vowel follows (y as consonant).
        #   |               : OR
        #   [^aeiouy]+      : Case 3: Match standard consonants (stops at a, e, i, o, u, or y).
        # )?                : END GROUP 1 (if the word starts with a vowel, this is empty).
        # (.*)              : GROUP 2: Capture everything else left in the word. (The Rest)
        match = re.match(r'^([^aeiouy]*qu|[y](?=[aeiou])|[^aeiouy]+)?(.*)', word, re.I) # re.I for allowing the RegEx to match both uppercase & lowercase.
        cluster, rest = match.groups()  # Unpacks the two captured groups into two separate variables

    # 2. Determine the new word structure
        if not cluster:
            # Starts with a vowel (a, e, i, o, u)
            new_word = word + "way"   #words that begin with vowel sounds, "way" or "yay" is added to the end.
        else:
            # Starts with a consonant cluster
            new_word = rest + cluster + "ay"

    # 3. Preserve Capitalization
        # Check if the entire word is all uppercase:
        if word.isupper():
            return new_word.upper()
        # If the word is title case with first letter only:
        if word[0].isupper():
            return new_word.capitalize()
        # Default: return the word in lowercase:
        return new_word.lower()

    # Apply conversion to words, while keeping the punctuations and spaces intact.
    def helper(m):
        """
        We define a 'helper' function that re.sub will call every time it finds a word.
        It receives a 'Match Object' (m) rather than a simple string.
        """
        return convert_word(m.group(0)) # m.group(0) extracts the actual text string found.
    # re.sub searches 'text' for any sequence of letters [a-zA-Z]+.
    # Every time it finds one, it runs it through 'helper' and replaces the original word with the Pig Latin version, leaving spaces/punctuations alone.
    return re.sub(r'[a-zA-Z]+', helper, text)

# Testing
test_cases = [
    "Quiet4",   # 'qu' stays together
    "Yellow",  # 'y' is consonant -
    "Style",   # 'y' is vowel (cluster is 'St')
    "String!", # cluster is 'Str' -
    "IDLE",    # all capitalization
    "Rhythm",   # 'y' is vowel (cluster is 'rh')
    "square"    # no capitalization & 'qu' is not the beginning.
]

for t in test_cases:
    print(f"{t:10} ➡️ {pig_latin_advanced(t)}")