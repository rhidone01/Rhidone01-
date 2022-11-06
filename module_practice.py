from collections import defaultdict

def group_anagram(a):
    dfdict = defaultdict(list) 
    for i in a:
        s_word = ' '.join(sorted(i))
        dfdict[s_word].append(i)
    return dfdict.values()

words = ['tea','car','net','bat','ten','eat','arc','tab','ate']
print(group_anagram(words))