from app import db

class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(100))
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id'))
    bank = db.relationship('Bank', back_populates='branches')

Bank.branches = db.relationship('Branch', order_by=Branch.id, back_populates='bank')
