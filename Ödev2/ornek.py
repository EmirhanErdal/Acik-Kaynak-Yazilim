from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_random_fact():
    api_url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if 'text' in data:
            return data['text']
    return None

@app.route('/random-fact', methods=['GET'])
def get_random_fact():
    fact = fetch_random_fact()

    if fact:
        return jsonify({'random_fact': fact})
    else:
        return jsonify({'error': 'Bilgi alınamadı'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
