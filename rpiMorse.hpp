#ifndef RPI_MORSE_HPP
#define RPI_MORSE_HPP

#include <string>
#include <vector>

#define GPIO18 1

namespace rpiMorse {
void setup();
void pinHigh(int pin);
void pinLow(int pin);
std::string parseLine(std::string line);
std::string getCode(char alphaNumeric);
void showCode(std::string code, int pin);
std::vector<std::string> split(std::string s, std::string delim);
}

#endif // RPI_MORSE_HPP
