import requests
import json
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_weather_data(url: str) -> list:
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        logging.error("Erro de Requisição - extract_data.py:14")
        return []

    if not data:
        logging.warning("Nenhum dado retornado - extract_data.py:18")  # Corrigido de .warn para .warning
        return []

    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"Arquivo salvo em {output_path} - extract_data.py:28")

    return data 
