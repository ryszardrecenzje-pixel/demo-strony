# Szablon strony AGD – sprzedaż i serwis

Czysty, gotowy do personalizacji szablon statycznej strony internetowej dla sklepu / serwisu AGD (sprzęt AGD).  
Przeznaczony dla klientów, którzy chcą szybko uruchomić profesjonalną stronę z katalogiem produktów, promocjami, magazynem i koszykiem wyceny.

---

## Co zawiera szablon

| Element | Opis |
|---------|------|
| **index.html** | Strona główna: o firmie, slider, serwis, kontakt, formularz zgłoszenia naprawy |
| **sprzedaz.html** | Przegląd kategorii AGD |
| **promocje.html** | Promocje dnia (generowane z `promocje.json`) |
| **magazyn.html** | Aktualny stan magazynu (generowany z `magazyn.json`) |
| **koszyk.html** + **koszyk.js** / **cart.js** | Koszyk wyceny (localStorage) – klient zbiera produkty i prosi o wycenę |
| Strony kategorii | lodowki.html, pralki.html, zmywarki.html, piekarniki.html, plyty_grzewcze.html, kuchenki.html, suszarki.html, zamrazarki.html, male_agd.html |
| **style.css** | Główne style |
| **config.js** | Centralna konfiguracja firmy (do uzupełnienia) |
| **produkty.json** | Dane produktów per kategoria (przykład) |
| **promocje.json** | Lista promocji dnia (przykład) |
| **magazyn.json** | Lista produktów z magazynu (przykład) |
| **regenerate_promocje_html.py** | Skrypt generujący `promocje.html` z JSON |
| **regenerate_magazyn_html.py** | Skrypt generujący `magazyn.html` z JSON |
| **scraper.py** | Szablon skryptu do automatycznej aktualizacji danych (do dostosowania) |

---

## Szybki start – personalizacja (krok po kroku)

### 1. Wymień dane firmy (placeholdery)

W **wszystkich plikach HTML** oraz w `config.js` wyszukaj i zamień:

| Placeholder          | Co wstawić                          | Przykład                    |
|----------------------|-------------------------------------|-----------------------------|
| `NAZWA_FIRMY`        | Nazwa Twojej firmy                  | AGD Premium                 |
| `MIASTO`             | Miasto                              | Poznań                      |
| `ADRES_ULICA`        | Ulica i numer                       | ul. Kwiatowa 12             |
| `KOD_POCZTOWY`       | Kod pocztowy                        | 60-123                      |
| `TELEFON_1`          | Główny telefon                      | 500 100 200                 |
| `TELEFON_2`          | Drugi telefon (opcjonalnie)         | 500 100 201                 |
| `TWOJA_STRONA_FB`    | Link do Facebooka                   | twojafirmapl                |
| `TWOJ_INSTAGRAM`     | Nazwa użytkownika Instagram         | twojafirma                  |
| `INSTAGRAM_USER`     | (w starszych miejscach)             | twojafirma                   |

**Najłatwiej:** użyj edytora z funkcją „Znajdź i zamień we wszystkich plikach” (VS Code, Sublime, Notepad++).

Dodatkowo zaktualizuj `config.js`:

```js
window.SITE_CONFIG = {
  nazwa: "AGD Premium",
  miasto: "Poznań",
  adres_ulica: "ul. Kwiatowa 12",
  kod_pocztowy: "60-123",
  telefon1: "500 100 200",
  telefon2: "500 100 201",
  email: "kontakt@agdpremium.pl",
  facebook: "https://www.facebook.com/agdpremium",
  instagram: "https://www.instagram.com/agdpremium/",
  maps_query: "AGD+Premium+ul.+Kwiatowa+12+Poznań",
  logo: "images/logo.png"
};
```

### 2. Logo

Zastąp plik:

```
images/logo.png
```

Swoim logo (najlepiej PNG z przezroczystym tłem, wysokość ok. 50–80 px).

### 3. Zdjęcia kategorii

W folderze `images/categories/` znajdują się przykładowe miniatury.  
Możesz je podmienić na własne (zachowaj nazwy plików lub zaktualizuj odwołania w HTML).

### 4. Produkty (katalog)

Edytuj plik **produkty.json**. Struktura:

```json
{
  "lodowki.html": [
    {
      "tytul": "Nazwa modelu",
      "opis": "Krótki opis produktu",
      "cena": "Cena na zapytanie",
      "zdjecia": [
        "images/produkty/lodowki/model1.jpg"
      ]
    }
  ],
  "pralki.html": [ ... ],
  ...
}
```

- Klucze odpowiadają nazwom plików kategorii.
- Zdjęcia umieść w `images/produkty/...` (utwórz podfoldery według potrzeb).
- Po zmianie JSON strony kategorii **nie generują się automatycznie** – część stron ma dane wbudowane.  
  Dla pełnej automatyzacji użyj skryptów regenerate lub ręcznie uzupełnij sekcje produktów.

### 5. Promocje dnia

1. Uzupełnij **promocje.json** listą aktualnych promocji.
2. Umieść zdjęcia w `images/promocje/`.
3. Uruchom generator:

```bash
python regenerate_promocje_html.py
```

Skrypt nadpisze `promocje.html` na podstawie JSON (zachowując nagłówek/stopkę).

### 6. Magazyn

1. Uzupełnij **magazyn.json**.
2. Umieść zdjęcia w `images/magazyn/`.
3. Uruchom:

```bash
python regenerate_magazyn_html.py
```

### 7. Koszyk wyceny

Działa od razu (localStorage w przeglądarce).  
Klient dodaje produkty → otwiera koszyk → „Proszę o wycenę” → przekierowanie do formularza na stronie głównej z wypełnioną listą.

Klucz localStorage: `agd_koszyk_wyceny`.

---


### 8. Formularz kontaktowy / zgłoszenia naprawy

Na stronie głównej używany jest Formspree (formspree.io).  
**Koniecznie** utwórz własne konto na formspree.io i zamień ID formularza:

Szukaj w `index.html`:
```
https://formspree.io/f/mrpglqgz
```
Zamień na swój endpoint (np. `https://formspree.io/f/xxxxxxxx`).

### 9. Mapa Google (osadzona)

W sekcji kontaktu jest placeholder embedu mapy.  
Najprościej:

1. Wejdź na Google Maps → wyszukaj swoją firmę → Udostępnij → Umieść mapę → skopiuj kod iframe.
2. Zastąp istniejący iframe w `index.html`.

Albo użyj linku wyszukiwania (już przygotowany z placeholderami).


## Wymagania techniczne

- Serwer WWW (Apache, Nginx, Netlify, GitHub Pages, Vercel, dowolny hosting statyczny)  
  **lub** po prostu otwieranie plików lokalnie (niektóre funkcje JS mogą mieć ograniczenia CORS).
- Do uruchamiania skryptów Python: Python 3.8+ (bez zewnętrznych zależności w wersji podstawowej).
- Opcjonalnie: GitHub Actions do automatycznej aktualizacji (wzór w `.github/workflows/` – do dostosowania).

---

## Automatyzacja (opcjonalnie)

Szablon zawiera:

- `scraper.py` – szkielet do podłączenia własnego źródła danych (API hurtowni, plik CSV, Excel itp.).
- `regenerate_*.py` – generowanie stron HTML z JSON.

**Przykładowy przepływ codziennej aktualizacji promocji:**

1. Skrypt pobiera dane z Twojego systemu B2B / CSV.
2. Zapisuje do `promocje.json`.
3. Uruchamia `regenerate_promocje_html.py`.
4. Commit + push (lub automatyczny deploy).

Możesz dodać plik `.github/workflows/update.yml` z cronem (wzór znajdziesz w oryginalnym projekcie).

---

## Struktura katalogów (docelowa)

```
szablon-agd-klient/
├── index.html
├── sprzedaz.html
├── promocje.html
├── magazyn.html
├── koszyk.html
├── lodowki.html
├── pralki.html
├── zmywarki.html
├── piekarniki.html
├── plyty_grzewcze.html
├── kuchenki.html
├── suszarki.html
├── zamrazarki.html
├── male_agd.html
├── style.css
├── config.js
├── cart.js
├── koszyk.js
├── produkty.json
├── promocje.json
├── magazyn.json
├── regenerate_promocje_html.py
├── regenerate_magazyn_html.py
├── scraper.py
├── README.md
└── images/
    ├── logo.png
    ├── categories/
    ├── promocje/
    ├── magazyn/
    └── produkty/
```

---

## Co zostało usunięte z oryginalnego projektu

- Wszystkie konkretne podstrony produktów (marka-model.html)
- Dane firmy Domel Konin (adres, telefony, social media)
- Skrypty pobierające dane z konkretnego B2B (z danymi logowania)
- Skrypty pobierania zdjęć z zewnętrznych źródeł (Ceneo, producentów itp.)
- Logi i pliki tymczasowe
- Workflowy GitHub Actions przypisane do konkretnego repo

Została czysta struktura + przykładowe dane + skrypty generujące, gotowe do podpięcia własnych źródeł.

---

## Wskazówki dla klientów (subskrypcja / white-label)

1. Po otrzymaniu szablonu wykonaj kroki 1–3 (dane firmy + logo).
2. Uzupełnij JSON-y produktami (lub zleć to nam w ramach subskrypcji).
3. Hostuj na dowolnym hostingu statycznym lub u nas.
4. Aktualizacje promocji/magazynu możesz robić sam (JSON + skrypt) albo korzystać z usługi aktualizacji.

---

## Licencja / użycie

Szablon przeznaczony do komercyjnego wykorzystania przez klientów końcowych.  
Nie usuwaj informacji o autorze szablonu, jeśli takie się znajdują (w tej wersji zostały wyczyszczone).

---

## Wsparcie

W razie pytań dotyczących personalizacji lub automatyzacji skontaktuj się z dostawcą szablonu.

Powodzenia z nową stroną!
