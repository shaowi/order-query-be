# Backend for Order Query

This is a simple backend for querying the top 10 customers with the most orders in a given date range. It is built with flask and sqlite3.

## Pre-requisites

- Python 3.6 or higher
- pip

## Installation

1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Run the server with `python app.py`

## Endpoints

### GET /topCustomers

- Query Parameters:
  - startDate: The start date of the date range (format: YYYY-MM-DD)
  - endDate: The end date of the date range (format: YYYY-MM-DD)

This endpoint returns the top 10 customers with the most orders in the given date range.
