from pyjtalk.pyjtalk import PyJtalk
from xml.etree import ElementTree
import socket
import threading

# setting
pyj = PyJtalk()
HOST = "localhost"
PORT = 10500
XMLFILE = "res.xml"
flag = True

# socket setting
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# thread set
def wait_input():
    global flag
    input()
    flag = False

thread = threading.Thread(target=wait_input)
thread.start()

# main process
while flag:
    # before setting
    words = []
    xml_file = open('res.xml', 'w')
    xml_file.write("<ROOT>\n")
    xml_file.close()

    xml_file = open('res.xml', 'a')

    # rec
    print("録音終了する場合はEnterを入力")
    while flag:
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

    # return voice

# finish process
thread.join()
