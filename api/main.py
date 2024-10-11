from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/verbe/<verbe>', methods=['GET'])
def conjuguer_verbe(verbe):
    # URL de base du site de conjugaison avec le verbe dynamique
    url = f'https://www.conjugaison.com/verbe/{verbe}.html'
    
    # Faire une requête HTTP GET sur cette URL
    response = requests.get(url)
    
    # Vérifier que la page existe
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Votre logique pour scraper les informations de conjugaison
        conjugaison_data = {}  # Dictionnaire pour stocker les conjugaisons
        
        # Exemple de scraping (adapté à votre logique spécifique)
        sections = soup.find_all('div', class_='verbebox')  # Récupérer les sections de conjugaison
        for section in sections:
            tense = section.find('a').text.strip()  # Le temps (Présent, Passé, etc.)
            conjugaison = section.find('p').text.strip()  # Les conjugaisons sous ce temps
            conjugaison_data[tense] = conjugaison.split('\n')  # Ajouter au dictionnaire
            
        # Retourner les données sous forme JSON
        return jsonify(conjugaison_data)
    else:
        # Si le verbe n'existe pas ou la page n'est pas trouvée
        return jsonify({"error": "Verbe non trouvé"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
