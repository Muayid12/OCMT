#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {


// delcare variables 
char ch;
ifstream file;
int character = 0;
string myline;
int line= 0;
int word = 1;
int numbers = 0;
int spaces = 0;



// getting word number 
file.open("Muayid.txt", ios::in);
file.unsetf(ios::skipws); 
while (1) {
file >> ch;
if (file.fail()) break;
character++;
if (ch == ' ' || ch== '\n') 
word++;
}

 
file.close();

// getting line
file.open("Muayid.txt", ios::in);
file.unsetf(ios::skipws); 
while (getline(file,myline))
{
    line++;   
} 

file.close();


// getting number 
file.open("Muayid.txt", ios::in);
file.unsetf(ios::skipws); 
while(file.get(ch))
{
    if(isdigit(ch))
    {
        numbers++;
    }
}

file.close();


// number of space
file.open("Muayid.txt", ios::in);
file.unsetf(ios::skipws); 
while (1) {
file >> ch;
if (file.fail()) break;
if (ch == ' ') 
spaces++;
}
file.close();


// display Statistics
cout << "\n Total lines = " << line << " lines \n";
cout << " Total Word = " << word << " words \n";
cout << " Total Character = " << character << " characters \n";
cout << " Total Numbers = " << numbers << "\n";
cout << " Total Space = " << spaces << "\n";
cout << " Percentage of numbers = " <<((double(numbers)/double(character))*100)<<"%\n";

return 0;

}
