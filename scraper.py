#!/usr/bin/env python3
"""
Opcjonalny skrypt do aktualizacji danych produktów.
Dostosuj do swojego źródła danych (API hurtowni, CSV, itd.).

Użycie:
  python scraper.py

Po uruchomieniu zaktualizuj produkty.json / promocje.json / magazyn.json
a następnie uruchom regenerate_*.py aby odświeżyć HTML.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent

print("Skrypt szablonowy – uzupełnij logikę pobierania danych z Twojego źródła.")
print("Przykład: wczytaj CSV / API i zapisz do promocje.json")

# Przykład struktury promocje.json:
example = [{
    "tytul": "Nazwa produktu",
    "opis": "Krótki opis",
    "cena": "999 zł",
    "cena_stara": "1299 zł",
    "zdjecie": "images/promocje/nazwa.jpg",
    "zdjecie_duze": "images/promocje/nazwa.jpg",
    "producent": "Marka",
    "aktualizacja": str(date.today())
}]
print(json.dumps(example, ensure_ascii=False, indent=2))
