import recurly 

import os 
from flask import Flask
import uuid

PUBLIC_DIR_PATH = os.getenv('PUBLIC_DIR_PATH', '../../public')
app = Flask(__name__, static_folder=PUBLIC_DIR_PATH, static_url_path='')


api_key = '4d3a3461d50c4f0c90d8623ea9546250'

#instantiating the Recurly Client object 
client = recurly.Client(api_key)


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to My Recurly Flask App'


#Fetch an Account Endpoint
@app.route("/accounts/<account_code>", methods=['GET'])
def get_accounts(account_code):

    try:
        account = client.get_account(f"code-{account_code}")
        return "Got Account %s" % account
    except recurly.errors.NotFoundError:
        # If the resource was not found, you may want to alert the user or
        # just return nil
        return "Resource Not Found"



#Update an Account Endpoint
@app.route("/update/<account_code>", methods=['PUT', 'GET'])
def update_accounts(account_code):

    try:
        account_update = {"address": {
		"street1": "300 Even Newer Address",
		"street2": "",
		"city": "San Francisco",
		"region": "CA",
		"postal_code": "94110",
		"country": "US",
		"phone": "" }
        }
        account = client.update_account(f"code-{account_code}", account_update)
        return "Updated Account %s" % account
    except recurly.errors.ValidationError as e:
        # If the request was invalid, you may want to tell your user
        # why. You can find the invalid params and reasons in e.error.params
        print("ValidationError: %s" % e.error.message)
        print(e.error.params)


#Creating an Account Endpoint
@app.route("/new", methods=['POST', 'GET'])
def new_purchase():

    try:
        recurly_account_code = str(uuid.uuid1())
        purchase = {
            "currency": "USD",
            "account": {
                "code": recurly_account_code,
                "first_name": "Brian",
                "last_name": "Swiggum",
                "billing_info": {
                    "first_name": "Brian",
                    "last_name": "Swiggum",
                    "company": "",
                    "address": {
                        "phone": "",
                        "street1": "1800 This Street",
                        "street2": "string",
                        "city": "Seatle",
                        "region": "WA",
                        "postal_code": "55555",
                        "country": "US"
                        },
                    "number": "4111111111111111",
                    "month": "",
                    "year": "",
                    "cvv": "",
                }
            },
            "subscriptions": [{"plan_code": '09111991'}],
        }
        invoice_collection = client.create_purchase(purchase)
        return "Created Charge Invoice %s" % invoice_collection.charge_invoice
        # return "Created Credit Invoices %s" % invoice_collection.credit_invoices

    except recurly.errors.ValidationError as e:
        # If the request was invalid, you may want to tell your user
        # why. You can find the invalid params and reasons in e.error.params
        print("ValidationError: %s" % e.error.message)
        return e.error.params





