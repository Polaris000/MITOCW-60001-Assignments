# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
list_to_return = []

get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    

    if len(sequence) == 1:
        return list(sequence)

    else:
        init_char = sequence[0]

        copy_str = sequence[1:]

        for i in get_permutations(copy_str):

            for j in range(0, len(copy_str) + 1):
                x_temp = list(i[:])
                
                x_temp.insert(j, init_char)
               

                list_to_return.append("".join(x_temp))
                

            if (i in list_to_return):
                list_to_return.remove(i)


    return list_to_return            


    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations("abc"))
