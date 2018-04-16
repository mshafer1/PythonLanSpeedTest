# PythonLANSpeedTest
A Python based network speed test for Local Area Networks (script or pinch-hitter must be run on two separate computers)


## Usage
`speetTest.py [server IP] [message]`

If server is not specified, speetTest will open a port to act as the server [a basic Echo Server implementation](https://pymotw.com/2/socket/tcp.html).

If message is not specified, a portion of 'Lorem Ipsum' is used.


### Server 
The server portion of this script is a basic [Echo Server implementation](https://pymotw.com/2/socket/tcp.html).

This portion of the script could be replaced by any echo server that does not delay before responding (Usefull if you are not able to control the server you wish to test against, but it is running an echo server).
    
### Client
The client or test portion of the script times how long it takes to write a message to the echo server and get the reply. 

This is then scaled based on the data used to report the speed experienced in both bits per second and bytes per second.
 
## Units involved
| Source    | Note  |
| ---       | ---   |
| bits      | There are 8 bits per character in the string of the message sent (Ascii) |
| bytes     | 8 bits to a byte |
| Kilobit   | There are 1,000 bits to a kilobit [(only in networking - elsewhere it is 1024)](https://www.lifewire.com/network-data-rates-817365) |
| Megabit  | 1,000 kb or 1,000,000 bits [(again, only in networking)](https://www.lifewire.com/network-data-rates-817365) |
| etc.|