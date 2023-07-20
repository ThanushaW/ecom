from flask import Flask,request,jsonify
import sqlite3
app = Flask(__name__)


# book_list = [
#     {
#         "id":0,
#         "author":"Thanusha Wijesinghe",
#         "language":"Sinhala",
#         "title":"Wanaraya"
#     },
#     {
#         "id":1,
#         "author":"Nipuni Wijekoon",
#         "language":"English",
#         "title":"50 Shades of Gray"
#     },
#     {
#         "id":2,
#         "author":"Malith De Silva",
#         "language":"Tamil",
#         "title":"Blah Blah"
#     }
# ]

def db_connection():
    conn =None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route('/')
def index():
    return "Hello world"


@app.route('/books',methods=['GET','POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        result = cursor.execute("SELECT * FROM book")
        books = [
            dict(id=row[0], author=row[1],language=row[2],title=row[3])
            for row in result.fetchall()
        ]
        if books is not None:
            return jsonify(books), 200
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['langauge']
        new_title = request.form['title']
        
        sql = "INSERT INTO book (author,langauge,title) VALUES (?,?,?)"
        result = cursor.execute(sql,(new_author,new_language,new_title))
        conn.commit()
        return f"Book with the id {cursor.lastrowid} created successfully", 201


@app.route('/books/<int:id>',methods=['GET','PUT','DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        result = cursor.execute("SELECT * FROM book WHERE id=?",(id,))
        rows = cursor.fetchall()
        for r in rows: book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong",404
            
    elif request.method == 'PUT':
        sql = """UPDATE book
        SET title=?,
        author=?
        langauge=?
        WHERE id=?"""
        result = cursor.execute(sql,(request.form['title'],request.form['author'],request.form['langauge'],id))
        conn.commit
        return f"Book with the id {id} updated successfully", 201
            
    elif request.method == 'DELETE':
        sql = """DELETE FROM book
        WHERE id=?"""
        result = cursor.execute(sql,(id,))
        for i,book in enumerate(book_list):
            if book['id'] == id:
                book_list.pop(i)
                return jsonify(book_list)


@app.route('/<name>')
def print_name(name):
    return f'Hi, {name}'



if __name__ =='__main__':
    app.run(debug=True)