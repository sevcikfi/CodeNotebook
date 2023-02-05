namespace rzikm_CreditTest;

class Logo
{
    const string FILEOUT = "out.html";
    const string HEADER = 
@"<!DOCTYPE html> 
<html><body>
<svg width='500' height='500'> 
<style type='text/css'> 
<![CDATA[ 
line { stroke: rgb(0, 0, 0); stroke-width:2} 
]]> 
</style>";
    const string FOOTER = "</svg></body></html>";

    public Logo(){}
    
    public void Execute(string[] args)
    {
        try
        {
            if (args.Length != 1) throw new ArgumentException("Argument error");

            string[] raw = ReadFile(args[0]);
            List<string> svgLines = new();
            Parse(raw, svgLines);
            WriteFile(svgLines.ToArray());
        }
        catch (ArgumentException ex)
        {
            Console.Error.WriteLine(ex);
        }
    }

    public string[] ReadFile(string filepath = "test.logo")
    {
        Console.WriteLine("Trying to read file...");
        try
        {
            return File.ReadAllLines(filepath);
        }
        catch (System.Exception)
        {
            throw new FileException("File error");
        }
    }

    public void Parse(string[] toParse, List<string> outLines){
        List<String> repeat = new();
        int repeatNum = 0;
        foreach (string line in toParse)
        {   
            
            switch(line.Split(" ")[0])
            {
                case "penup": 
                    Console.WriteLine("penup");
                    break;
                case "pendown": 
                    Console.WriteLine("pendown");
                    break;
                case "right": 
                    Console.WriteLine("penup");
                    break;
                case "forward": 
                    Console.WriteLine("penup");
                    break;
                case "repeat":
                
                case " ":
                    
                case "]":
                    for (int i = 0; i < repeatNum; i++)
                    {
                        Parse(repeat.ToArray(), outLines);
                    }
                    break;

                default: 
                    Console.WriteLine("rip");
                    throw new ParseException("Parse error");
                    break;
            }
        }
    }

    public void WriteFile(string[]? lines = null)
    {
        lines ??= new string[]{"<line x1='0' y1='0' x2='35.3553390593274' y2='35.3553390593274' />"};

        try
        {
        	using (StreamWriter sw = File.CreateText(FILEOUT))
        	    {
        	        Console.WriteLine("Started writing file");
        	        sw.WriteLine(HEADER);
        	        foreach (var line in lines)
        	        {
        	            sw.WriteLine(line);
        	        }
        	        sw.WriteLine(FOOTER);
        	        Console.WriteLine("Finished writing file");
        	    }
        }
        catch (System.Exception)
        {
        
        	throw;
        }
    }
}