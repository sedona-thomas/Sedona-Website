/*
 * Sedona Thomas
 * main.cpp: main function definition
 */
#include <iostream>
#include <string>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <exception>
#include <iomanip>
#include <regex>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <array>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <iterator>

#include "template.h"

/*
 * Name() Class or Struct: defined in template.h
 */

// default constructor
Name()
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: (%p)->Name()\n", this);
    #endif 
    // body
}

// constructor
Name(int _x)//(int _x = 0)
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: (%p)->Name(int)\n", this);
    #endif 
    // body
    x = _x;
}

// copy constructor
Name(const Name& orig) 
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: (%p)->Name(const Name&)\n", this);
    #endif 
    // body
    x = orig.x;
}

// copy assignment
Name& operator=(const Name& rhs)
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: op=(const Name&)\n");
    #endif 
    // body
}

// destructor
~Class()
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: (%p)->~Name()\n", this);
    #endif 
    // body
}

// move constructor
Name(Name&& orig) : list{orig.list}, x{orig.x}
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: (%p)->Name(Name&&)\n", this);
    #endif
    // body 
    orig.x = 0;
    orig.list = nullptr;
}

// move assignment
const Name& operator=(const Name& rhs)
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: op=(const Name&)\n");
    #endif 
    if (this != &rhs)
    {
        // body
    }
    return *this;
}

// put-to operator
std::ostream& operator<<(std::ostream& os, const Name& rhs)
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: op<<(std::osstream&, Name&)\n");
    #endif 
    os << rhs.x;
    return os;   
}

// get-from operator
std::istream& operator>>(std::istream& is, Name& rhs)
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: op>>(std::isstream&, Name&)\n");
    #endif 
    int temp;
    is >> temp;
    s.x = temp;
    return is;
}

// method:
template <typename T> // generic variable
void method(T v) //const
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: method()\n");
    #endif 
    // body
}

/*
 * end of Name() Class or Struct
 */

// operator+
Name& operator+(const Name& rhs)
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: op+(const Name&)\n");
    #endif 
    // body
    return *this;
}

// operator+
Name& operator-(const Name& rhs)
{
    #ifdef BASIC4TRACE
        fprintf(stderr, "BASIC4TRACE: op-(const Name&)\n");
    #endif 
    // body
    return *this;
}

// main_namespace: contains main methods to be imported
namespace main_namespace
{
    // main():  
    int main()
    {
        using namespace std;
        // body
        return 0;
    }
}

// main():  
int main()//(int argc, char **argv)
{
    using namespace main_namespace;
    // body    
    return 0;
}


