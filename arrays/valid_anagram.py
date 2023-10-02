from collections import Counter, defaultdict

def solutionA(s, t):
    return sorted(s) == sorted(t)

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS, countT = Counter(s), Counter(t)
    
    for c in countS:
        if countS[c] != countT[c]:
            return False
    return True

print(isAnagram("civic", "civic"))
print(isAnagram("rat", "car"))
print(isAnagram("silent", "listen"))
print(isAnagram("dog", "god"))