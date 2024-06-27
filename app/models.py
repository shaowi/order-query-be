from . import db


class Customer(db.Model):
    __tablename__ = "Customers"
    customerID = db.Column(db.String, primary_key=True)
    contactName = db.Column(db.String)


class Order(db.Model):
    __tablename__ = "Orders"
    orderID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.String, db.ForeignKey("Customers.customerID"))
    orderDate = db.Column(db.Date)
