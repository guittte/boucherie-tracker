import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    print("--- Modèles disponibles pour ta clé ---")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"ID: {m.name} | Display: {m.display_name}")
except Exception as e:
    print(f"Erreur lors de la récupération: {e}")
