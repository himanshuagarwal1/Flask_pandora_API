from data import db

# People data model
class People(db.Model):
    __tablename__ = 'People'
    id = db.Column(db.Integer, primary_key=True)     
    index= db.Column(db.Integer)    
    has_died= db.Column(db.Boolean())
    age= db.Column(db.Integer) 
    eyeColor= db.Column(db.String(20))  
    name= db.Column(db.String(20)) 
    gender= db.Column(db.String(20)) 
    company_id= db.Column(db.Integer)   
    phone= db.Column(db.String(20)) 
    address= db.Column(db.Text) 
    friends= db.Column(db.Text) 
    favouritefruit= db.Column(db.Text)
    favouritevegetable= db.Column(db.Text) 


    def __repr__(self):
        return 'Id: {}, name:{}'.format(self.id, self.name)

    def getPerson(name0):
        return People.query.filter_by(name=name0).first()

# Company data model
class Company(db.Model):
    __tablename__ = "Company"
    id = db.Column(db.Integer, primary_key = True)
    index= db.Column(db.Integer) 
    company = db.Column(db.String(20))

    def __repr__(self):
        return 'Index: {}, company:{}'.format(self.index, self.company)
