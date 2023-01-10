# Flask Rest API

# Define models for database with table invoices, terms, vendors, and general_ledger_accounts
# Create API that list:
# Method: GET; Endpoint:/api/vendors

# Response:
# [
# 	{
# 	  	"vendor_id": int,
# 	  	"vendor_name": "string",
# 		"vendor_phone": "string",
# 		"vendor_address1": "string"
# 	},
# 	{
# 	  	"vendor_id": int,
# 	 	 "vendor_name": "string",
# 		"vendor_phone": "string",
# 		"vendor_address1": "string"
# 	},......
# ]

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Vendor Class/Model
class Vendor(db.Model):
    vendor_id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String(100), unique=True)
    vendor_phone = db.Column(db.String(100))
    vendor_address1 = db.Column(db.String(100))

    def __init__(self, vendor_name, vendor_phone, vendor_address1):
        self.vendor_name = vendor_name
        self.vendor_phone = vendor_phone
        self.vendor_address1 = vendor_address1

# Vendor Schema
class VendorSchema(ma.Schema):
    class Meta:
        fields = ('vendor_id', 'vendor_name', 'vendor_phone', 'vendor_address1')

# Init schema
vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)

# Create a Vendor
@app.route('/vendor', methods=['POST'])
def add_vendor():
    vendor_name = request.json['vendor_name']
    vendor_phone = request.json['vendor_phone']
    vendor_address1 = request.json['vendor_address1']

    new_vendor = Vendor(vendor_name, vendor_phone, vendor_address1)

    db.session.add(new_vendor)
    db.session.commit()

    return vendor_schema.jsonify(new_vendor)

# Get All Vendors
@app.route('/vendor', methods=['GET'])
def get_vendors():
    all_vendors = Vendor.query.all()
    result = vendors_schema.dump(all_vendors)
    return jsonify(result.data)

# Get Single Vendor
@app.route('/vendor/<id>', methods=['GET'])
def get_vendor(id):
    vendor = Vendor.query.get(id)
    return vendor_schema.jsonify(vendor)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

