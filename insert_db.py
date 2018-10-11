import sqlite3

DBPATH = 'return_db.sqlite'
db_con = sqlite3.connect(DBPATH)
cursor = db_con.cursor()

try:
    #CREATE
    cursor.execute("CREATE TABLE IF NOT EXISTS return (input TEXT PRIMARY KEY, output TEXT NOT NULL)")

    print("認識してほしい言葉を入力して下さい")
    word_in = input(">>")
    print("それに対する返答を入力して下さい")
    word_out = input(">>")

    # INSERT
    cursor.execute("INSERT INTO return VALUES (?, ?)", (word_in, word_out))

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

db_con.commit()
db_con.close()
