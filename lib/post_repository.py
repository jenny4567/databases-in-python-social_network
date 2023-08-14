from lib.Post import Post

class postRepository():
        def __init__(self, connection):
            self._connection = connection

            # Retrieve all post
        def all(self):
            rows = self._connection.execute('SELECT * from posts')
            post = []
            for row in rows:
                item = Post(row["id"], row["title"], row["content"], row["view_count"], row["account_id"])
                post.append(item)
            return post