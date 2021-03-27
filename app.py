from flask import Flask, render_template
import covid19
import openapi

app = Flask(__name__)

@app.route('/')
def index():
    data = covid19.get_corona_summary()
    city_data = openapi.get_city_data()
    print("국내 데이터",data)
    print("시도 데이터",city_data)

    return render_template('index.html',corona_data = data, corona_city = city_data)

if __name__ == "__main__":
    app.run(debug = True)