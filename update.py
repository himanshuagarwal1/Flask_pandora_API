import json

from data import db
from Models.Data_models import People , Company

c = open('companies.json')
p = open('people.json')

data_companies = json.load(c)
data_people = json.load(p)



fruits = ['orange', 'apple', 'strawberry',  'banana']
vegetable = ['beetroot','cucumber', 'celery',  'carrot']

def update():
    for i in data_people:
        
        i.pop("_id")
        i.pop("guid")
        i.pop("balance")
        i.pop("picture")
        i.pop("email")
        i.pop("about")
        i.pop("registered")
        i.pop("tags")
        i.pop("greeting")
        i["friends"] = str(i["friends"])
        fruit = []
        vege = []
        for j in i["favouriteFood"]:
            if j in fruits:
                fruit.append(j)
            else:
                vege.append(j)
        i["favouritefruit"] = str(fruit)
        
        i["favouritevegetable"] = str(vege)
        i.pop("favouriteFood")
        y = People(**i)
        db.session.add(y)
        db.session.commit()
    
    for i in data_companies:
        z = Company(**i)
        db.session.add(z)
        db.session.commit()
update()