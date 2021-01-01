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
#curl -X "POST" -H "Content-Type:application/json" -d "{\"Firstname\":\"james\",\"Lastname\":\"Bond\",\"Postcode\":\"F78K987\",\"Ordertype\":\"pods\"}" http://127.0.0.1:5000/coffeeconsumers
# to check it worked .. curl http://127.0.0.1:5000/coffeeconsumers
@app.route('/coffeeconsumers', methods=['POST'])
def create():
    #sanity check to make sure flask link is working
    #return "used by create method"
    coffeeconsumer = {
            #"id": request.json["nextId"],                
            "Firstname": request.json["Firstname"],
            "Lastname": request.json["Lastname"],
            "Postcode": request.json["Postcode"],
            "Ordertype": request.json["Ordertype"],
    }
    #return jsonify([])
    return jsonify(coffeedao.create(coffeeconsumer))
    #return "served by Create"
 
#update
#curl -X "PUT" -d "{\"firstname\":\"Test\",\"lastname\":\"Test\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/coffeeconsumers/1
#curl -X "PUT" -d "{\"ordertype\":\"pods\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/coffeeconsumers
#PUT FUNCTION RETURNS AN EMPTY  JSON OBJECT
@app.route('/coffeeconsumers/<int:id>', methods=['PUT'])
def update(id): 
    foundcustomers = coffeedao.findById(id)
    print(foundcustomers)
    if len(foundcustomers)==[0]:
        return jsonify({}), 404
    currentcustomers = foundcustomers
    #if 'id' in request.json:
        #currentcustomers['id'] = request.json['id']
    if 'Firstname' in request.json:
        currentcustomers['Firstname'] = request.json['Firstname']
    if 'Lastname' in request.json:
        currentcustomers['Lastname'] = request.json['Lastname']
    if 'Postcode' in request.json:
        currentcustomers['Postcode'] = request.json['Postcode']
    if 'Ordertype' in request.json:
        currentcustomers['Ordertype'] = request.json['Ordertype']

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

