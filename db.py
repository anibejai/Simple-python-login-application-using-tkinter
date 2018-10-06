def Database():
    global conn, cursor
    conn = sqlite3.connect('C:/Users/anirudh/Desktop/python database/sqlite-tools-win32-x86-3240000/testdb.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'entries' (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT,Firstname TEXT,Lastname TEXT)")
