import socket
import sys

import logging #Setup for debugging tools

# Logging Levels: 0-notset, 10-debug, 20-info, 30-warning, 40-error, 50-critical
activeLogLevel = 10 #
logging.basicConfig(level=20, format='%(levelname)s:%(asctime)s:%(message)s') #setup logging format.


class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(bytes("PRIVMSG " + chan + ' :' + msg + '\n','UTF-8'))

    def quit(self):
        print('Exit Code Detected: Shutting Down')
        self.irc.send(bytes('QUIT \n','UTF-8'))
        sys.exit()

    def connect(self, server, port, channel, botnick):

        print('Connecting to: %s' % server)
        self.irc.connect((server, port))
        self.irc.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :This is a fun bot!\n",'UTF-8'))
        self.irc.send(bytes("NICK " + botnick + "\n",'UTF-8'))
        self.irc.send(bytes("JOIN " + channel + "\n",'UTF-8'))
        

    def get_text(self):
        text = self.irc.recv(2040).decode('UTF-8').strip('\n\r')
        if text.find('PING') != -1:
            self.irc.send(bytes('PONG :pingis\n','UTF-8'))

        return text
