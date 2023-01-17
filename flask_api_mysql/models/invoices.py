from app import db

class invoices(db.Model):
    __tablename__ = "invoices"

    invoice_id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.vendor_id'), nullable=False)
    invoice_number = db.Column(db.Integer, nullable=False)
    invoice_date = db.Column(db.DateTime, nullable=False)
    invoice_total = db.Column(db.Float, nullable=False)
    payment_total = db.Column(db.Float, nullable=False, default=0.00)
    credit_total  = db.Column(db.Float, nullable=False, default=0.00)
    terms_id = db.Column(db.Integer, db.ForeignKey('terms.terms_id'), nullable=False)
    invoice_due_date = db.Column(db.DateTime, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=None)