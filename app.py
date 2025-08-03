from flask import Flask , render_template
app = Flask(__name__)
travel = [
    {
        "Entry No :" :"1",
        "Place" :"Paris",
        "Description" :"The city of lights",
        "Tour Price" :"$1200",
    },
    {
        "Entry No :" :"2",
        "Place" :"New York",
        "Description" :"The city that never sleeps",
        "Tour Price" :"$1500",
    },
    {
        "Entry No :" :"3",
        "Place" :"Tokyo",
        "Description" :"The heart of Japan",
        "Tour Price" :"$1800",
    },
    {
        "Entry No :" :"4",
        "Place" :"Sydney",
        "Description" :"The harbour city",
        "Tour Price" :"$2000",
    },
    {   
        "Entry No :" :"5",
        "Place" :"Cape Town",
        "Description" :"The mother city of South Africa",
        "Tour Price" :"$1600",
    }

]
@app.route('/')
def hello_world():
    return render_template('index.html', travel=travel,Agency_Name="Meet Nature",Agency_Description="We provide the best travel experiences around the world.")

if __name__ == '__main__':
    app.run(debug=True)