from collections import defaultdict 

def group_anagram(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_word = ''.join(sorted(i))
        dfdict[sorted_word].append(i)
    return dfdict.values()
b = 'ant','bat','ten','tab','net'
print(group_anagram(b))