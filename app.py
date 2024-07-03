from flask import Flask, render_template, request
import requests

def crear_app():
    app = Flask(__name__)

    # Endpoint base de la API de EMT Madrid
    BASE_URL = "https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/"

    # Función para hacer la consulta a la API
    def consultar_emt(stop_id, line_arrive):
        url = f"{BASE_URL}{stop_id}/arrives/{line_arrive}/"
        headers = {
            'Accept': 'application/json',
            'accessToken': 'cd449b3a-3957-11ef-b838-523c69ce06f6'  # Reemplazar con tu API Key de EMT Madrid
        }
        # Cuerpo de la solicitud
        body = {
            "cultureInfo": "ES",
            "Text_StopRequired_YN": "Y",
            "Text_EstimationsRequired_YN": "Y",
            "Text_IncidencesRequired_YN": "N",
            "DateTime_Referenced_Incidencies_YYYYMMDD": ""
        }
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and data['data']:
                first_arrival = data['data'][0]['Arrive'][0]
                estimate_arrive_seconds = first_arrival.get('estimateArrive', 0)
                estimate_arrive_minutes = estimate_arrive_seconds // 60
                return estimate_arrive_minutes
            else:
                return None
        else:
            return None

    # Ruta principal para el formulario y resultados
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            stop_id = request.form['stop_id']
            line_arrive = request.form['line_arrive']
            estimate_arrive = consultar_emt(stop_id, line_arrive)
            if estimate_arrive is not None:
                return render_template('index.html', estimate_arrive=estimate_arrive, stop_id=stop_id, line_arrive=line_arrive)
            else:
                return render_template('index.html', error="Error al obtener los datos de la EMT")
        return render_template('index.html', estimate_arrive=None)
    return app
if __name__ == '__main__':
    app = crear_app()
    app.run()
