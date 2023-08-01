from flaskapp import create_app
from flask import session

app = create_app()
app.secret_key = "AWPrceEAXo4uiM" 

if __name__ == '__main__':
    #app.run(debug=True)

    app.run(host='0.0.0.0', port=5000, debug=True)