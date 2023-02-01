# this program works by getting the full string
# and then using list slicing slices the full string
# to get the new desired string that is
# "object-oriented programming with python"

message = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"

string_1 = message[39:67]
string_2 = message[107:112]
string_3 = message[0:7]

full_string = string_1 + string_2 + string_3
print(full_string)
