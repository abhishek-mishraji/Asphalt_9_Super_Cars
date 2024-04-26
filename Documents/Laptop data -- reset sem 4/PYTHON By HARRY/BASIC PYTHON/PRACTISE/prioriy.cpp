// 1 derive class but have multiple base class

// class DerivedC: visibility-mode base1, visibility-mode base2
// {
//      Class body of class "DerivedC"
// };
#include <iostream>
#include <iomanip>
using namespace std;

class Base1
{

public:
    // void set_base1int()
    // {
    //     cout << "Base 1";
    // }
};

class Base2
{

public:
    // void set_base1int()
    // {
    //     cout << "Base 2";
    // }
};

class Base3
{

public:
    void set_base1int()
    {
        cout << "Base 3";
    }
};
class Derived : public Base1, public Base2, public Base3
{
public:
    // void set_base1int()
    // {
    // }
};
int main()
{
    Derived harry;
    // harry.set_base2int();
    harry.set_base1int();
    return 0;
}
