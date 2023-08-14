from lib.accounts import Account

'''
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username text
'''

class accountRepository():
        def __init__(self, connection):
            self._connection = connection

            # Retrieve all account
        def all(self):
            rows = self._connection.execute('SELECT * from accounts')
            account = []
            for row in rows:
                item = Account(row["id"], row["email_address"], row["username"])
                account.append(item)
            return account