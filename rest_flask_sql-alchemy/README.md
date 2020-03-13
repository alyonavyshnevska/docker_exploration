# Tools
- Flask: lightweight Python Framework
- SQL Alchemy: Orject-relational mapper. Layer that allows to interact with a database. 
- Flask-Marshmellow: for serialization of objects
- Postman: to make http requests 

For the most part if I am using REST it will return a json file. 

## Interacting with Database
### Routing: we need our endpoints
``` 
# route() decorator tells Flask what URL should trigger our function.
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'worked'}) 
```