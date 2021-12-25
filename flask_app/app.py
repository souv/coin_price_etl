from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
import pandas as pd 

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:zzzaaa999@localhost:3306/crawler_db"

db.init_app(app)


colnames = ['datetime','coin_name','coin_price']

@app.route('/login',methods=['POST','GET'])
def main():
	sql_cmd ="""select * from coin_price"""
	query_data = db.engine.execute(sql_cmd)
	df = pd.DataFrame (query_data,columns=colnames)
	return render_template('result.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == "__main__":
    app.run()