
## RPiMorse
RPiMorse is a simple Morse code system for the Raspberry Pi. It comes with a working CLI which allows the user to input text to be converted to Morse code.
It uses the RPi's GPIO to set a pin as high and low at a pre-defined frequency. This has been tested with an LED, however, it may work with any device that takes a basic pin output.

## Motivation
RPiMorse was created as a learning experience on how to control the GPIO pins using C++.

## Frameworks
**Built with**
- [wiringPi](https://wiringpi.com)

## Features
Somewhat modular code, to allow control of any pin with any device.

## Installation
Step 1:
```
g++ -Wall RpiMorse.cpp -o RPiMorse -lwiringPi
```

To run:
```
./RPiMorse
```

And example of what it will look like when you're running it:
```
Line (q to quit): Please make me a sandwich
Line (q to quit): q
```

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contributing
Feel free to report any bugs or enhancements, as well as make pull requests. My only condition is that you follow the same formatting standard as the rest of the code.
