from flask import Flask

app = Flask(__name__)

companies = [
    {
        "name": "company1",
        "items": [
            {
                "name": "item1",
                "price": 15.99
            },
            {
                "name": "item2",
                "price": 25.99
            }
        ]
    },
    {
        "name": "company2",
        "items": [
            {
                "name": "item3",
                "price": 35.99
            },
            {
                "name": "item4",
                "price": 45.99
            }
        ]
    }
]

@app.route('/company/<string:name>')
def get_company(name):
    for company in companies:
        if company['name'] == name:
            return company
    return {'message': 'Company not found'}

app.run(port=5000)
