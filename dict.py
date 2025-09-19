info = {
    "name" : "Anjaney",
    "subject" : ["C", "C++", "Javascript" , "python"],
    "age" :20,
    "isPass" : True,
    23 : 24,
}

print(info)

info["name"] = "Prajwal" #overwrite
info["surname"] = "Naik"  #add new key to dict(info)

print(info)


#Methods in dictionary

all = info.keys()     #return all keys
print(all)

values = info.values()   #return all values
print(values)

items = info.items()   #print both keys and values in th form of tupels pair
print(items)

specific = info.get("age")
print(specific)