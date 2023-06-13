# Razor Tutorial

## Create

`dotnet new webapp -o RazorPagesMovie` creates folder with boiler plate
`dotnet dev-certs https --trust` enables https in dev

### Pages

Razor page:

- A `.cshtml` file that has HTML markup with C# code using Razor syntax.
- A `.cshtml.cs` file that has C# code that handles page events.
  
wwwroot folder:

Contains static assets, like HTML files, JavaScript files, and CSS files.

appsettings.json:

Contains configuration data, like connection strings.

```dotnet
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();
// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this
    for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}
```

---

In this tutorial, classes are added for managing movies in a database. The app's model classes use Entity Framework Core (EF Core) to work with the database. EF Core is an object-relational mapper (O/RM) that simplifies data access. You write the model classes first, and EF Core creates the database.

The model classes are known as POCO classes (from "Plain-Old CLR Objects") because they don't have a dependency on EF Core. They define the properties of the data that are stored in the database.

### Add data model

```dotnet
using System.ComponentModel.DataAnnotations;

namespace RazorPagesMovie.Models;

public class Movie
{
    public int Id { get; set; }
    public string? Title { get; set; }
    [DataType(DataType.Date)]
    public DateTime ReleaseDate { get; set; }
    public string? Genre { get; set; }
    public decimal Price { get; set; }
}
```

```bash
dotnet tool uninstall --global dotnet-aspnet-codegenerator
dotnet tool install --global dotnet-aspnet-codegenerator
dotnet tool uninstall --global dotnet-ef
dotnet tool install --global dotnet-ef
dotnet add package Microsoft.EntityFrameworkCore.Design
dotnet add package Microsoft.EntityFrameworkCore.SQLite
dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Tools
```

scaffold the thingy

```bash
dotnet aspnet-codegenerator razorpage -m Movie -dc RazorPagesMovie.Data.RazorPagesMovieContext -udl -outDir Pages/Movies --referenceScriptLibraries --databaseProvider sqlite
```

The scaffold process creates the following files:

- Pages/Movies: Create, Delete, Details, Edit, and Index.
- Data/RazorPagesMovieContext.cs

### Creating database using EF migration

```bash
dotnet ef migrations add InitialCreate
dotnet ef database update
```

### Page Model

Razor Pages are derived from `PageModel`. By convention, the `PageModel` derived class is named `PageNameModel`. For example, the Index page is named `IndexModel`.

The constructor uses [[dependency injection]] to add the `RazorPagesMovieContext` to the page. The injection gets added by the builder service in `Program.cs`.

```dotnet
public class IndexModel : PageModel
{
    private readonly RazorPagesMovie.Data.RazorPagesMovieContext _context;

    public IndexModel(RazorPagesMovie.Data.RazorPagesMovieContext context)
    {
        _context = context;
    }
```

### GET

When a `GET` request is made for the page, the `OnGetAsync` method returns a list of movies to the Razor Page. On a Razor Page, `OnGetAsync` or `OnGet` is called to initialize the state of the page. In this case, `OnGetAsync` gets a list of movies and displays them. When `OnGet` returns `void` or `OnGetAsync` returns `Task`, no return statement is used.

When the return type is `IActionResult` or `Task<IActionResult>`, a return statement must be provided. For example:

```dotnet
public async Task<IActionResult> OnPostAsync()
{
  if (!ModelState.IsValid)
    {
        return Page();
    }

    _context.Movie.Add(Movie);
    await _context.SaveChangesAsync();

    return RedirectToPage("./Index");
}
```

### front end behaviour

Razor can transition from HTML into C# or into Razor-specific markup. When an `@` symbol is followed by a Razor reserved keyword, it transitions into Razor-specific markup, otherwise it transitions into C#.

### The `@page` directive
The `@page` Razor directive makes the file an MVC action, which means that it can handle requests. `@page` must be the first Razor directive on a page. `@page` and `@model` are examples of transitioning into Razor-specific markup.

### The @model directive

```asp
@page
@model RazorPagesMovie.Pages.Movies.IndexModel
```

The `@model` directive specifies the type of the model passed to the Razor Page. In the preceding example, the `@model` line makes the `PageModel` derived class available to the Razor Page. The model is used in the `@Html.DisplayNameFor` and `@Html.DisplayFor` HTML Helpers on the page.

Examine the lambda expression used in the following HTML Helper:

```dotnet
@Html.DisplayNameFor(model => model.Movie[0].Title)
```

The `DisplayNameFor` HTML Helper inspects the `Title` property referenced in the lambda expression to determine the display name. The lambda expression is inspected rather than evaluated. That means there is no access violation when `model`, `model.Movie`, or `model.Movie[0]` is `null` or empty. When the lambda expression is evaluated, for example, with `@Html.DisplayFor(modelItem => item.Title)`, the model's property values are evaluated.

### The layout page

Select the menu links RazorPagesMovie, Home, and Privacy. Each page shows the same menu layout. The menu layout is implemented in the `Pages/Shared/_Layout.cshtml` file. Layout templates allow the HTML container layout to be:

- Specified in one place.
- Applied in multiple pages in the site.

Find the `@RenderBody()` line. `RenderBody` is a placeholder where all the page-specific views show up, wrapped in the layout page. For example, select the Privacy link and the `Pages/Privacy.cshtml` view is rendered inside the `RenderBody` method.


## Sources

- [MS docs](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-7.0&tabs=visual-studio-code)