from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:1234@localhost:3306/apdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import invoices, terms, vendors, general_ledger_accounts
db.init_app(app)

with app.app_context():
    db.create_all()

@app.get('/api/vendors')
def get_vendors():
    v = db.session.query(vendors)\
        .with_entities(vendors.vendor_id, vendors.vendor_name, vendors.vendor_address1, vendors.vendor_phone)

    ls=[]
    for v in v:
        te = {
            "vendor_id" : v.vendor_id,
            "vendor_name" : v.vendor_name,
            "vendor_address1" : v.vendor_address1,
            "vendor_phone" : v.vendor_phone
        }
        ls.append(te)
    return ls

@app.get('/api/invoices/vendors/<string:vendor_name>')
def get_invoices_by_vendor_name(vendor_name):
    i = db.session.query(invoices, vendors, terms)\
        .join(vendors, invoices.vendor_id == vendors.vendor_id)\
        .join(terms, invoices.terms_id == terms.terms_id)\
        .filter(vendors.vendor_name.like('%'+vendor_name+'%'))\
        .with_entities(invoices.invoice_id, invoices.invoice_number, invoices.invoice_total, vendors.vendor_name, terms.terms_description)

    ls=[]
    for i in i:
        te = {
            "invoice_id" : i.invoice_id,
            "invoice_number" : i.invoice_number,
            "invoice_total" : i.invoice_total,
            "vendor_name" : i.vendor_name,
            "term_description" : i.terms_description
        }
        ls.append(te)
    return ls

@app.post('/api/general_ledger_accounts/new')
def create_general_ledger_account():
    account_number = request.json['account_number']
    account_description = request.json['account_description']

    new_account = general_ledger_accounts(account_number=account_number, account_description=account_description)
    db.session.add(new_account)
    db.session.commit()
    return "Account number " + str(account_number) + " has been created."

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000)
