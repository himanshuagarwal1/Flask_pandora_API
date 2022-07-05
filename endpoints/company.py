from flask_restful import Resource, fields,  marshal
from Models.Data_models import Company, People



people_fields ={
    "index" : fields.Integer,
    "name" : fields.String,
}

# Driver code for finding all employees of a company
class CompanyResource(Resource):
    def get(self, name0=None):        
        if name0:
            data = Company.query.filter_by(company=name0).first()
            data = People.query.filter_by(company_id =  data.index).all()
            if not data:
                return "No Associated Employees found", 404            
            return marshal(data, people_fields) , 200
        else:
            return "No company found", 404
