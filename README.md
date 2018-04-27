
## RPiMorse
RPiMorse is a simple Morse code translator and transmitter, using an embedded server. It allows the user to type in plain English and generates the Morse Code. The user can then transmit the Morse Code to a configured server. If using the embedded server the code will appear in a third pane labeled "Received" and, if configured, will output to the "active pin", as set in the config dialog.

## Frameworks
**Built with**
- [RPIO](https://pythonhosted.org/RPIO/)
- [PyQt5](https://pypi.python.org/pypi/PyQt5)

## Features
- Modular code
- GUI
- Embedded Server

## Installation
Step 1 (install RPIO and PyQt5):
Raspbian:
```
$ sudo pip3 install RPIO
$ sudo apt-get install python3-pyqt5
```
![](/screenshots/window_1.png)

![](/screenshots/window_2.png)

![](/screenshots/config_window.png)

## Running
```
python3 main.py
```

There are also some arguments you can pass to control the application.

```
--ip [ip-address]
Controls the server's IP address

-- port [port-number]
Controls the server's port

--disable-server
Disables the internal server
```

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contributing
Feel free to report any bugs or enhancements, as well as make pull requests. My only condition is that you follow the same formatting standard as the rest of the code.

## Server
RPiMorse comes with a built-in socket server, [server.py](server.py). This will allow users to communicate between each other when the applications are open.

The server can be controlled through command-line arguments `--ip [ip-address]` and `--port [port-number]`. The server can also be disabled using `--disable-server` for when you want to use your own server.

This server uses port 2000 by default and does not pose any security risks on its own. It has been creating with the purpose of running on a local network and only talking to devices connected to this network.

### Creating your own server
Using a custom server should be really easy. The application only requires that the server it pings returns "Pong!" when it receives "Ping!".