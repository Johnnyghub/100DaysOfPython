from requests import post

print("Welcome to flight club!\nWe find the best flight deals and email them to you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
verification = input("Enter your email again for verification: ")

if email.lower() == verification.lower():
    SHEETY_ENDPOINT = "https://api.sheety.co/e05cec963399e42a3b96c83cde4dd2b4/flightDeals/customers"
    body = {
        'customer': {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    HEADERS = {
        "Authorization": "Bearer FWEAFERDFVERASGFVREDfcafgagfaga",
    }
    with post(url=SHEETY_ENDPOINT, json=body, headers=HEADERS) as response:
        response.raise_for_status()
        print("Welcome to flight club!")
else:
    print("Emails do not match, sorry!")
