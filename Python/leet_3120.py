class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        my_dict = {}
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for letter in word:
            if letter not in letters:
                continue
            if letter.upper() in word:
                my_dict[letter] = 1
        total = 0
        for key in my_dict:
            total += my_dict[key]
        return total
