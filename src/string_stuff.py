import collections


def frequent_character(arg1):


    return collections.Counter(arg1).most_common(1)[0][0]
def split_string(arg1):
    return arg1[:int(len(arg1)/2)], arg1[int(len(arg1)/2):]
