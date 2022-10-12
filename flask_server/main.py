from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
#you can install flash_sqlalchemy using pip install flask-sqlalchemy but neither work (don't as me why it's a dash in the pip install)
#from flask_sqlalchemy import create_engine


app = Flask(__name__)
engine = create_engine("https://my-first-s3-data-bucket-1.s3.amazonaws.com/slope_intercept.csv")

@app.route('/')
def home():
    # tx housing is the table in pgadmin
    df = pd.read_sql('txhousing', con=engine)

#Is this the correct way to fetch the zip? Can't check it... In our database csv file the zip column is named zipcodes
    return render_template("base.html", zips= ['zipcodes'])

@app.route("/api/<zipcode>")
def api(zipcode):
    ret_value = int(zipcode)*2
    # this is where you SQL read goes
    #I was trying to look up what we replace the *2 with but I wasn't sure... and I can't get the create_engine to work to throw stuff at the wall through testing.
    return jsonify({"return":ret_value})

if __name__ == "__main__":
    app.run(debug=True)