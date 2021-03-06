# -*- coding: utf-8 -*-
import re
import time

def filter_events(event):
    # You can modify event attribute, or disable (filter) event, returning False
    # Sample processing below
    emailre_ = re.compile(r"(?P<email>[-a-z0-9_.]+@(?:[-a-z0-9\.]+))",
                    re.IGNORECASE)

    if event.date > time.time()*1000:
       return False # Something wrong — event from future

    if event.author.startswith("jelmer"):
       event.author="jelmer@samba.org"      
    event.author = event.author.lower().replace('"',"'")
    m = emailre_.search(event.author)
    if m:
        event.author = m.group('email') 
    event.author = event.author.replace('"',"'")
    if event.author in ["(no author)"]:
        event.author = "anonymous"
    
    event.comment = re.sub('[Bb][Uu][Gg]\s*\d+\.?', '', event.comment)
    if event.comment.startswith("*** empty log message ***"):
        event.comment = ""

    if len(event.comment) < 10:
        event.comment = ""

    return True
