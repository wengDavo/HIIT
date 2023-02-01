# This program takes in a string and returns
# the reverse of the string using list slicing and step -1


def reverse_string(msg):
    return msg[::-1]


msg = "arigato"
print("Initial string:", msg)
print("Reversed string:", reverse_string(msg))
