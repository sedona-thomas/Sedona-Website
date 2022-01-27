/*
 * Sedona Thomas
 * thisFile.h: header file 
 */

#ifndef __METHOD_H__
#define __METHOD_H__

// class: private by default
class Class
// struct: public by default
//struct Struct
// rename with following command: ":%s/Name/{Class_or_Struct_name}/g"
{
public:
    
    // default constructor
    Name();

    // constructor
    Name(int _x);//(int _x = 0)

    // copy constructor
    Name(const Name& orig);

    // copy assignment
    Name& operator=(const Name& rhs);

    // destructor
    ~Class();

    // move constructor
    Name(Name&& orig);

    // move assignment
    const Name& operator=(const Name& rhs);
    
    // bool operator
    operator bool(const Name& rhs) const { return (x != 0); }
    
    // put-to operator
    friend std::ostream& operator<<(std::ostream& os, const Name& rhs);

    // get-from operator
    friend std::istream& operator>>(std::istream& is, Name& rhs);

    // operator[]
    char& operator[](int i) { return list[i]; }

    // operator[] const
    const char& operator[](int i) const { return list[i]; }

    // size()
    size_t size() const { return list.size(); }
    
    // method:
    void method(T v); //const

private:

    int x;
    std::vector<int> list;
    // variables

}

// operator+
Name& operator+(const Name& lhs, const Name& rhs);

// operator-
Name& operator-(const Name& lhs, const Name& rhs);

// functor    
struct functor                                                                                                                                                                            
{             
    template<typename T>
    void operator() (const T& obj)
    {         
        //functor body
    }         
};            

#endif
