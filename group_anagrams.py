from collections import defaultdict 

def group_anagram(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_word = ''.join((i))
        dfdict[sorted_word].append(i)
    return dfdict.values()

words = ['tea','car','net','bat','ten','eat','arc','tab','ate']
print(group_anagram(words)) 
#dict_values([['tea', 'eat', 'ate'], ['car', 'arc'], ['net', 'ten'], ['bat', 'tab']])