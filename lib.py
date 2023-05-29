def is_term(term):
    count = 1
    for symbol in term:
        if count == 0:
             return False
        if symbol == 'implies':
            count += 1
        else:
            count -= 1
    return count == 0
    
def is_theorem(term, set_size):
    permutations = get_permutations(set_size)
    for permutation in permutations:
        adjusted_term = make_function(term, permutation)
        if evaluate_function(adjusted_term) == 0:
            return False
    return True

def get_permutations(set_size):
    if set_size == 1:
        return [[0],[1]]
    permutations = []
    reduced_permutations = get_permutations(set_size-1)
    for permutation in reduced_permutations:
        permutation_copy = permutation.copy()
        permutation.append(0)
        permutations.append(permutation)
        permutation_copy.append(1)
        permutations.append(permutation_copy)
    return permutations

def make_function(term: list, permutation):
    term_copy = term.copy()
    for index, value in enumerate(permutation):
        symbol_to_swap = 'X'+str(index)
        replace_element(term_copy, symbol_to_swap, value)
    replace_element(term_copy, 'F', 0)
    return term_copy

def evaluate_function(function):
    if function[0] != 'implies':
        return function[0]
    function1, function2 = split_function(function[1:])
    value1 = evaluate_function(function1)
    value2 = evaluate_function(function2)
    return (value1 == 0 or value2 == 1)

def split_function(function):
    spaces = 1
    index = 0
    while (spaces > 0):
        element = function[index]
        if element == 'implies':
            spaces += 2
        spaces -= 1
        index += 1
    return (function[:index], function[index:])

def replace_element(list, current, new):
    for index, element in enumerate(list):
        if element == current:
            list[index] = new

term = ['implies', 'implies', 'X1', 'implies', 'X2', 'X0','implies','implies','X1','X2', 'implies','X1','X0']
print(is_theorem(term, 3))
    

