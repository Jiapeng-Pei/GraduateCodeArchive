# COMP 628 Homework 3
## Jiapeng Pei S01435611

### Task 1.
#### a.
ICANN is a nonprofit organization to help the U.S. government manage certain functions that maintain the Internet's core infrastructure. It dedicated to keeping the Internet secure, stable and interoperable. Since ICANN maintains the central repository for IP addresses and manages the domain name system and root servers, they are authoritative source for whois information.

#### b.
Domains By Proxy, LLC

#### c.
raymondlawoffice.com

### Task 2.
#### a. 
The default for the type option is A. Some other possible types inlucde AAAA, CNAME, MX and NS.

#### b. 
The IP address is 169.254.169.253

#### c.
-x simplifies reverse lookups for mapping addresses to names. When the -x is used, there is no need to provide the name, class and type arguments. 

#### d.
The result is different from that of using nslookup. Following are the last lines of the result:
;; Query time: 4 msec
;; SERVER: 169.254.169.253#53(169.254.169.253)
;; WHEN: Thu Sep 22 06:17:00 UTC 2022
;; MSG SIZE  rcvd: 115

#### e.
The domain name is dns.google.

### Task 3.
a. 
	1. 10.1.49.247
	2. 255.255.240.0
	3. 4096

b.
	1. nmap -sn 10.1.49.247/20
	2. 10.1.51.32
		10.1.58.108
		10.1.61.225

c.
(1)      IP Address           "Open" ports
	1.   10.1.51.32            21
	2.   10.1.58.108          22, 80, 139, 445
	3.   10.1.61.225          80

(2) 10.1.58.108 & 10.1.61.225