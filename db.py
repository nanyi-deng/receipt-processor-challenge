import uuid

#create a simple in-memory database via dictionary.
#this is a simplification on the exercise. 
#in production, we should use proper db since in-memory database like this can only store small amount of data and will loss it all once the program shut down. 
db = {}

#create id according to receipt 
def store_receipt(receipt):
    #store the receipt and create unique id
    receipt_id = str(uuid.uuid4())
    db[receipt_id] = receipt
    return receipt_id

#get the receipt according to id 
def get_receipt(receipt_id):
    return db.get(receipt_id)
