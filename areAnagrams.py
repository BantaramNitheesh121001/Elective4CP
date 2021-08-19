# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    s1 = s1.upper()
    s2 = s2.upper()
    if len(s1) != len(s2):
        return False
    for i in s1:
        a = s1.count(i)
        b = s2.count(i)
        if a != b:
            return False
    return True
# write your test cases here...
assert (areAnagrams("hello","oehll") == True)
assert (areAnagrams("hell","oehll") == False)
assert (areAnagrams("Thisisheaven","isheavenThis") == True)
assert (areAnagrams("Abbabbba","ababa") == False)
print("All test cases passed... :-)")