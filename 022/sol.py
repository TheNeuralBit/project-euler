def score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

print(score('COLIN'))
with open('names.txt', 'r') as fp:
    names = (name.strip("\"") for name in fp.readline().strip().split(","))

    result = sum(position*score(name) for position, name in enumerate(sorted(names), 1))
    print(result)
