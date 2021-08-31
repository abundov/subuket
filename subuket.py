# SuBuket v1.0
# Coded by kaiz3n

import os, sys

print()
print("Okay let's do this in Python 3")
print(" ____________________")
print("< S u B u k e t v1.0 >")
print(" --------------------")
print("        \   ^__^")
print("         \  (oo)\_______")
print("            (__)\       )\/")
print("                ||----w |")
print("                ||     ||")
print()                             
print("Subuket v1.0 - Subdomain S3 Bucket Checker")
print("Make sure you are in the sublist3r directory and you have python3 installed")
print("Run the command like this: python3 subuket.py some.domain.com")
print()
print()
print()
command = 'python3 sublist3r.py -o results.txt -d ' + sys.argv[1]
os.system(command)
print()
print()
print("Now we need to run 'aws s3 ls s3://some.domain.com' but on all the subdomains found")
print("Make sure you have aws installed with a key")
filepath = 'results.txt'
with open(filepath) as testy:
    line = testy.readline()
    count = 1
    while line:
        command1 = 'aws s3 ls s3://' + line.strip()
        line = testy.readline()
        os.system(command1)
        print("-------------------------------------")
        print("Subdomain {}: ".format(line.strip()))
        print()
