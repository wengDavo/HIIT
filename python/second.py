def two(msg):
    if len(msg) <= 2:
        return "string to short"
    newMsg = ''
    for i in range(2):
        newMsg += msg[i]
    for i in range(1,3):
        newMsg += msg[-i]
    return newMsg

message = "elephant"
print(two(message))
