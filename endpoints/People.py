from flask_restful import Resource, fields,  marshal
from Models.Data_models import  People

One_people_fields = {
    "index" : fields.Integer,
    "name" : fields.String, 
    "age" : fields.Integer, 
    "favouritefruit" : fields.String,
    "favouritevegetable" : fields.String,
}

people_list_fields = {
    'count': fields.Integer,
    'number': fields.List(fields.Nested(One_people_fields)),
}

# Driver code to give details for a person
class PeopleResource(Resource):
    def get(self, first=None, last=None):        
        if first:
            if last:
                name0 = first +" "+ last
            else:        
                name0 = first
            data = People.getPerson(name0)
            return marshal(data, One_people_fields), 200
        else:
            return "Valid names are required", 404 