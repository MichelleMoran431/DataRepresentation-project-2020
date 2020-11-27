from CoffeeExpertsDAO import coffeedao
#print ("ok")

coffeeconsumer = {
        'id': '1234',
        'firstname':'michelle',
        'lastname':'conway',
        'postcode':'F28K381'
}


coffeeconsumer2 = {
        'id': '4567',
        'firstname':'James',
        'lastname':'Moran',
        'postcode':'F28K382'
}
#returnvalue = coffeedao.create(coffeeconsumer)
returnValue =coffeedao.getAll()
print(returnValue)
returnValue =coffeedao.findById(coffeeconsumer2['id'])
print("find By Id")
print(returnValue)
returnValue =coffeedao.update(coffeeconsumer2)
print(returnValue)
returnValue =coffeedao.findById(coffeeconsumer2['id'])
print(returnValue)
returnValue =coffeedao.delete(coffeeconsumer2['id'])
print(returnValue)
returnValue =coffeedao.getAll()
print(returnValue)