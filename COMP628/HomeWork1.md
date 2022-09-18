# HomeWork1 - Introduction to Networking

## Jiapeng Pei S01435611

### Tasks

#### Question 1.1:

  The Network layer.

#### Question 1.2:
  
  Transport Layer.

#### Question 2.1:

  10.256.34.222 is not a valid IP address. Since each number contains only 8 digits, so the range of numbers is [0, 255]. 256 exceeds this range.

#### Question 2.2:

  Yes. All of the numbers are in [0, 255].

#### Question 3.1:

  I think it depends. If someone need to ensure the integrity of information, like sending an e-mail or making a transaction, it is better to use TCP. This person needs to make sure all the data is transferred properly. If someone is watching a live on the internet, UDP is better for its speed and efficiency. In this case the person can afford an occasional hiccup.

#### Question 3.2

  UDP.

#### Question 4.1 

  In these applications, reliablity is more important, since it guarantees the dilivery of data to destination router. For example, when I am using SSH, I don't want my data get missed.
  Bonus: Firstly without IP address, we cannot set up TCP connections. Secondly DHCP in connectionless, thus inherently fits UDP.

### Questions

1. An IP address is a specific and unique address in that network which allows information to be sent and received by the connected device in question. It is a 32 bit binary number with the format of: x.x.x.x, where x represents a 8 bit binary number ranging from 0 to 255.

2. TCP is connection-oriented. TCP ensures the complete and corrent delivery of data in logical order. It is used when reliablity is more important. UDP is connectionless. UDP doesn't ensure the completeness and sequentiality of tranferred data. But it is very fast and efficient. We could use UDP where the importance of speed overwhelms that of integrity. 

3. Application Layer, Transport Layer, Network Layer, Data Link Layer and Physical Layer.

4. Application Layer.

5. Port 67/68.
