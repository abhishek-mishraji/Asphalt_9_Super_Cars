
namespace visual_console
{

    enum Days
    {
        Sunday,
        Monday,
        Tuesday,
        Wednesday=88,
        Thursday,
        Friday,
        Saturday
    }
    internal class Enumm
    {
        public
        void display()
        {
           const int x = (int)Days.Sunday;
            Console.WriteLine(x);
            const int y = (int)Days.Wednesday;
            Console.WriteLine(y);
            const int z = (int)Days.Thursday;                
            Console.WriteLine(z);
            const int aa = (int)Days.Friday;
            Console.WriteLine(aa);


        }
    }
}