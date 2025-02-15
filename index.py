from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
BACKEND_URL = "https://ventas-backend.azurewebsites.net"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consult', methods=['POST'])
def consult():
    query = request.form.get("query")
    if not query:
        return jsonify({"error": "Debe ingresar una consulta válida."}), 400
    
    response = requests.post(f"{BACKEND_URL}/generate-response", json={"customer_id": None, "query": query})
    
    if response.status_code == 200:
        return jsonify({"respuesta": response.json()["respuesta"]})
    else:
        return jsonify({"error": "Error en la consulta. Verifique el servidor backend."}), 500

if __name__ == '__main__':
    app.run(debug=True)
