from app.database import db

class DIDNumber(db.Model):
    __tablename__ = 'did_number'
    
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(20), nullable=False, unique=True)
    monthly_price = db.Column(db.Numeric(10, 2), nullable=False)
    setup_price = db.Column(db.Numeric(10, 2), nullable=False)
    currency = db.Column(db.String(5), nullable=False)
