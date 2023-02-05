namespace rzikm_CreditTest;
class Program
{
    static void Main(string[] args)
    {
        Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");
        Console.WriteLine("Program started");
    
        Logo app = new();
        app.Execute(args);
        Console.WriteLine("Program finished");

        // TODO: Unittests
        //Console.ReadLine();
    }
}
