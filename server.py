from flask import Flask, jsonify, request, abort,url_for,redirect
from CoffeeExpertsDAO import coffeedao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#app = Flask(__name__)

#@app.route('/')
#def index():
   #return "Hello, World!"

#curl "http://127.0.0.1:5000/coffeeconsumers"
@app.route('/coffeeconsumers')
def getAll():
    #print("in getall")
    #results =coffeedao.getAll()
    #return jsonify(results)
    return jsonify(coffeedao.getAll())


#curl "http://127.0.0.1:5000/coffeeconsumers/2"
@app.route('/coffeeconsumers/<int:id>')
def findById(id):
    #foundcustomers = coffeedao.findById(id)
    #return jsonify({foundcustomers})
    return jsonify(coffeedao.findById(id))

#create a new entry into the database
#curl -X "POST" -H "Content-Type:application/json" -d "{\"firstname\":\"juuu\",\"lastname\":\"test\",\"postcode\":\"test\"}" http://127.0.0.1:5000/coffeeconsumers
# to check it worked .. curl http://127.0.0.1:5000/coffeeconsumers
@app.route('/coffeeconsumers', methods=['POST'])
def create():
    #sanity check to make sure flask link is working
    #return "used by create method"
    coffeeconsumer = {
            #"id": request.json["nextId"],                
            "firstname": request.json["firstname"],
            "lastname": request.json["lastname"],
            "postcode": request.json["postcode"],
    }
    #return jsonify([])
    return jsonify(coffeedao.create(coffeeconsumer))
    #return "served by Create"
 
#update
#curl -X "PUT" -d "{\"firstname\":\"Test\",\"lastname\":\"Test\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/coffeeconsumers/1
#PUT FUNCTION RETURNS AN EMPTY  JSON OBJECT
@app.route('/coffeeconsumers/<int:id>', methods=['PUT'])
def update(id): 
    foundcustomers = coffeedao.findById(id)
    print(foundcustomers)
    if len(foundcustomers)==[0]:
        return jsonify({}), 404
    currentcustomers = foundcustomers
    #if 'id' in request.json:
       # currentcustomers['id'] = request.json['id']
    if 'firstname' in request.json:
        currentcustomers['firstname'] = request.json['firstname']
    if 'lastname' in request.json:
        currentcustomers['lastname'] = request.json['lastname']
    if 'postcode' in request.json:
        currentcustomers['postcode'] = request.json['postcode']

    coffeedao.update(currentcustomers)
    return jsonify(currentcustomers)


#delete 
#curl -X DELETE http://127.0.0.1:5000/coffeeconsumers/1
@app.route('/coffeeconsumers/<int:id>',methods=['DELETE'])
def delete(id):
    coffeedao.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)

