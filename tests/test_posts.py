from lib.Post import Post

def test_post_constructs():
    post1 = Post(1, 'my title', 'my content', 2, 3)

    assert post1.id == 1
    assert post1.title == 'my title'
    assert post1.content == 'my content'
    assert post1.view_count == 2
    assert post1.account_id == 3

def test_equlity():
    post1 = Post(1, 'my title', 'my content', 2, 3)
    post2 = Post(1, 'my title', 'my content', 2, 3)
    assert post1 == post2

def test_print_format():
    post1 = Post(1, 'my title', 'my content', 2, 3)
    assert str (post1) == "1 - my title - my content - 2 - 3"