
## RPiMorse
RPiMorse is a simple Morse code system for the Raspberry Pi. It comes with a working CLI which allows the user to input text to be converted to Morse code.
It uses the RPi's GPIO to set a pin as high and low at a pre-defined frequency. This has been tested with an LED, however, it may work with any device that takes a basic pin output.

## Motivation
RPiMorse was created as a learning experience on how to control the GPIO pins using C++.

## Frameworks
**Built with**
- [RPIO](https://pythonhosted.org/RPIO/)
- [PyQt5](https://pypi.python.org/pypi/PyQt5)

## Features
- Modular code
- GUI

## Installation
Step 1 (install RPIO and PyQt5):
Raspbian:
```
$ sudo pip3 install RPIO
$ sudo apt-get install python3-pyqt5
```
![](https://photos-2.dropbox.com/t/2/AAALi2s27NQDJU29BMdNtFbGztDJZv9T11azJyWOhaO-ng/12/211939994/png/32x32/1/_/1/2/2018-04-07-001506_800x600_scrot.png/EPu0358BGP0WIAcoBw/Eb5acC-x6gQGZAt1ujS2fkLqKQVvWoxvcsgLbyh0zM4?preserve_transparency=1&size=1600x1200&size_mode=3)

![](https://photos-2.dropbox.com/t/2/AACr39midKJLMVvOoYbkpHdrl2B1uMy3rVCg5zeb9EgwQg/12/211939994/png/32x32/1/_/1/2/2018-04-07-001528_800x600_scrot.png/EPu0358BGP4WIAcoBw/52Q5IwfEyDI8Jg73JpTJCeHJLvPJKekpwGj_VjowOSQ?preserve_transparency=1&size=1600x1200&size_mode=3)
## Running
```
python3 main.py
```
Currently there is no toggle for CLI mode, so the application will always open as a GUI. This may change in a later update.

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contributing
Feel free to report any bugs or enhancements, as well as make pull requests. My only condition is that you follow the same formatting standard as the rest of the code.
