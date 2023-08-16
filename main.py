"""
main.py

Date: 07/20/2023

Programmer's name: Suren Tumasyan

Description: Runs the Flask app

"""
from flaskapp import create_app
from flask import session

app = create_app()
app.secret_key = "AWPrceEAXo4uiM" 

if __name__ == '__main__':
    """Runs the Flask application.
    
    Starts the Flask web server and runs the application on the specified host and port.
    """

    app.run(host='0.0.0.0', port=5000, debug=True)