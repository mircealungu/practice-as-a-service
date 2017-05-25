from flask import Flask
from zeeguu_exercises import ex_blueprint


app = Flask(__name__)
app.register_blueprint(ex_blueprint)


"""
TODO consider this option
def home_page(session):
    response = make_response(render_template('index.html'))
    response.set_cookie('sessionID', session)
    return response
"""
if __name__ == "__main__":
    app.run(debug=True)
