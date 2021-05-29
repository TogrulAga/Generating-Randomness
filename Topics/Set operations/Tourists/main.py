# work with these variables
eugene = set(input().split())
rose = set(input().split())
intersection = eugene.intersection(rose)
union = eugene.union(rose)
print(union - intersection)
