namespace rzikm_CreditTest;

public class ArgumentException : System.Exception
{
    public ArgumentException() {}
    public ArgumentException(string message) : base(message) {}
    public ArgumentException(string message, System.Exception inner) : base(message, inner) {}
}

public class FileException : System.Exception
{
    public FileException() {}
    public FileException(string message) : base(message) {}
    public FileException(string message, System.Exception inner) : base(message, inner) {}
}

public class ParseException : System.Exception
{
    public ParseException() {}
    public ParseException(string message) : base(message) {}
    public ParseException(string message, System.Exception inner) : base(message, inner) {}
}