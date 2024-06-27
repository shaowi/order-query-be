from flask import request, jsonify, current_app as app
from sqlalchemy.sql import func
from .models import db, Customer, Order


@app.route("/api/topCustomers", methods=["GET"])
def get_top_customers():
    start_date = request.args.get("startDate")
    end_date = request.args.get("endDate")

    subquery = (
        db.session.query(
            Order.customerID, func.count(Order.orderID).label("orderCount")
        )
        .filter(Order.orderDate.between(start_date, end_date))
        .group_by(Order.customerID)
        .order_by(func.count(Order.orderID).desc())
        .limit(10)
        .subquery()
    )

    results = (
        db.session.query(
            Customer.customerID, Customer.contactName, subquery.c.orderCount
        )
        .join(subquery, Customer.customerID == subquery.c.customerID)
        .all()
    )

    top_customers = [
        {
            "customerID": r.customerID,
            "contactName": r.contactName,
            "orderCount": r.orderCount,
        }
        for r in results
    ]
    return jsonify(top_customers)
