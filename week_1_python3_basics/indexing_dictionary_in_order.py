# an example of using sorted to access keys in order even though they are unordered in a dictionary

age = {"Jim":31, "Nick":31, "Pam":27, "Sam":35, "Tim":31, "Tom":50}

print("No specific order: ")
# unordered (will loop over keys by default)
for name in age:
    print(name, age[name])

# alphabetical order
print("\nAlphabetical order")
for name in sorted(age.keys()):
    print(name, age[name])

# reverse alphabetical order
print("\nReverse alphabetical order")
for name in sorted(age.keys(), reverse=True):
    print(name, age[name])
