# SuBuket v1.0
# Check subdomains for Open S3 buckets
# Coded by kaiz3n

Basically, this tool makes use of another tool (sublist3r) to fetch subdomains, and then checks to see if those subdomains might be an Open AWS S3 bucket which can be read and/or written to using the (aws cli) tool.


This is a very, very basic and hardcoded version so please make sure that:
1) You have python3 installed
2) You have installed sublist3r by running "git clone https://github.com/aboul3la/Sublist3r.git" and are in the directory before attempting to run SuBuket
3) The syntax is: "python3 subuket.py some-domain.com"
4) Have fun!


Disclaimer: Use this tool at your own risk and make sure you follow all laws. It is meant to be an Ethical web-application testing tool to help secure companie's S3 buckets, thus preventing data loss and/or leaks. 


SuBuket is licensed under the GNU GPL license.
