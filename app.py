from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
api_key = "bd5e378503939ddaee76f12ad7a97608"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    # API call to OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        weather_info = {
            'city': city,
            'temperature': round(weather_data['main']['temp'] - 273.15, 2),  # Convert temperature to Celsius
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }
        return render_template('weather.html', weather_info=weather_info)
    else:
        error_message = weather_data['message']
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
