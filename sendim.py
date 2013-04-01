#!/usr/bin/env python

"""
testing seding instant message
"""

import xmpp

username = 'ghandel333'
passwd = 'Iluvmurr<3!'
to='ghandel@wisc.edu'
msg='hello :)'


client = xmpp.Client('gmail.com')
client.connect(server=('talk.google.com',5223))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
client.send(message)
