//namespace rzikm_CreditTest;

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
        // TODO: Arg exception
        try
        {
            if (args.Length != 1) throw new System.ApplicationException("rip");
        }
        catch (System.Exception ex)
        {
            Console.Error.WriteLine(ex);
            Console.WriteLine("Error rip");
        }

    }
    public void ReadFile(string filepath = "test.logo")
    {
        try {
            
            Console.WriteLine("Trying to read file...");
            foreach (string line in File.ReadLines(filepath))
            {
                
            } // TODO: File exception
        } catch (System.Exception ex) { 
            Console.WriteLine(ex);
        }
    }

    public void Parse(string[] lines){
        foreach (string line in lines)
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

                default: 
                    Console.WriteLine("rip");
                    break;
            }
        }
    }

    public void WriteOut(string[]? lines = null)
    {
        lines ??= new string[]{"<line x1='0' y1='0' x2='35.3553390593274' y2='35.3553390593274' />"};

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

}