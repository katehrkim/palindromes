def palindrome(word):
    if type(word) == str:
        word = word.lower()
    if type(word) == int:
        word = str(word)
    punctuations = '''!() -[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned = ""
    for char in word:
        if char not in punctuations:
            cleaned = cleaned + char
    half_len = len(cleaned) // 2
    for i in range(0, half_len):
        if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
            return False
    return True