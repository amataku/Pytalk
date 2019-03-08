import sqlite3

DBPATH = 'return_db.sqlite'
db_con = sqlite3.connect(DBPATH)
cursor = db_con.cursor()

try:
    #CREATE
    cursor.execute("CREATE TABLE IF NOT EXISTS return (input TEXT PRIMARY KEY, output TEXT NOT NULL, label TEXT, selec TEXT)")

    print("認識してほしい言葉を入力して下さい。")
    word_in = input(">> ")
    print("\nそれに対する音声での返答を入力して下さい。")
    word_out = input(">> ")

    print("\nこの応答に対するラベルを選択して下さい。ラベルを選択しない場合はEnterを押して下さい。(API機能使用の場合はapi,画像表示使用の場合はimage)")
    word_label = input(">> ")
    if word_label == "":
        word_label = "normal"
        word_selec = "none"
    else:
        print("\n使用する機能を選択して下さい。(ニュース使用の場合はnews,天気の場合はweather,画像表示の場合はファイル名)")
        word_selec = input(">> ")

    # INSERT
    cursor.execute("INSERT INTO return VALUES (?, ?, ?, ?)", (word_in, word_out, word_label, word_selec))

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

else:
    print("\n応答追加完了")

db_con.commit()
db_con.close()
