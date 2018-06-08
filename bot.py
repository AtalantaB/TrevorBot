'''Trevor Bot: Internet Relay Chat Bot that responds to various keywords.
Use instructions under readme.txt'''

from irc import *
import re, os, random, time, timeit

channel = '#jk1984' #Channel to connect to.
port = 6667 #port to connect with
server = 'chat.freenode.net' #Server to connect to
nickname = 'TrevorBot' #Nickname of bot
adminName = 'Dracoliat' #Nickname of admin of bot.
triggers = {'.stop':0, 'hello':1, 'roach':2, 'cockroach':2, 'trevor':3}

irc = IRC() #setup class
irc.connect(server, port, channel, nickname) #connect to server

def selfMsg(chan, msg, hst): #called when bot sends a message to a user
    irc.send(chan, msg) #sends message to server
    print('%s PRIVMSG %s :%s' % (hst, chan, msg)) #prints bot's own message.

    
host = ''

#prints like normal until the host has joined a channel
while host == '': 
    text = irc.get_text()
    print(text)

    #Checks if bot joins channel and if host not set
    if text.split(' ',3)[1] == 'JOIN':

        #sets host and ends loop moving into main loop.
        host = text.split(' ',3)[0] 
    else:
        pass #repeats loop.
    

#RUNTIME TESTING
#END OF RUNTIME TESTING

#main loop
while 1:

    #Get most recent text.
    text = irc.get_text()

    
    #doesn't print pings.
    if not text.startswith('PING :'): 
        print(text)
        
    name = ''
    content = ''
    
    
    if channel in text:

        #split name from rest of msg.
        try:
            name = text.split('!', 1)[0][1:]
        except:
            name = name
                

        #Check if message sent by user.
        if 'PRIVMSG' in text and any([x in text.split(' ',3)[3][1:] for x in triggers.keys()]):

            #Holds results of triggers.
            triggered = [triggers[x] for x in triggers.keys() if x in text.split(' ',3)[3][1:]]
            content = text.split(' ',3)[3][1:]

            #Commands
            if 0 == triggered[0] and name.lower() == adminName.lower(): 
                irc.quit()
                
            #send Hi Name! if it sees the world hello
            if 1 == triggered[0]:
                message = 'Hi ' + name + '!'
                selfMsg(channel, message, host)

            #send response if detects word 'roach' or 'cockroach'
            if 2 == triggered[0]:
                selfMsg(channel, '@ %s #TrevorForget ' % (name) +
                        'https://www.csoonline.com/article/3227910/security/hackers-create-memorial-for-a-cockroach-named-trevor.html', host)

            #send response if detects word 'trevor'
            if 3 == triggered[0]:
                selfMsg(channel, '@%s I\'m sad too, but Trevor will always live on in our hearts. #TrevorForget' % (name), host)



        #If new user joins channel.
        if text.split(' ')[1]=='JOIN':
            selfMsg(channel, 'Welcome ' + name + ' #TrevorForget', host)
    
