""" Your Verdure Server """

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, url_for



# GET https://api.yelp.com/v3/businesses/search


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
# app.secret_key = os.environ['FLASK_TOKEN']
# app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def market_list():
    """Show list of farmer's markets on home page. 
    """

    return render_template("index.html")

# @app.route('/<int:market_id>')
# def market_detail(market_id):
#     """Show detail for individual market."""

##############################################################################
# Helper functions



# # Setup up variables based on environment (Heroku, local) 
# PORT = int(os.environ.get("PORT", 5000))
# DEBUG = "NO_DEBUG" not in os.environ

if __name__ == "__main__":
    app.run()