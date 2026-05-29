class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_dict = {}
        last_dict = {}
        for idx,letter in enumerate(word):
            if letter not in first_dict.keys():
                first_dict[letter] = idx
            last_dict[letter] = idx
        count = 0
        for item in last_dict.keys():
            if item.upper() in first_dict.keys() and last_dict[item] < first_dict[item.upper()]:
                count += 1
        return count
