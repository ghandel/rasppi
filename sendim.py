#!/usr/bin/env python

"""
testing seding instant message
"""

import xmpp

username = ''
passwd = ''
to='someone@example.com'
msg='hello :)'


client = xmpp.Client('gmail.com')
client.connect(server=('talk.google.com',5223))
client.auth(username, passwd, 'botty')
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
client.send(message)
