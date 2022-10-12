from flask import Flask, render_template, jsonify
# from sqlalchemy import create_engine
# from flask_sqlalchemy import create_engine

app = Flask(__name__)
# engine = create_engine("SQL_URI")

@app.route('/')
def home():
    # df = pd.read_sql('mxpluxbtable', con=engine)

    return render_template("base.html", zips= [12345,23456,34567])

@app.route("/api/<zipcode>")
def api(zipcode):
    ret_value = int(zipcode)*2
    # this is where you SQL read goes
    return jsonify({"return":ret_value})

if __name__ == "__main__":
    app.run(debug=True)