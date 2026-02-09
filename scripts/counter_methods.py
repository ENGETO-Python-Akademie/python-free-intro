from collections import Counter

for method in dir(Counter):
    if not method.startswith("_"):
        print(method)