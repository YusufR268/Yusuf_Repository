from plates import length
from plates import alphanum
from plates import first_char
from plates import zero_num
from plates import is_valid


# def test_first_char():
#     assert first_char('AAAA') == True
#     assert first_char('1AAA') == False
#     assert first_char('A1AA') == False
#     assert first_char('45') == False

# def test_len():
#     assert length('AAA777') == True
#     assert length('AA0') == True
#     assert length('AAAAA854') == False
#     assert length('A') == False

# def test_mid():
#     assert zero_num('AAA963') == True
#     assert zero_num('AA52R') == False
#     assert zero_num('AAA3IL') == False

# def test_zero_place():
#     assert zero_num('AAA401') == True
#     assert zero_num('AA700') == True
#     assert zero_num('AA052') == False
#     assert zero_num('AAA001') == False

# def test_alnum():
#     assert alphanum('AAA963') == True
#     assert alphanum('AA/@') == False
#     assert alphanum('AA !') == False

# def test_is_valid():
#     assert is_valid('AAA963') == True
#     assert is_valid('AA740') == True
#     assert is_valid('HELLO') == True
#     assert is_valid('AA/@') == False
#     assert is_valid('AA047') == False
#     assert is_valid('A') == False

def test_2letters():
    assert is_valid('AAA963') == True

def test_2letters2():
    assert is_valid('A9') == False

def test_max_char():
    assert is_valid('WORLD') == True

def test_max_char2():
    assert is_valid('HEYWORLD') == False

def test_num_place():
    assert is_valid('AAA963') == True

def test_num_place2():
    assert is_valid('AA96S') == False

def test_zero_place():
    assert is_valid('AAA603') == True

def test_zero_place2():
    assert is_valid('AAA063') == False

def test_alphanum():
    assert is_valid('AAA963') == True

def test_alphanum2():
    assert is_valid('AA 63') == False
