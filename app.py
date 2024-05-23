from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/save-user-info', methods=['POST'])
def save_user_info():
    data = request.get_json()
    wallet = data.get('wallet')
    ip = data.get('ip')
    location = data.get('location')

    log_entry = f"Wallet: {wallet}, IP: {ip}, Location: {location}\n"
    
    file_path = os.path.join(os.path.dirname(__file__), 'user_info.txt')

    try:
        with open(file_path, 'a') as file:
            file.write(log_entry)
        return jsonify({"message": "Informations enregistrées"}), 200
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier: {e}")
        return jsonify({"message": "Erreur du serveur"}), 500

@app.route('/view-user-info', methods=['GET'])
def view_user_info():
    file_path = os.path.join(os.path.dirname(__file__), 'user_info.txt')

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({"content": content}), 200
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
        return jsonify({"message": "Erreur du serveur"}), 500

if __name__ == '__main__':
    app.run(port=5000)
