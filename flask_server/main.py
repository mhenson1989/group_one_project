from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import timezone

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://root:Mike0310@mypostgresdb.clwl24wa1fo4.us-east-1.rds.amazonaws.com:5432/my_data_class_db"
db.init_app(app)
@app.route('/')
def home():

    return render_template("base.html", zips= ['zipcodes'])

@app.route("/api/<zipcode>")
def api(zipcode):
    ret_value = db.session.execute(f"SELECT * FROM txhousing WHERE zipcodes = {zipcode}")
    #return [(float(x[1]),float(x[2])) for x in ret_value]
    for x in ret_value:
        return str(x[1])+","+str(x[2])
    #timestampdate = date.replace(tzinfo=timezone.utc).timestamp()
    #print(timestampdate)

    #return [(float(x[1])*timestampdate+float(x[2])) for x in ret_value]

if __name__ == "__main__":
    app.run(debug=True)