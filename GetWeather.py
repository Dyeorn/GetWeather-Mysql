import requests
import mysql.connector
from datetime import datetime


api_key = "sua_api_key"
cities = ['Nova York', 'Tóquio', 'Bay Area', 'Londres', 'Singapura', 'Los Angeles', 'Hong Kong', 'Pequim', 'Xangai', 'Sydney', 'Chicago', 'Toronto', 'Frankfurt', 'Zurique', 'Houston', 'Seul', 'Melbourne', 'Paris', 'São Paulo', 'Jacobina']
data_atual = datetime.now().date()
data_formatada = data_atual.strftime("%d/%m/%Y")


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'pjota',
    password = 'papaleguas1',
    database = 'weather2'
)


cursor = conexao.cursor()

for city in cities:

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    name = data["name"]
    country = data["sys"]["country"]
    weather = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    speed = data["wind"]["speed"]
    descript = data ["weather"][0]["description"]
    celsius = weather - 273.15

    consulta = "INSERT INTO dados_tempo (city, country, weather, humidity, speed, descript, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (name, country, celsius, humidity, speed, descript, data_formatada)
    cursor.execute(consulta, valores)


conexao.commit()
cursor.close()
conexao.close()


