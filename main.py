from flask import Flask, render_template, url_for

import requests



app = Flask(__name__)



def get_random_joke():

    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        return data['value']

    else:

        return "Failed to fetch Chuck Norris joke"



@app.route('/')

def index():

    joke = get_random_joke()

    return render_template('index.html', joke=joke)



if __name__ == "__main__":

    app.run(debug=True)

