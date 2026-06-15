# Problem Set 4A
# Name: Tanisha Nimkar
# Collaborators: NA

def get_permutations(sequence):
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
        return [sequence]
    
    first_char = sequence[0]
    rest = sequence[1:]

    smaller_perms = get_permutations(rest)

    result = []

    for perm in smaller_perms:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + first_char + perm[i:]
            result.append(new_perm)
    
    return result

if __name__ == '__main__':
    print("Test Case 1")
    print("Input: 'a'")
    print("Expected Output: ['a']")
    print(f"Actual Output: {get_permutations('a')}")

    print()

    print("Test Case 2")
    print("Input: 'ab'")
    print("Expected Output: ['ab', 'ba']")
    print(f"Actual Output: {get_permutations('ab')}")

    print()

    print("Test Case 3")
    print("Input: 'abc'")
    print("Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']")
    print(f"Actual Output: {get_permutations('abc')} ")



#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
