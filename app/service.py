from models import BookModel

class BookService:
    def __init__(self):
        self.model = BookModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, item_id, params):
        if isinstance(params, dict):
            params = [params]

        for param in params:
            param["id"] = item_id
        
        return self.model.update(params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def get_all(self):
        response = self.model.get_all()
        return response
    
    def get(self, book_id):
        response = self.model.get(book_id)
        return response

    def add_notes(self, item_id, notes):
        if isinstance(notes, dict):
            notes = [notes]
        return self.update(item_id, {"notes":notes})