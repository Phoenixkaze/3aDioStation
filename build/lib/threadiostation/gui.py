from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from urllib.parse import quote
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

import os
import socket
import struct
import sys
import threading
import time
import urllib
import locale
import io

import simplelocalize

def launch():
    global server, sock
    if filePath.get().strip() == '':
        messagebox.showwarning(localiDict['nofilemsg']['title'], localiDict['nofilemsg']['msg'])
        return
    if not filePath.get().endswith(('.cia', '.3dsx', '.cetk', '.tik')):
        messagebox.showerror(localiDict['fileerrormsg']['title'], localiDict['fileerrormsg']['msg'])
        return
    if _3dsIp.get().strip() == '':
        messagebox.showwarning(localiDict['3dsiperrormsg']['title'], localiDict['3dsiperrormsg']['msg'])
        return
    launchButton.state(['disabled'])
    stopButton.state(['!disabled'])
    server = TCPServer(('', int(port.get())), SimpleHTTPRequestHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def serve(stopE: Event):
        server.serve_forever()
        while not stopE.isSet():
            continue
        server.shutdown()
    thread = threading.Thread(target=serve, args=(stopEvent,))
    thread.start()
    try:
        payloadBytes = (f"{ip.get()}:{port.get()}/" + quote(os.path.basename(filePath.get()))).encode('ascii')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((_3dsIp.get(), 5000))
        sock.sendall(struct.pack('!L', len(payloadBytes)) + payloadBytes)
        def rec(stopE: Event):
            while len(sock.recv(1)) < 1 and not stopE.isSet():
                time.sleep(0.05)
                sock.close()
        t = threading.Thread(target=rec, args=(stopEvent,))
        t.start()
    except Exception as e:
        messagebox.showerror("Error", 'An error occurred: ' + str(e))
        server.shutdown()
        sock.close()

def stop():
    if server:
        stopEvent.set()
        #sock.close()
        server.shutdown()
        stopButton.state(['disabled'])
        launchButton.state(['!disabled'])

def selectFile():
    global payloadBytes
    filePath.set(filedialog.askopenfilename(filetypes=[('cia files','*.cia'), ('3dsx file','*.3dsx')]))
    directory = os.path.dirname(filePath.get())
    if directory != ".":
        os.chdir(directory)
    

payloadBytes = None
localiDict = simplelocalize.setupLocalization()
root = Tk()
root.title("3aDioStation")

ip = StringVar(value=socket.gethostbyname(socket.gethostname()))
port = StringVar(value="8080")

sock = None
server = None
stopEvent = threading.Event()

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tipLabel = ttk.Label(mainFrame, text=localiDict['filetip'])
tipLabel.grid(row=0, column=0, columnspan=4, sticky=(W))

filePath = StringVar()
fileEntry = ttk.Entry(mainFrame, textvariable=filePath)
fileEntry.grid(row=1, column=0, columnspan=3, sticky=(W, E))

browseButton = ttk.Button(mainFrame, text=localiDict['browsebtn'], command=selectFile)
browseButton.grid(row=1, column=3)


ttk.Label(mainFrame, text="IP").grid(row=2, column=0)
ttk.Entry(mainFrame, textvariable=ip).grid(row=2, column=1, sticky=(W, E))
ttk.Label(mainFrame, text=localiDict['port']).grid(row=2, column=2)
ttk.Entry(mainFrame, textvariable=port, width=4).grid(row=2, column=3)

_3dsIp = StringVar()
ttk.Label(mainFrame, text=localiDict['3dsip']).grid(row=3, column=0)
ttk.Entry(mainFrame, textvariable=_3dsIp).grid(row=3, column=1)

stopButton = ttk.Button(mainFrame, text=localiDict['stopbtn'], command=stop)
stopButton.grid(row=5, column=2)
stopButton.state(['disabled'])

launchButton = ttk.Button(mainFrame, text=localiDict['launchbtn'], command=launch)
launchButton.grid(row=5, column=3)

mainFrame.bind("<Destroy>", lambda e: stop())
root.mainloop()