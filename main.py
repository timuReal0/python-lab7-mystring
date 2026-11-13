from domain import MyString
from test import run_all_tests
if __name__ == "__main__":
    run_all_tests()
    print("\n\n\n\n\n")
    # Create MyString objects
    s = MyString('')                            # empty string
    s1 = MyString('abcd')                       # 'abcd'
    print(s1)

    sr = MyString(initialize_with_random=True)  # n random lowercase letters
    print(sr)

    try:
        s2 = MyString('aBc')                    # uppercase letter not allowed
    except TypeError as e:
        print(e)

    # Access, slicing, length
    print(s1[0])                                # a
    print(s1[1:3])                              # new MyString: 'bc'
    print(len(s1))                              # 4

    # Loop over the string
    for ch in s1:
        print(ch)                               # a, b, c, d on separate lines

    # Modify a character
    s3 = MyString('akmd')
    s3[2] = 'x'                                 # content is now: 'akxd'
    try:
        s3[1] = 'A'                             # cannot add uppercase character
    except TypeError as e:
        print(e)

    # Insert a character
    s3.insert(1, 'z')                           # 'azkxd'
    s3.insert(8, 'y')                           # 8 > length, added at the end: 'azkxdy'
    print(s3)

    # Remove all occurrences of a character
    s3.remove_character('x')                    # 'azkdy'
    print(s3)
    try:
        s3.remove_character('q')                # 'q' is not in the string
    except ValueError as e:
        print(e)

    s4 = MyString('xaxbx')
    s4.remove_character('x', 1, 3)              # only between positions 1 and 3: 'xabx'
    print(s4)

    # Replace k occurrences of a substring
    s5 = MyString('abcabcabc')
    s5.replace('ab', 'xz', 2)                   # 'xzcxzcabc'
    print(s5)

    # Concatenation and repetition
    s6 = s3 + MyString('lm')                    # 'azkdylm'
    print(s6)
    s7 = s3 * 2                                 # 'azkdyazkdy'
    print(s7)

    # Rotate the string
    s3.rotate(2)                                # 'dyazk'
    print(s3)

    # Reverse a substring
    s3.reverse_substring(0, 2)                  # 'aydzk'
    print(s3)

    # Sliding windows
    print(s3.sliding_window(3, 2))              # ['ayd', 'ydz', 'dzk']

    #frequency
    print(s3.frequency())

    #BONUS
    print(MyString('ad')==MyString('bc'))
    print(MyString('ad')==MyString('xd'))