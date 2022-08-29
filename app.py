from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Mission_to_Mars_DB"
mongo = PyMongo(app)



@app.route("/")
def index():
    all_data=mongo.db.mars_db.find_one()
    return render_template("index.html", data=all_data)

@app.route("/scrape")
def scrape():     
    all_info=scrape_mars.news_data()
    all_info=scrape_mars.scrapping_images()
    all_info=scrape_mars.all_facts_mars()
    all_info=scrape_mars.hemisperical()
    mongo.db.mars_db.insert_one(all_info)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
