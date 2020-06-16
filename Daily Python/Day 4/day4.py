lister = [2,2,2,6,7,8,9,9,76,34]

from collections import Counter

c = Counter(lister)

print(c.most_common(1))