from flask_restful import Resource, fields,  marshal
from Models.Data_models import People
import json


two_people_fields={
    "index" : fields.Integer,    
    "age" : fields.Integer,    
    "name" : fields.String,
    "phone" : fields.String, 
    "address" : fields.String,
    
}

# Driver code for finding commom frind of given 2 people
class PeopleResource2(Resource):
    def str_to_list(self,data):
        data = data.friends
        data = data.replace("[","")
        data = data.replace("]", "")
        data = data.split(",")
        return data    

    def get(self, name0, name01):

        if name0 and name01:
        
            name1 = name0.replace("_"," ")
            name2 =  name01.replace("_"," ")            
            data1 = People.getPerson(name1)
            lisA = self.str_to_list(data1)            
            data2 = People.getPerson(name2)            
            lisB  = self.str_to_list(data2)            
            lis= [i  for i in lisA if i in lisB]
            lisA =[]

            for i in lis:
                j = i.replace("'", "\"")
                j = json.loads(j)
                x= People.query.filter( People.index == j["index"] , People.has_died == False  ,People.eyeColor == "brown").first()
                if x:
                    lisA.append(marshal(x, two_people_fields))                
            return lisA , 200
            

        