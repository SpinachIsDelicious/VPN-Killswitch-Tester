
# VPN Killswitch Testing Script

### Have Python Installed
### Have a server with a public IP address
### Edit [client.py](https://github.com/SpinachIsDelicious/VPN-Killswitch-Tester/blob/main/Client.py) to send a request to your server

To start, run the [server.py](https://github.com/SpinachIsDelicious/VPN-Killswitch-Tester/blob/main/Server.py) script on tmux preferably in your server (If you're sshed from the client)
Now, run [client.py](https://github.com/SpinachIsDelicious/VPN-Killswitch-Tester/blob/main/Client.py) on your system with the VPN connected and then disconnect with a strict kill switch
After this small connection drop, you can close out of [client.py](https://github.com/SpinachIsDelicious/VPN-Killswitch-Tester/blob/main/Client.py) and check your server for any connection drops leading to your actual VPN connected machine's IP address
## To do:
### Add threading
### Add other protocols instead of http
