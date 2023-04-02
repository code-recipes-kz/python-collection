class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        words_length = len(words)
        substring_length = word_length * words_length
        
        words_count = Counter(words)
        result = []
        
        for i in range(len(s) - substring_length + 1):
            substring = s[i:i+substring_length]
            substring_count = Counter([substring[j:j+word_length] for j in range(0, substring_length, word_length)])
            
            if substring_count == words_count:
                result.append(i)
                
        return result