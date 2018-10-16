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
    state = "rec"
    xml_file = open('res.xml', 'w')
    xml_file.write("<ROOT>\n")
    xml_file.close()

    xml_file = open('res.xml', 'a')

    # rec
    print("録音終了する場合はEnterを入力")
    while state == "rec":
        response = client.recv(4096).decode('utf-8')
        response_rep = response.replace('<s>','')
        xml_file.write(response_rep.replace('</s>',''))

    # get words from res.xml
    xml_file.write("</ROOT>")
    xml_file.close()
    tree = ElementTree.parse(XMLFILE)
    root = tree.getroot()
    for ROOT in root:
        for SHYPO in ROOT:
            for WHYPO in SHYPO:
                if WHYPO.attrib["WORD"] != "":
                    words.append(WHYPO.attrib["WORD"])

    # serch database
    print(words)
    for r_words in (reversed(words)):
        cursor.execute('SELECT * FROM return WHERE input=?',(r_words,))
        return_word = cursor.fetchone()
        if return_word != None:
            if return_word[1] == "news":
                news = module.return_news(words)
                pyj.say(news)
                break
            elif return_word[1] == "weather":
                weather = module.return_weather(words)
                pyj.say(weather)
                break
            else:
                pyj.say(return_word[1])
                break

    print("継続する場合はEnter,終了する場合はexitと入力して下さい")
    in_over = input(">>")
    if in_over == "exit":
        over_rall = False

# finish process
thread.join()
db_con.close()
