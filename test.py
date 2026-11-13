from domain import *

def content(s):
    return ''.join(s)

def test_init():
    s = MyString('')
    assert content(s) == ''
    assert len(s) == 0

    s = MyString()
    assert content(s) == ''

    s = MyString('abcd')
    assert content(s) == 'abcd'
    assert len(s) == 4

    try:
        MyString('aBc')
        assert False
    except TypeError:
        pass

def test_init_random():
    for _ in range(10):
        s = MyString(initialize_with_random=True)
        assert 1 <= len(s) <= 10
        for ch in s:
            assert 'a' <= ch <= 'z'

def test_validate():
    s = MyString('')
    for ch in ['a', 'm', 'z']:
        try:
            s._validate(ch)         
        except TypeError:
            assert False         

    for ch in ['A', 'Za', '1',['a']]:
        try:
            s._validate(ch)
            assert False
        except TypeError:
            pass

def test_str():
    s = MyString('ab')
    assert str(s) == 'ab\nCharacter at position 0: a\nCharacter at position 1: b'
    s = MyString('z')
    assert str(s) == 'z\nCharacter at position 0: z'
    s = MyString('')
    assert str(s) == ''


def test_getitem():
    s = MyString('abcd')
    assert s[0] == 'a'
    assert s[3] == 'd'
    assert s[-1] == 'd'
    assert s[-4] == 'a'

    sub = s[1:3]
    assert isinstance(sub, MyString)
    assert content(sub) == 'bc'
    assert content(s[:2]) == 'ab'
    assert content(s[2:2]) == ''

    try:
        s[4]
        assert False
    except IndexError:
        pass

def test_setitem():
    s = MyString('akmd')
    s[2] = 'x'
    assert content(s) == 'akxd'
    s[0] = 'z'
    assert content(s) == 'zkxd'
    s[-1] = 'y'
    assert content(s) == 'zkxy'

    for ch in ['A', '1', 3]:
        try:
            s[1] = ch
            assert False
        except TypeError:
            pass

def test_len():
    assert len(MyString('')) == 0
    assert len(MyString('a')) == 1
    assert len(MyString('abcd')) == 4


def test_add():
    s1 = MyString('azkdy')
    s2 = MyString('lm')
    s3 = s1 + s2
    assert isinstance(s3, MyString)
    assert content(s3) == 'azkdylm'
    assert content(s1) == 'azkdy'
    assert content(s2) == 'lm'
    assert content(s1 + MyString('')) == 'azkdy'

    for other in ['lm', 5, ['a']]:
        try:
            s1 + other
            assert False
        except TypeError:
            pass


def test_mul():
    s = MyString('azkdy')
    s2 = s * 2
    assert isinstance(s2, MyString)
    assert content(s2) == 'azkdyazkdy'
    assert content(s) == 'azkdy'

    assert content(s * 1) == 'azkdy'
    assert content(s * 3) == 'azkdyazkdyazkdy'
    assert content(s * 0) == ''
    assert content(MyString('') * 5) == ''

    for n in [2.0, '2', None]:
        try:
            s * n
            assert False
        except TypeError:
            pass

def test_insert():
    s = MyString('akxd')
    s.insert(1, 'z')     
    assert content(s) == 'azkxd'


    s.insert(0, 'b')                    
    assert content(s) == 'bazkxd'
    s.insert(8, 'y')              
    assert content(s) == 'bazkxdy'
    s.insert(len(s), 'w')                
    assert content(s) == 'bazkxdyw'

    s = MyString('abc')
    try:
        s.insert(-1, 'x')
        assert False
    except ValueError:
        pass
    assert content(s) == 'abc'

    for ch in ['X', '1', 'xy', '']:
        try:
            s.insert(1, ch)
            assert False
        except TypeError:
            pass
    assert content(s) == 'abc'


def test_remove_character():
    s = MyString('azkxdy')
    s.remove_character('x')
    assert content(s) == 'azkdy'

    s = MyString('xaxbx')
    s.remove_character('x', 1, 3)
    assert content(s) == 'xabx'


    s = MyString('xaxbx')
    s.remove_character('x', start=2)
    assert content(s) == 'xab'

    s = MyString('aaa')
    s.remove_character('a')
    assert content(s) == ''

    s = MyString('azkdy')
    try:
        s.remove_character('q')
        assert False
    except ValueError:
        pass
    assert content(s) == 'azkdy'

    s = MyString('xabx')
    try:
        s.remove_character('x', 1, 2)
        assert False
    except ValueError:
        pass
    assert content(s) == 'xabx'

    try:
        MyString('').remove_character('a')
        assert False
    except ValueError:
        pass

def test_replace():
    s = MyString('abcabcabc')
    s.replace('ab', 'xz', 2)
    assert content(s) == 'xzcxzcabc'

    s = MyString('abcabc')
    s.replace('ab', 'xz', 0)
    assert content(s) == 'abcabc'

    s = MyString('abcabc')
    s.replace('abc', 'x', 1)
    assert content(s) == 'xabc'

    s = MyString('abcabc')
    s.replace('b', '', 2)
    assert content(s) == 'acac'

    s = MyString('abcabc')
    try:
        s.replace('ab', 'XY', 1)
        assert False
    except TypeError:
        pass
    assert content(s) == 'abcabc'

def test_rotate():
    s = MyString('azkdy')
    s.rotate(2)
    assert content(s) == 'dyazk'

    s = MyString('abcd')
    s.rotate(0)
    assert content(s) == 'abcd'
    s.rotate(4)
    assert content(s) == 'abcd'

    s = MyString('')
    s.rotate(3)
    assert content(s) == ''



def test_reverse_substring():
    s = MyString('dyazk')
    s.reverse_substring(0, 2)
    assert content(s) == 'aydzk'

    s = MyString('abcdef')
    s.reverse_substring(0, 5)
    assert content(s) == 'fedcba'

    s = MyString('abcdef')
    s.reverse_substring(2, 2)
    assert content(s) == 'abcdef'


def test_sliding_window():
    s = MyString('aydzk')
    assert s.sliding_window(3, 2) == ['ayd', 'ydz', 'dzk']

    assert s.sliding_window(2, 0) == ['ay', 'dz', 'k']

    assert s.sliding_window(1, 0) == ['a', 'y', 'd', 'z', 'k']

    assert s.sliding_window(5, 0) == ['aydzk']

    assert MyString('').sliding_window(3, 1) == []
    try:
        s.sliding_window(3 , -1)
        assert False
    except ValueError:
        pass

def test_frequency():
    assert MyString('abra').frequency() == {'a': 2, 'b': 1, 'r': 1}
    assert MyString('abc').frequency() == {'a': 1, 'b': 1, 'c': 1}
    assert MyString('zzz').frequency() == {'z': 3}
    assert MyString('').frequency() == {}


def test_eq(): #BONUS
    assert MyString('ad') == MyString('bc')
    assert MyString('abc') == MyString('cba')
    assert MyString('') == MyString('')

    assert MyString('a') != MyString('x')
    assert MyString('a') != MyString('')

def run_all_tests():
    test_init()
    test_init_random()
    test_validate()
    test_str()
    test_getitem()
    test_setitem()
    test_len()
    test_add()
    test_mul()
    test_insert()
    test_remove_character()
    test_replace()
    test_rotate()
    test_reverse_substring()
    test_sliding_window()
    test_eq()
    print("All tests passed!")


if __name__ == "__main__":
    run_all_tests()