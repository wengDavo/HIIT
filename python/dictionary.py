def freq_checker(word):
    my_dict = {}
    for item in word:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    return my_dict

def to_tuple(my_dict):
    sorted_dict = sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
    return sorted_dict

def frequent_10(my_dict):
    return my_dict[0:11]

if __name__ == "__main__":
    word = input("Enter a sentance:")
    print("-"*10)
    dict = freq_checker(word)
    print(f"Number of characters:{dict}")
    print("-"*10)
    dict_sorted = to_tuple(dict)
    print(f"Sentence Converted to Tuple and sorted:{dict_sorted}")
    print("-"*10)
    dict_frequent = frequent_10(dict_sorted)
    print(f"The 10 most frequent characters are:{dict_frequent}")
    print("-"*10)


