from app import db

class terms(db.Model):
    __tablename__ = "terms"
    
    terms_id = db.Column(db.Integer, primary_key=True)
    terms_description = db.Column(db.String(50), nullable=False)
    terms_due_days = db.Column(db.Integer, nullable=False)