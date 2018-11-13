# coding:utf-8
from pyjtalk.pyjtalk import PyJtalk
from xml.etree import ElementTree
import socket
import threading
import sqlite3
import module

# setting
pyj = PyJtalk()
HOST = "localhost"
PORT = 10500
XMLFILE = "res.xml"
state = "rec"
over_rall = True

# database setting
DBPATH = 'return_db.sqlite'
db_con = sqlite3.connect(DBPATH)
cursor = db_con.cursor()

# socket setting
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# thread setting
def wait_input():
    global state
    global over_rall
    while over_rall:
        if state == "rec":
            input()
            state = "end_rec"

thread = threading.Thread(target=wait_input)
thread.start()

# main process
while over_rall:
    # before setting
    words = []
    say_flag = False
    state = "rec"
    response = ""
    xml_file = open('res.xml', 'w')
    xml_file.write("<ROOT>\n")
    xml_file.close()

    xml_file = open('res.xml', 'a')

    # rec
    client.recv(4096)
    print("録音終了する場合はEnterを入力")
    while state == "rec":
        response = client.recv(4096).decode('utf-8')
        response = response.replace('<s>','')
        xml_file.write(response.replace('</s>',''))

    # get words from res.xml
    try:
        xml_file.write("</ROOT>")
        xml_file.close()
        tree = ElementTree.parse(XMLFILE)
        root = tree.getroot()
        for ROOT in root:
            for SHYPO in ROOT:
                for WHYPO in SHYPO:
                    if WHYPO.attrib["WORD"] != "":
                        words.append(WHYPO.attrib["WORD"])
    except:
        print("読み込みエラーが発生しました")

    print("入力:")
    print(words)

    # serch database
    for r_words in (reversed(words)):
        cursor.execute('SELECT * FROM return WHERE input=?',(r_words,))
        return_word = cursor.fetchone()
        if return_word != None:

            # select label
            if return_word[2] == "plane":
                print("出力:")
                print(return_word[1])
                print("")
                pyj.say(return_word[1])
                say_flag = True
                break

            elif return_word[2] == "api":
                if return_word[3] == "news":
                    print("出力:")
                    print(return_word[1])
                    news = module.return_news(words)
                    news = return_word[1] + news
                    print("")
                    pyj.say(news)
                    say_flag = True
                    break

                elif return_word[3] == "weather":
                    print("出力:")
                    weather = module.return_weather(words)
                    weather = return_word[1] + weather
                    print(weather)
                    print("")
                    pyj.say(weather)
                    say_flag = True
                    break

            elif return_word[2] == "image":
                print("出力:")
                print(return_word[1])
                print("")
                pyj.say(return_word[1])
                module.return_map(return_word[3])
                say_flag = True
                break

    if say_flag == False:
        pyj.say("すみません。よくわかりません。")

    print("継続する場合はEnter,終了する場合はexitと入力して下さい")
    in_over = input(">> ")
    if in_over == "exit":
        over_rall = False

# finish process
thread.join()
db_con.close()
