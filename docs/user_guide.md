# User Guide

This guide outlines how to use the hodl-server API to interact with the cryptocurrency wallet and tracking system. The API supports standard CRUD (Create, Read, Update, Delete) operations across users, wallets, cryptocurrencies, fiat currencies, and price data.

All endpoints are relative to the root URL of the deployed API: https://hodl-server.onrender.com
For example, interacting with Users can be done via https://hodl-server.onrender.com/users 

All requests and responses are in JSON format.

## Users

Manage application users.
	•	Create user: POST /users
	•	Get all users: GET /users
	•	Get user by ID: GET /users/<user_id>
	•	Update user: PUT /users/<user_id>
	•	Delete user: DELETE /users/<user_id>

⸻

## Wallets

Manage digital wallets, linked to users.
	•	Create wallet: POST /wallets
	•	Get all wallets: GET /wallets
	•	Get wallet by ID: GET /wallets/<wallet_id>
	•	Update wallet: PUT /wallets/<wallet_id>
	•	Delete wallet: DELETE /wallets/<wallet_id>

You can filter wallets by user using query parameters.

⸻

## Cryptocurrencies

Maintain the list of supported cryptocurrencies.
	•	Create cryptocurrency: POST /cryptocurrencies
	•	Get all cryptocurrencies: GET /cryptocurrencies
	•	Get cryptocurrency by ID: GET /cryptocurrencies/<crypto_id>
	•	Update cryptocurrency: PUT /cryptocurrencies/<crypto_id>
	•	Delete cryptocurrency: DELETE /cryptocurrencies/<crypto_id>

⸻

## Fiat Currencies

Manage fiat currency options for price comparison and conversions.
	•	Create fiat currency: POST /fiatcurrencies
	•	Get all fiat currencies: GET /fiatcurrencies
	•	Get fiat currency by ID: GET /fiatcurrencies/<fiat_id>
	•	Update fiat currency: PUT /fiatcurrencies/<fiat_id>
	•	Delete fiat currency: DELETE /fiatcurrencies/<fiat_id>

⸻

## Cryptocurrency Prices

Track crypto-to-fiat exchange rates.
	•	Add new price record: POST /cryptoprices
	•	Get all price records: GET /cryptoprices
	•	Get price record by ID: GET /cryptoprices/<price_id>
	•	Update price record: PUT /cryptoprices/<price_id>
	•	Delete price record: DELETE /cryptoprices/<price_id>

You can also query price records by cryptocurrency and/or fiat currency IDs.

⸻

## Error Handling

Validation errors and incorrect requests will return a 400 Bad Request with details in JSON format.

Example:

{
  "error": "ValidationError",
  "messages": {
    "email": ["Not a valid email address."]
  }
}