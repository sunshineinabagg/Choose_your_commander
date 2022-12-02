import requests
import sqlite3

URL = 'https://api.scryfall.com'

try:
    sqlite_connection = sqlite3.connect('scryfall.db')

    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS cards (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                text TEXT,
                                image TEXT NOT NULL,
                                colors TEXT NOT NULL,
                                partner TEXT NOT NULL)'''

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()

    for i in range(100):
        r = requests.get(f'{URL}/cards/random?q=is%3Acommander&cc_key=').json()
        
        info = [
            r.get('name'),
            r.get('oracle_text'),
            r['image_uris']['png'],
            str(r.get('color_identity'))
        ]

        if "Partner" in r.get('keywords'):
            info.append(True)
        else:
            info.append(False)
            
        cursor = sqlite_connection.cursor()
        cursor.execute('INSERT INTO cards (name, text, image, colors, partner) VALUES(?, ?, ?, ?, ?)', info)
        sqlite_connection.commit()
        cursor.close()              

except KeyError:
    print(r.get('scryfall_uri'))    

finally:
    if (sqlite_connection):
        sqlite_connection.close()