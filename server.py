from flask import Flask, jsonify, request, abort
from CoffeeExpertsDAO import coffeedao

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
   return "Hello, World!"

#curl "http://127.0.0.1:5000/coffeeconsumers"
@app.route('/coffeeconsumers')
def getAll():
    print("in getall")
    results = coffeedao.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/coffeeconsumers/2"
@app.route('/coffeeconsumers/<int:id>')
def findById(id):
    foundcustomer = coffeedao.findById(id)

    return jsonify(foundcustomer)

#create a new entry into the database
#curl -X "POST" -H "Content-Type:application/json" -d "{\"firstname\":\"test\",\"lastname\":\"test\",\"postcode\":\"test\"}" http://127.0.0.1:5000/coffeeconsumers
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
    return jsonify(coffeedao.create(coffeeconsumer))
    return "served by Create"
 
#update
#curl -X "PUT" -d "{\"firstname\":\"Test\",\"lastname\":\"Test\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/coffeeconsumers/1
#PUT FUNCTION RETURNS AN EMPTY  JSON OBJECT
@app.route('/coffeeconsumers/<int:id>', methods=['PUT'])
def update(id): 
    #sanity check to make sure flask link is working
    #return "used by update method"
    #foundcustomers = []
    #foundcustomers = coffeedao.findById(id)
    foundcustomers = coffeedao.findById(id)
    print (foundcustomers)
    if len(foundcustomers)==[]:
        return jsonify({}), 404
    currentcustomers = foundcustomers
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

    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)

