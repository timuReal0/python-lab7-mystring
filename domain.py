import random
import string


class MyString:
    #BONUS
    def __eq__(self, other):
        first_sum=0
        other_sum=0
        for ch in self._chars:
            first_sum+=ord(ch)
        for ch in other._chars:
            other_sum+=ord(ch)
        return first_sum==other_sum


    def __init__(self, text='', initialize_with_random=False):
        """
        Creates a new MyString from the given text, or from n random lowercase letters
        (n between 1 and 10) if initialize_with_random is True.
        """
        if initialize_with_random:
            n = random.randint(1, 10)
            self._chars = []
            for i in range(n):
                self._chars.append(random.choice(string.ascii_lowercase))
        else:
            for ch in text:
                self._validate(ch)
            self._chars = list(text)

    def _validate(self, ch):
        """
        Raises TypeError if ch is not a single lowercase English letter.
        """
        if not isinstance(ch, str) or len(ch) != 1 or ch not in string.ascii_lowercase:
            raise TypeError(f"'{ch}' is not a lowercase letter")

    def __str__(self):
        """
        Returns the string on the first line, then the character at each position.
        """
        lines = [''.join(self._chars)]
        i = 0
        for ch in self._chars:
            lines.append(f"Character at position {i}: {ch}")
            i += 1
        return '\n'.join(lines)

    def __getitem__(self, key):
        """
        Returns the character at the given position, or a new MyString for a slice.
        """
        result = self._chars[key]
        if isinstance(key, slice):
            return MyString(result)
        return result

    def __setitem__(self, key, value):
        """
        Replaces the character at the given position (only lowercase letters allowed).
        """
        self._validate(value)
        self._chars[key] = value

    def __len__(self):
        """
        Returns the number of characters.
        """
        return len(self._chars)

    def __iter__(self):
        """
        Allows looping over the characters.
        """
        return iter(self._chars)

    def __add__(self, other):
        """
        Returns a new MyString made of this string followed by the other one.
        """
        if isinstance(other, MyString):
            return MyString(self._chars + other._chars)
        raise TypeError("Can only add a MyString to a MyString")

    def __mul__(self, n):
        """
        Returns a new MyString made of this string repeated n times.
        """
        if isinstance(n, int):
            return MyString(self._chars * n)
        raise TypeError("Can only multiply a MyString by an int")

    def insert(self, pos, ch):
        """
        Inserts a character at the given position; if the position is past the end,
        the character is added at the end.
        """
        if pos < 0:
            raise ValueError("Position cannot be negative")
        self._validate(ch)
        if pos > len(self) - 1:
            self._chars.append(ch)
        else:
            self._chars.insert(pos, ch)

    def remove_character(self, ch, start=0, end=-1):
        """
        Removes all occurrences of a character between start and end (included);
        raises ValueError if there is nothing to remove.
        """
        if end == -1:
            end = len(self) - 1
        remained = []
        for i in range(len(self._chars)):
            if i < start or i > end:
                remained.append(self._chars[i])
            else:
                if self._chars[i] != ch:
                    remained.append(self._chars[i])
        if len(self._chars) == len(remained):
            raise ValueError(f"'{ch}' is not in the string")
        self._chars = remained

    def replace(self, old, new, k):
        """
        Replaces the first k occurrences of a substring with another one, in place.
        """
        for ch in new:
            self._validate(ch)
        result = []
        i = 0
        replaced = 0
        while i < len(self._chars):
            if replaced < k and self._chars[i:i + len(old)] == list(old):
                result.extend(new)
                i += len(old)
                replaced += 1
            else:
                result.append(self._chars[i])
                i += 1
        self._chars = result

    def rotate(self, k):
        """
        Rotates the string to the right by k positions.
        """
        if len(self._chars) == 0:
            return
        k = k % len(self._chars)
        self._chars = self._chars[-k:] + self._chars[:-k]

    def reverse_substring(self, start, end):
        """
        Reverses the characters between start and end (end included).
        """
        self._chars[start:end + 1] = self._chars[start:end + 1][::-1]

    def sliding_window(self, size, overlap):
        """
        Returns the list of substrings of the given size, where consecutive ones share
        `overlap` characters; the last one may be shorter.
        """
        if size <= 0 or overlap < 0 or overlap >= size:
            raise ValueError("size must be > 0 and 0 <= overlap < size")
        step = size - overlap
        windows = []
        start = 0
        while start < len(self._chars):
            windows.append(''.join(self._chars[start:start + size]))
            if start + size >= len(self._chars):
                break
            start += step
        return windows

    def frequency(self):
        """
        Returns a dictionary with the number of occurrences of each character.
        """
        freq = {}
        for ch in self._chars:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        return freq