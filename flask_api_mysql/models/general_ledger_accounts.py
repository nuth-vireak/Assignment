from app import db

class general_ledger_accounts(db.Model):
    __tablename__ = "general_ledger_accounts"
    account_number = db.Column(db.Integer, primary_key=True)
    account_description = db.Column(db.String(45), nullable=False)