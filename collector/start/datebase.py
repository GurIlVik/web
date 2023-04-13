import sqlite3 


def open_file_bd(email, token, name):
    conn = sqlite3.connect('db_sqlite3.gurilvik')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS otpravka_register(
        id INTEGER PRIMARY KEY,
        email VARCHAR(50),
        token VARCHAR(50),
        name VARCHAR(50)
        )''')
    request = (f'''INSERT INTO otpravka_register (email, token, name)
            VALUES ("{email}", "{token}", "{name}")''')
    cursor.execute(request)
    conn.commit()
    
    for i in cursor.execute('SELECT * FROM otpravka_register'):
        print(i)
    
    
    