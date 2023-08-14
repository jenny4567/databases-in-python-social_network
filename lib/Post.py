class Post():
    def __init__(self, id, title, content, view_count, account_id):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count
        self.account_id = account_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id} - {self.title} - {self.content} - {self.view_count} - {self.account_id}"
    
    