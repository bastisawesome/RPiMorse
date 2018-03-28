#include <string>
#include <iostream>
#include <QApplication>

#include "rpiMorse.hpp"
#include "mainwindow.h"

int main(int argc, char *argv[]) {
    rpiMorse::setup();

    std::string input;

    do {
     std::cout << "Line (q to quit): ";
     std::getline(std::cin, input);

     if(input == "q" || input == "quit") break;

     std::string code = rpiMorse::parseLine(input);
     rpiMorse::showCode(code, GPIO18);

    } while(true);

//    QApplication app(argc, argv);
//    MainWindow window;
//    window.show();

//    return app.exec();
}
