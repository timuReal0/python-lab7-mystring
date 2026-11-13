# MyString – a Mutable Lowercase String Class

A Python class that behaves like a string, but only allows lowercase English letters and,
unlike Python's `str`, can be modified in place.
Written for Lab 7 of an introductory programming course, to practice classes,
special (magic) methods, exception handling and test-driven development.

## Operations

| Operation | Usage |
|-----------|-------|
| Create from text | `MyString('abcd')` |
| Create from 1 to 10 random letters | `MyString(initialize_with_random=True)` |
| Access a character | `s[0]` |
| Modify a character | `s[2] = 'x'` |
| Slicing (returns a new MyString) | `s[1:3]` |
| Length | `len(s)` |
| Loop over the characters | `for ch in s:` |
| Concatenation | `s1 + s2` |
| Repetition | `s * 3` |
| Insert a character (added at the end if the position is too large) | `s.insert(1, 'z')` |
| Remove all occurrences of a character, optionally between two positions | `s.remove_character('x', start, end)` |
| Position of the first occurrence of a substring, or -1 | `s.find('bc')` |
| Replace the first k occurrences of a substring, in place | `s.replace('ab', 'xz', 2)` |
| Rotate to the right by k positions | `s.rotate(2)` |
| Reverse a substring (end included) | `s.reverse_substring(0, 2)` |
| Sliding windows of a given size and overlap | `s.sliding_window(3, 2)` |
| Number of occurrences of each character | `s.frequency()` |
| Display the string and the character at each position | `print(s)` |

**Bonus:** two MyStrings are equal when the sums of the codes of their characters are equal,
so `MyString('ad') == MyString('bc')` is `True`.

## Validation

Only the letters a–z are accepted. Adding any other character raises a `TypeError`,
and invalid arguments raise a `ValueError` (for example, removing a character
that is not in the string).

## Example

```python
s = MyString('akmd')
s[2] = 'x'                  # akxd
s.insert(1, 'z')            # azkxd
s.insert(8, 'y')            # azkxdy  (8 is past the end)
s.remove_character('x')     # azkdy
s.rotate(2)                 # dyazk
s.reverse_substring(0, 2)   # aydzk
s.sliding_window(3, 2)      # ['ayd', 'ydz', 'dzk']
```

```
>>> print(MyString('ab'))
ab
Character at position 0: a
Character at position 1: b
```

## Project structure

| File | Contents |
|------|----------|
| `domain.py` | The `MyString` class |
| `test.py` | Tests written with `assert` for every operation |
| `main.py` | Runs the tests, then demonstrates all the operations |

## How to run

Requires Python 3.

```
python main.py
```

To run only the tests:

```
python test.py
```
