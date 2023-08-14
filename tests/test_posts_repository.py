from lib.post_repository import postRepository
from lib.Post import Post

"""
When we call postRepository#all
We get a list of post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = postRepository(db_connection) # Create a new postRepository
    posts = repository.all() # Get all posts

    # Assert on the results
    assert posts == [
        Post(1, 'Title 1', 'some content', 50, 1),
        Post(2, 'Title 2', 'some more content', 21, 1),
        Post(3, 'Title 3', 'even more content', 104324, 2)
    ]