from lib.accounts import Account

'''
accounts table:
id: serial
email address text
username text
'''

def test_accounts_constructs():
    accounts1 = Account(1, 'fishy@gmail.com', 'fishy_the_fish')

    assert accounts1.id == 1
    assert accounts1.email == 'fishy@gmail.com'
    assert accounts1.username == 'fishy_the_fish'

def test_equlity():
    accounts1 = Account(1, 'fishy@gmail.com', 'fishy_the_fish')
    accounts2 = Account(1, 'fishy@gmail.com', 'fishy_the_fish')
    assert accounts1 == accounts2

def test_print_format():
    accounts1 = Account(1, 'fishy@gmail.com', 'fishy_the_fish')
    assert str (accounts1) == "Account 1 - fishy@gmail.com - fishy_the_fish"