
l = input().split(',')
d = {}
for element in l:
    element = element.strip()  # Remove any leading/trailing whitespace
    if element in d:
        d[element] += 1
    else:
        d[element] = 1

# Print the frequency of each element
for element, count in d.items():
    print(f"Element: {element}, Frequency: {count}")
