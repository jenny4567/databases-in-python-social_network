from lib.account_repository import accountRepository
from lib.accounts import Account

'''
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username text
'''

"""
When we call accountRepository#all
We get a list of account objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = accountRepository(db_connection) # Create a new accountRepository
    accounts = repository.all() # Get all accounts

    # Assert on the results
    assert accounts == [
        Account(1, '1234@gmail.com', '1234'),
        Account(2, '5678@gmail.com', '5678')
    ]