from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from sqlalchemy import text
import os 


app = Flask(__name__)
'sqlite:///' + os.path.join(os.path.dirname(__file__), 'mydatabase.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'bookstore.db')
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    availability = db.Column(db.Integer)
    description = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String) 
    def __init__(self, id, title, availability, description, category, price):
        self.id = id
        self.title = title
        self.availability = availability
        self.description = description
        self.category = category
        self.price = price
        self.image = image

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)
    total_price= db.Column(db.Integer)
    shipping_address = db.Column(db.String)
    
    def __init__(self, id, item, total_price, shipping_address):
        self.id = id
        self.item = item
        self.total_price = total_price
        self.shipping_address = shipping_address
        
class Order_Details(db.Model):
    __tablename__ = 'order_detail'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    
   
    def __init__(self, order_id, book_id, item):
        self.order_id = order_id
        self.book_id = book_id
        self.id = id
            

with app.app_context():
    try:
        db.session.execute(text('SELECT * from books'))
        print("Database connection successful!")
    except Exception as e:
        print("Failed to connect to the database:", str(e))

# sqlilite 3 books 


@app.route('/')
def index():
    books = Book.query.all()
    name = "Online Book Store"  
    categories = ['Categories'] 
    return render_template('home.html', name=name, categories=categories, books=books)




@app.route('/books/<int:book_id>')
def getBook(book_id):
   book = Book.query.get(book_id) 
   return render_template('detail.page.html', book=book)


@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')

@app.route('/order', methods=['POST'])
def createOrder():
    json_data = request.get_json()
    print(json_data)
    return(make_response('success')) 

if __name__ == '__main__':
    app.run()

   