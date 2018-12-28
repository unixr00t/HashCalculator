#!/bin/python2.7

import hashlib
import sys
import os

path = raw_input("Enter the path of your file:\n")
assert os.path.exists(path), "Did not find the file at," +str(path)
print("\nFound your file! Hash will be calculated soon!!\n")

#Calculating MD5 Hash

hasher = hashlib.md5()
file = open(path,'rb')
buf = file.read()
a = hasher.update(buf)
md5_a = (str(hasher.hexdigest()))
print("MD5 Hash = " +md5_a)

#Calculating SHA1 Hash

sha_1 = hashlib.sha1()
b = sha_1.update(buf)
sha1_b = (str(sha_1.hexdigest()))
print("\nsha1 hash = " +sha1_b)

with open('result.txt', 'w') as result:
	result.write("Path Of your File = " + path + "\n")
	result.write("MD5 Hash = " + md5_a + "\n")
	result.write("SHA1 Hash = " + sha1_b + "\n")
result.close()
#end