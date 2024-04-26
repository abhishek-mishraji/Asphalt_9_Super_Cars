


using System;

class Anonymous_type
{

    public static void anonymous_type_display()
    {
        var v = new
        {
            name = "abhishek",
            age = 21,
            degree = "Engineer"
        };

        Console.WriteLine("Name: {0}, Age: {1}, Degree: {2}", v.name, v.age, v.degree);
    }

    public static void Main(string[] args)
    {
        anonymous_type_display();
    }
}
