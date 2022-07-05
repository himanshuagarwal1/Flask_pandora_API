# Flask-RESTful API for Pandora challenge 

This project shows one of the possible ways to implement RESTful API server for Pandora challenge.

There are implemented two models: People and companies amd three endpoints people, peopletwo and company.

Main libraries used:
1. Flask - Flask framework
2. Flask-RESTful - restful API library.
3. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
|
├── endpoints
│   ├── __init__.py
│   ├── company.py
│   │── friends.py
│   └── people.py
│
├── Models
│   ├── __init__.py
│   └── Data_models.py
│
├── app.py
├── update.py
├── data.py
├── Readme.md
├── database.db
├── requirements.txt
├── companies.json
├── people.json
└── test.py
```


* app.py - flask application initialization.
* test.py - unittest for endpoints.
* database.db - database 
* update.py-  to update the database 
* database.db - database 
* database.db - database 
* requirements.txt  - requirements to run this projects 
* data_models - contains all data models.
* endpoints - contains all endpoints and resources for API endpoints.

## Running 

1. Clone repository.
2. pip install -r requirements.txt
3. Run command: python app.py

# Running tests
1. this unittests is covered around the endpoints of API
2. before running the tests make sure the flask app is runnig 
3. Open a new terminal and run test.py. 

# update database
1. to update the database please replace the companies.json and people.json present in the project with exact same columns and name of files.
2. Open a new terminal and run update.py

## Usage



### People endpoint

Solution for "Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`"

REQUEST

In this endpoint Decker is first name and Mckenzie is last name the valid and name is required for the appropriate result

GET  http://127.0.0.1:5000/people/Decker&Mckenzie 

RESPONSE 

''' json
{
    "index": 1,
    "name": "Decker Mckenzie",
    "age": 60,
    "favouritefruit": "[]",
    "favouritevegetable": "['cucumber', 'beetroot', 'carrot', 'celery']"
}



### Peopletwo endpoint

Solution for "Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive."

REQUEST

In this endpoint there are 2 names Bonnie_Bass and Rosemary_Hayes 2 names should be joined by "&" and first name and last name with "_", It should follow this structure. 

GET http://127.0.0.1:5000/peopletwo/Bonnie_Bass&Rosemary_Hayes


RESPONSE 

''' json
[
    {
        "index": 1,
        "age": 60,
        "name": "Decker Mckenzie",
        "phone": "+1 (893) 587-3311",
        "address": "492 Stockton Street, Lawrence, Guam, 4854"
    }
]


### company endpoint

Solution for "Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees."

REQUEST

In this endpoint enter company's name to the endpoint

GET http://127.0.0.1:5000/company/PERMADYNE

RESPONSE 

''' json

[
    {
        "index": 289,
        "name": "Frost Foley"
    },
    {
        "index": 580,
        "name": "Luna Rodgers"
    },
    {
        "index": 670,
        "name": "Boyer Raymond"
    },
    {
        "index": 714,
        "name": "Solomon Cooke"
    },
    {
        "index": 828,
        "name": "Walter Avery"
    },
    {
        "index": 928,
        "name": "Hester Malone"
    },
    {
        "index": 985,
        "name": "Arlene Erickson"
    }
]

