import os
import copy
import sys

keyToFind = "AKIAIVFDJXSPEUEXITOA"
users = []
userVar = os.popen("aws iam list-users").read()
userLines = userVar.split("\n")
for line in userLines:
    if "UserName" in line:
        arr = line.split('"')
        users.append(copy.copy(arr[3]))

keysFound = []
user = None
status = None
date = None
key = None

for user in users:
    keyLines = os.popen("aws iam list-access-keys --user " + user).read().split("\n")
    for line in keyLines:
        if "UserName" in line:
            arr = line.split('"')
            user = copy.copy(arr[3])
        if "Status" in line:
            arr = line.split('"')
            status = copy.copy(arr[3])
        if "CreateDate" in line:
            arr = line.split('"')
            date = copy.copy(arr[3])
        if "AccessKeyId" in line:
            arr = line.split('"')
            key = copy.copy(arr[3])

            if(key == keyToFind):
                keysFound.append(copy.copy([user, status, date, key]))
            user = None
            status = None
            date = None
            key = None

print keysFound


