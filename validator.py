from google.cloud.firestore_v1.base_query import FieldFilter
def validateParameter(ref,atribute,value,atribute2=None,value2=None):
    if atribute2==None:
        result=ref.where(filter=FieldFilter(atribute,"==",value)).stream()
    else:
        result=ref.where(filter=FieldFilter(atribute,"==",value)).where(filter=FieldFilter(atribute2,"==",value2)).stream()
    cc=0
    for r in result:
        cc=cc+1
    if cc==0:
        return True
    return False

userSchema  = {
    "type":"object",
    "properties":{
        "email":{"type":"string"},
        "money":{"type":"string"},
        "name":{"type":"string"},
        "password":{"type":"string"}
    },
    "required":["email",'money','name','password'],
    "additionalProperties": False
}
userSchemaUpdate  = {
    "type":"object",
    "properties":{
        "id":{"type":"string"},
        "email":{"type":"string"},
        "money":{"type":"string"},
        "name":{"type":"string"},
        "password":{"type":"string"},
        "confirm":{"type":"string"}
    },
    "required":['id',"email",'money','name','password','confirm'],
    "additionalProperties": False
}
incomeSchema  = {
    "type":"object",
    "properties":{
        "amount":{"type":"number"},
        "createdAt":{"type": "string",
                    "format": "date-time"},
        "source":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["amount",'createdAt','source','user'],
    "additionalProperties": False
}
incomeSchemaUpdate  = {
    "type":"object",
    "properties":{
        "id":{"type":"string"},
        "amount":{"type":"number"},
        "createdAt":{"type": "string",
                    "format": "date-time"},
        "source":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["id","amount",'createdAt','source','user'],
    "additionalProperties": False
}
expenseSchema  = {
    "type":"object",
    "properties":{
        "amount":{"type":"number"},
        "createdAt":{"type": "string",
                    "format": "date-time"},
        "category":{"type":"string"},
        "description":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["amount",'createdAt','category','description','user'],
    "additionalProperties": False
}
expenseSchemaUpdate  = {
    "type":"object",
    "properties":{
        "id":{"type":"string"},
        "amount":{"type":"number"},
        "createdAt":{"type": "string",
                    "format": "date-time"},
        "category":{"type":"string"},
        "description":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["id","amount",'createdAt','category','description','user'],
    "additionalProperties": False
}

categorySchema  = {
    "type":"object",
    "properties":{
        "amount":{"type":"number"},
        "category":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["amount",'category','user'],
    "additionalProperties": False
}
categorySchemaUpdate  = {
    "type":"object",
    "properties":{
        "id":{"type":"string"},
        "amount":{"type":"number"},
        "category":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["id","amount",'category','user'],
    "additionalProperties": False
}

sourceSchema  = {
    "type":"object",
    "properties":{
        "source":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["amount",'source','user'],
    "additionalProperties": False
}
sourceSchemaUpdate  = {
    "type":"object",
    "properties":{
        "id":{"type":"string"},
        "source":{"type":"string"},
        "user":{"type":"string"}
    },
    "required":["id","amount",'source','user'],
    "additionalProperties": False
}