from collections import Counter
from re import split

counter = Counter()
with open("../wc_input/test.txt","rU") as files:
    for line in files:
        line = line.strip().lower()
        if not line:
            continue
        counter.update(word for word in split("[^a-zA-Z']+", line) if word)

list_items = counter.items()
list_items.sort()



with open("../wc_output/wc_result.txt","wb") as text_file:
    text_file.write('%-16s | %16s \n' % ("Word", "Count"))
    for word, count in list_items:
        text_file.write('%-16s | %16d \n' % (word, count))



