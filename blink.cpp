#include <wiringPi.h>

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

#define GPIO18 1

void setup();
void pinHigh(int pin);
void pinLow(int pin);
std::string parseLine(std::string line);
std::string getCode(char alphaNumeric);
void showCode(std::string code, int pin);
std::vector<std::string> split(std::string s, std::string delim);

int main() {
	setup();
	
	std::string input;
	
	std::vector<std::string> test;
	
	do {
		std::cout << "Line (q to quit): ";
		std::getline(std::cin, input);
		
		if(input == "q" || input == "quit") break;
		
		std::string code = parseLine(input);
		showCode(code, GPIO18);
		
	} while(true);
	
	return 0;
}

void setup() {
	wiringPiSetup();
}

void pinHigh(int pin) {
	digitalWrite(pin, HIGH);
}

void pinLow(int pin) {
	digitalWrite(pin, LOW);
}

std::string parseLine(std::string line) {
	std::string code = "";
	for(char &c : line) {
		if(c == ' ') {
			code += "WORD";
			continue;
		}
		code += getCode(tolower(c));
		// Writing some hacks to make punctuation work correctly
		if(c == '.') {
			code += "STOP";
		}
		
		code += " ";
	}
	
	return code;
}

std::string getCode(char alphaNumeric) {
	switch(alphaNumeric) {
		case 'a': return ".-";
		case 'b': return "-...";
		case 'c': return "-.-.";
		case 'd': return "-..";
		case 'e': return ".";
		case 'f': return "..-.";
		case 'g': return "--.";
		case 'h': return "....";
		case 'i': return "..";
		case 'j': return "";
		case 'k': return "";
		case 'l': return ".-..";
		case 'm': return "--";
		case 'n': return "-.";
		case 'o': return "---";
		case 'p': return ".--.";
		case 'q': return "--.-";
		case 'r': return ".-.";
		case 's': return "...";
		case 't': return "-";
		case 'u': return "..-";
		case 'v': return "...-";
		case 'w': return ".--";
		case 'x': return "-..-";
		case 'y': return "-.--";
		case 'z': return "--..";
		case '0': return "-----";
		case '1': return ".----";
		case '2': return "..---";
		case '3': return "...--";
		case '4': return "....-";
		case '5': return ".....";
		case '6': return "-....";
		case '7': return "--...";
		case '8': return "---..";
		case '9': return "----.";
		case '.': return ".-.-.-";
		case ',': return "--..--";
		case ':': return "---...";
		case '?': return "..--..";
		case '\'': return ".----.";
		case '-': return "-....-";
		case '/': return "-..-.";
		case '(':
		case ')': return "-.--.-";
		case '"': return ".-..-.";
		case '@': return ".--.-.";
		case '=': return "-...-";
		default: return "";
	}
}

void showCode(std::string code, int pin) {
	// Takes parsed code, then parses it into the pin
	// to output Morse code
	const int DELAY = 500;
	
	// This is where it gets confusing...
	// Split the code into sentences, by splitting where it says STOP
	std::vector<std::string> splitByStop = split(code, "STOP");
	for(auto line : splitByStop) {
		// Next, we need the sentence split into words
		// So split line by WORD
		std::vector<std::string> words = split(line, "WORD");
		
		// Now loop through each word
		for(auto word : words) {
			// Now split each word into characters, which
			// is easily done through spaces
			std::vector<std::string> chars = split(word, " ");
			
			// And now we go through each character, which is already split
			// into the working code, so...
			// Also, have to manually convert from string to char
			for(auto morseCode : chars) {
				// Finally made it to the end,
				// where we can output the code!
				for(char dotOrDash : morseCode) {
					pinHigh(pin);
					if(dotOrDash == '.') {
						std::cout << "DOT\n";
						delay(DELAY);
					}
					else {
						std::cout << "DASH\n";
						delay(DELAY*3);
					}
					pinLow(pin);
					delay(DELAY);
				}
			}
			
			// Finally, delay for the proper amount of time
			// which is 3 units of time (one unit is already delayed
			// by the previous loop)
			delay(DELAY*2);
		}
		
		// Finally, delay for the proper amount of time.
		// In this case, because the word has already delayed,
		// I will be using a smaller value here, but it will
		// still come out to the be right time delay (7 units of time)
		delay(DELAY*4);
	}
	
}

std::vector<std::string> split(std::string s, std::string delim) {
	std::vector<std::string> tokens;
	std::string token;
	size_t pos = 0;
	
	while((pos = s.find(delim)) != std::string::npos) {
		token = s.substr(0, pos);
		tokens.push_back(token);
		s.erase(0, pos + delim.length());
	}
	tokens.push_back(s);
	
	return tokens;
}
