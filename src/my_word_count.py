from collections import Counter
from re import split

counter = Counter()
with open("C:/Users/zhibiao/Desktop/WC_Input/text.txt","rU") as files:
    for line in files:
        line = line.strip().lower()
        if not line:
            continue
        counter.update(word for word in split("[^a-zA-Z']+", line) if word)

list_items = counter.items()
list_items.sort()

print "%-16s | %16s" % ("Word", "Count")
for word, count in list_items:
    print "%-16s | %16d" % (word, count)
