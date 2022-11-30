import sys
import numpy as np

def sequential_map(*args):
    object = args[-1]
    if type(object) == int:
        for func in args[:-1]:
            object = func(object)
    else:
        for func in args[:-1]:
            object = list(map(func, object))
    return object


def func_chain(*args):
    def result(object):
        if type(object)==int:  #for numbers
            for func in args:
                object = func(object)
        else:  #for lists and tuples
            for func in args:
                object = list(map(func, object))
        return object
    return result


def consensus_filter(*args):
    object = args[-1]
    if type(object) == int:  # for integer objects
        if args[0](object):
            return object
        else:
            return None
    for func in args[:-1]:  # for sets and lists
        right_nums = list(map(func, object))  # list of True and False
        indexes = [i for i, x in enumerate(right_nums) if x]  # indexes of right elems in object
        object = [object[ind] for ind in indexes]  # create new, reduced object
    return object


def conditional_reduce(func1, func2, object):
    right_nums = list(map(func1, object))  # list of True and False
    indexes = [i for i, x in enumerate(right_nums) if x]  # indexes of right elems in object
    object_for_func2 = [object[ind] for ind in indexes]  # create new, reduced object
    if len(object_for_func2) == 0:
        return None
    for i in range(len(object_for_func2)-1):
        i += 1
        object_for_func2[1] = object_for_func2[0]+object_for_func2[1]
        object_for_func2.remove(object_for_func2[0])
    return(object_for_func2[0])


def myprint(*args, sep=' ', end='\n', file=sys.stdout):
    string = ''
    for elem in args[:-1]:
        string = string + str(elem) + sep
    string = string + str(args[-1]) + end
    if file == sys.stdout:
        sys.stdout.write(string)
    else:
        with open(file, 'w') as f:
            f.write(string)