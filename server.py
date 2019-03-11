from flask import Flask, request
import json
import requests
from twilio.rest import TwilioRestClient

client = TwilioRestClient(account_sid, auth_token)
fromnumber = "+18563228074"
app = Flask(__name__)


@app.route('/countryfacts')
def country_fact():
    text = request.values.get('Body', 'United States of America')
    # text = text.strip()
    number = request.values.get('From', '+12672502802')
    url = "https://restcountries.eu/rest/v1/all"
    response = requests.get(url)
    #a list of countries
    countries = response.json()
    #find a county
    for country in countries:
        name = country.get("name")
        if text == name:
            population = country.get("population")
            message = client.messages.create(body="The population in {name} is {population}".format(name=name,
                                                                   population=population),to=number,from_=fromnumber)
            return ""
    message = client.messages.create(body="Not found",to=number,from_=fromnumber)
    return ""

app.run()
