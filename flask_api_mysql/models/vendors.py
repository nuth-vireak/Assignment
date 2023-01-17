from app import db

class vendors(db.Model):
    __tablename__ = "vendors"

    vendor_id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String(45), nullable=False)
    vendor_address1 = db.Column(db.String(45), nullable=False)
    vendor_address2 = db.Column(db.String(45), nullable=False)
    vendor_city = db.Column(db.String(45), nullable=False)
    vendor_state = db.Column(db.String(45), nullable=False)
    vendor_zip_code = db.Column(db.String(45), nullable=False)
    vendor_phone = db.Column(db.String(45), nullable=False)
    vendor_contact_last_name = db.Column(db.String(45), nullable=False)
    vendor_contact_first_name = db.Column(db.String(45), nullable=False)
    terms_id = db.Column(db.Integer, db.ForeignKey('terms.terms_id'), nullable=False)
    account_number = db.Column(db.Integer, db.ForeignKey('general_ledger_accounts.account_number'), nullable=False)