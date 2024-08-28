class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        reverse_h = {}
        a = s.split(" ")

        if len(pattern) != len(a):
            return False

        for c ,w in zip(pattern ,a):
            if c in h and h[c] !=w :
                return False

            if w in reverse_h and reverse_h[w] != c :
                return False

            h[c] =w
            reverse_h[w] = c
        


        return True