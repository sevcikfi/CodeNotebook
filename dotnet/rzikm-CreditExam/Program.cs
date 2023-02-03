namespace rzikm_CreditTest;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("おはよう World!");
        Console.Error.WriteLine("rzkm testing!");
        String unicodeString =
            "This Unicode string has 2 characters outside the " +
            "ASCII range:\n" +
            "Pi (\u03a0), and Sigma (\u03a3).";
        Console.WriteLine(unicodeString);

        
        Console.ReadKey();
    }
}
