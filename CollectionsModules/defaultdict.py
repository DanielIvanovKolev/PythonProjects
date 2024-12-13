from collections import defaultdict

d = {'a': 10}

print(d)
print(d['a'])

d = defaultdict(lambda: 0)  # This says that all the default values will be 0

print(d['Wrong key'])  # We don't have this key in d, but we put default value

