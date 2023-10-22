from hello_tjkpolisher.who import my_name, who, print_name
from hello_tjkpolisher.randomness import lotto_kr

def test_my_name():
    my_name()
    
def test_who():
    who()
    
def test_print_name():
    print_name("tester")
    
def test_lotto_kr():
    lotto_kr()