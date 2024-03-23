from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

     # Checking empty feild, and setting a default value, to avoid KeyValue Error server crash
    if not bool(city.strip()):
        city = "Gujranwala"

    weather_data = get_current_weather(city)

    # Incorrect city name
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title = weather_data["name"],
        country = weather_data["sys"]["country"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8000)
    serve(app, host="0.0.0.0", port=8000)