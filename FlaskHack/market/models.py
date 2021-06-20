from market import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    education = db.Column(db.String(length=60), nullable=False)
    skill = db.Column(db.String(length=60), nullable=False)
    exp = db.Column(db.String(length=60), nullable=False)
    domicile = db.Column(db.String(length=60), nullable=False)
    resume = db.Column(db.String(length=60), nullable=False)
    repo = db.Column(db.String(length=60), nullable=False)
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Company(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    company_name = db.Column(db.String(length=30), nullable=False, unique=True)
    position = db.Column(db.String(length=50), nullable=False, unique=True)
    education = db.Column(db.String(length=60), nullable=False)
    skill = db.Column(db.String(length=60), nullable=False)
    exp = db.Column(db.String(length=60), nullable=False)
    domicile = db.Column(db.String(length=60), nullable=False)
    number_of_need = db.Column(db.String(length=60), nullable=False)
    benefit = db.Column(db.String(length=60), nullable=False)
   
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}'