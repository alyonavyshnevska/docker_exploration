from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import os 
import markdown
import shelve

# Creating an app (an instance of Flask)
app = Flask(__name__)

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("products.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    "Show documentation file"

    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        #Convert to HTML
        return markdown.markdown(content)

class ProductList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        products = []

        for key in keys:
            products.append(shelf[key])

        return {'message:': 'Success', 'data': products}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('product_type', required=True)
        
        #Parse args into object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Product registered', 'data': args}, 201

class Product(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'messsage': 'Product not found', 'data': {}}, 404
        
        return {'message': 'Product found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()
        if not (identifier in shelf):
            return {'messsage': 'Product not found', 'data': {}}, 404        

        del shelf[identifier]
        return '', 204

api.add_resource(ProductList, '/products')
api.add_resource(Product, '/product/<string:identifier>')

