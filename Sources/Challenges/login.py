import hashlib
import os
resource_file = "passwords.txt"
def encode(username,password):
    return "$%s::%s$"%(username,hashlib.sha1(password).hexdigest())
def add_user(username,password):
    if os.path.exists(resource_file):
        with open(resource_file) as f:
            if "$%s::"%username in f.read():
                raise Exception("user already exists")
    with open(resource_file,"w") as f:
         print >> f, encode(username,password)
    return username
def check_login(username,password):
    with open(resource_file) as f:
        if encode(username,password) in f.read():
           return username

def create_username():
     try: 
         username = add_user(raw_input("enter username:"),raw_input("enter password:"))
         print "Added User! %s"%username
     except Exception as e:
         print "Failed to add user %s! ... user already exists??"%username
def login():
     if check_login(raw_input("enter username:"),raw_input("enter password:")):
        print "Login Success!!"
     else:
        print "there was a problem logging in"

while True:
    {'c':create_username,'l':login}.get(raw_input("(c)reate user\n(l)ogin\n------------\n>").lower(),login)()

