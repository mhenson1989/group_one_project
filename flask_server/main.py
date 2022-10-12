from flask import Flask, render_template, jsonify
#from sqlalchemy import create_engine
from flask_sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine("https://my-first-s3-data-bucket-1.s3.amazonaws.com/slope_intercept.csv")

@app.route('/')
def home():
    # tx housing is the table in pgadmin
    df = pd.read_sql('txhousing', con=engine)

    return render_template("base.html", zips= [zipcodes])

@app.route("/api/<zipcode>")
def api(zipcode):
    ret_value = int(zipcode)*2
    # this is where you SQL read goes
    return jsonify({"return":ret_value})

if __name__ == "__main__":
    app.run(debug=True)