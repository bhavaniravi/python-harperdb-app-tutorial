import harperdb
import os

db = harperdb.HarperDB(
    url=os.environ["DB_URL"],
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"])

schema = f"book_repo"


class BookModel:
    table = "books"
    def create(self, book_list):
        return db.insert(schema, self.table, book_list)
    
    def update(self, book_list):
        return db.update(schema, self.table, params)

    def delete(self, id):
        return db.delete(schema, self.table, [id])
    
    def get(self, id):
        return db.search_by_hash(schema, self.table, [id], get_attributes=['*'])

    def get_all(self):
        return db.sql(f"select book_name, author, pages from {schema}.{self.table}")