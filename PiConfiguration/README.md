## Raspberry Pi Setup Documentation:

### GUI setup:
Since we are using PyQt4 and other libraries in our GUI code, we need to run a few commands to make sure they are supported and the code does not fail.

```shell
sudo apt-get install python-qt4
pip install pygatt
pip install pexpect
```

### Code Update:
In order to run "updateCode.sh", first we need to run:

```shell
sudo apt-get install xterm
```



### Remote Control Setup:
First, vnc server must be installed **on the Pi** by running:
```shell
sudo apt-get install tightvncserver
```
Then we activate the server by running:
```shell
vncserver -nolisten tcp -nevershared -dontdisconnect :1
```
This command will prompt you for a password that you will need from the client side to connect.

Once this is setup, we can remote control the Pi screen from our own OS.
