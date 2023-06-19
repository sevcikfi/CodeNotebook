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

---

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

## front end behaviour

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

## The layout page

Select the menu links RazorPagesMovie, Home, and Privacy. Each page shows the same menu layout. The menu layout is implemented in the `Pages/Shared/_Layout.cshtml` file. Layout templates allow the HTML container layout to be:

- Specified in one place.
- Applied in multiple pages in the site.

Find the `@RenderBody()` line. `RenderBody` is a placeholder where all the page-specific views show up, wrapped in the layout page. For example, select the Privacy link and the `Pages/Privacy.cshtml` view is rendered inside the `RenderBody` method.

```Csharp
@{
    Layout = "_Layout";
}
```

The preceding markup sets the layout file to `Pages/Shared/_Layout.cshtml` for all Razor files under the Pages folder.

## Submitting data

### The Create page model

The OnGet method initializes any state needed for the page. he Movie property uses the `[BindProperty]` attribute to opt-in to model binding. When the Create form posts the form values, the ASP.NET Core runtime binds the posted values to the `Movie` model.

The `OnPostAsync` method is run when the page posts form data:

```csharp
public async Task<IActionResult> OnPostAsync()
{
  if (!ModelState.IsValid || _context.Movie == null || Movie == null)
    {
        return Page();
    }

    _context.Movie.Add(Movie);
    await _context.SaveChangesAsync();

    return RedirectToPage("./Index");
}
```

If there are any model errors, the form is redisplayed, along with any form data posted. Most model errors can be caught on the client-side before the form is posted. An example of a model error is posting a value for the date field that cannot be converted to a date.

If there are no model errors, the data is saved and the browser is redirected to the Index page.

### The Create Razor Page

The following Tag Helpers are shown in the preceding markup:

- `<form method="post">`

    The `<form method="post">` element is a Form Tag Helper. The Form Tag Helper automatically includes an antiforgery token.

- `<div asp-validation-summary="ModelOnly" class="text-danger"></div>`

    The Validation Tag Helpers (`<div asp-validation-summary` and `<span asp-validation-for`) display validation errors.

- `<label asp-for="Movie.Title" class="control-label"></label>`

    The Label Tag Helper (`<label asp-for="Movie.Title" class="control-label"></label>`) generates the label caption and `[for]` attribute for the `Title` property.

- `<input asp-for="Movie.Title" class="form-control" />`

    The Input Tag Helper (`<input asp-for="Movie.Title" class="form-control">`) uses the `DataAnnotations` attributes and produces HTML attributes needed for jQuery Validation on the client-side.

- `<span asp-validation-for="Movie.Title" class="text-danger"></span>`

```html
<div asp-validation-summary="ModelOnly" class="text-danger"></div>
<div class="form-group">
    <label asp-for="Movie.Title" class="control-label"></label>
    <input asp-for="Movie.Title" class="form-control" />
    <span asp-validation-for="Movie.Title" class="text-danger"></span>
</div>
```

---

## Connecting to Database

The `RazorPagesMovieContext` object handles the task of connecting to the database and mapping `Movie` objects to database records. The database context is registered with the [[Dependency Injection]] container in `Program.cs`:

```csharp
builder.Services.AddDbContext<RazorPagesMovieContext>(options =>
    options.UseSqlite(builder.Configuration.GetConnectionString("RazorPagesMovieContext") ?? throw new InvalidOperationException("Connection string 'RazorPagesMovieContext' not found.")));
```

The ASP.NET Core Configuration system reads the `ConnectionString` key. For local development, configuration gets the connection string from the `appsettings.json` file. When the app is deployed to a test or production server, an environment variable can be used to set the connection string to a test or production database server.

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "ConnectionStrings": {
    "RazorPagesMovieContext": "Data Source=RazorPagesMovie.Data.db"
  }
}
```

### Seeding the database for testing

Create a new class named `SeedData` in the Models folder and add the following to `Program.cz` which does following:

- Get a database context instance from the *dependency injection (DI)* container.
- Call the `seedData.Initialize` method, passing to it the database context instance.
- Dispose the context when the seed method completes. The `using` statement ensures the context is disposed.

```csharp
using (var scope = app.Services.CreateScope())
{
    var services = scope.ServiceProvider;

    SeedData.Initialize(services);
}
```

---

## Changing the page

We updated `Models/Movie.cs` which does following:

- The `[Column(TypeName = "decimal(18, 2)")]` data annotation enables Entity Framework Core to correctly map `Price` to currency in the database.
- The `[Display]` attribute specifies the display name of a field. In the preceding code, `Release Date` instead of `ReleaseDate`.
The `[DataType]` attribute specifies the type of the data (`Date`). The time information stored in the field isn't displayed.

*Tag Helpers* enable server-side code to participate in creating and rendering HTML elements in Razor files.

In the following code, the *Anchor Tag Helper* dynamically generates the HTML `href` attribute value from the Razor Page (the route is relative), the `asp-page`, and the route identifier (`asp-route-id`).

```html
<td>
    <a asp-page="./Edit" asp-route-id="@item.ID">Edit</a> |
    <a asp-page="./Details" asp-route-id="@item.ID">Details</a> |
    <a asp-page="./Delete" asp-route-id="@item.ID">Delete</a>
</td>
```

Use **View Source** from a browser to examine the generated markup. A portion of the generated HTML is shown below:

```html
<td>
  <a href="/Movies/Edit?id=1">Edit</a> |
  <a href="/Movies/Details?id=1">Details</a> |
  <a href="/Movies/Delete?id=1">Delete</a>
</td>
```

The dynamically generated links pass the movie ID with a *query string*. For example, the `?id=1` in `https://localhost:5001/Movies/Details?id=1`.

## Add route template, lowkey REST API

Update the Edit, Details, and Delete Razor Pages to use the `{id:int}` route template. Change the page directive for each of these pages from `@page` to `@page "{id:int}"`. Run the app and then view source. The generated HTML adds the ID to the path of the URL:

```html
<td>
  <a href="/Movies/Edit/1">Edit</a> |
  <a href="/Movies/Details/1">Details</a> |
  <a href="/Movies/Delete/1">Delete</a>
</td>
```

With the `@page "{id:int}"` directive, the break point is never hit. The **routing engine** returns HTTP 404. Using `@page "{id:int?}"` (with ?), the `OnGetAsync` **method** returns `NotFound` (HTTP 404).

### Review concurrency exception handling

Review the `OnPostAsync` method in the `Pages/Movies/Edit.cshtml.cs` file. The code detects *concurrency exceptions* when one client deletes the movie and the other client posts changes to the movie.

To test the `catch` block:

1. Set a breakpoint on `catch (DbUpdateConcurrencyException)`.
2. Select **Edit** for a movie, make changes, but don't enter **Save**.
3. In another browser window, select the **Delete** link for the same movie, and then delete the movie.
4. In the previous browser window, post changes to the movie.

### Posting and binding review

Look at the `Pages/Movies/Edit.cshtml.cs` file. When an HTTP GET request is made to the Movies/Edit page, for example, `https://localhost:5001/Movies/Edit/3`:

- The `OnGetAsync` method fetches the movie from the database and returns the `Page` method.
- The `Page` method renders the `Pages/Movies/Edit.cshtml` Razor Page. The `Pages/Movies/Edit.cshtml` file contains the model directive `@model RazorPagesMovie.Pages.Movies.EditModel`, which makes the **movie model** available on the **page**.
- The Edit form is displayed with the values from the movie.

When the `Movies/Edit` page is posted:

- The **form** values on the page are bound to the `Movie` property. The `[BindProperty]` attribute enables `Model binding`.

    ```csharp
    [BindProperty]
    public Movie Movie { get; set; }
    ```

- If there are errors in the model state, for example, `ReleaseDate` cannot be converted to a date, the form is redisplayed with the submitted values.
- If there are no model errors, the movie is saved.

The HTTP GET methods in the Index, Create, and Delete Razor pages follow a similar pattern. The HTTP POST `OnPostAsync` method in the Create Razor Page follows a similar pattern to the `OnPostAsync` method in the Edit Razor Page.

---

## Adding search

```csharp
[BindProperty(SupportsGet = true)]
public string? SearchString { get; set; }
public SelectList? Genres { get; set; }
[BindProperty(SupportsGet = true)]
public string? MovieGenre { get; set; }
```

We added the previous code which does the following:

- `SearchString`: Contains the text users enter in the search text box. `SearchString` has the `[BindProperty]` attribute. `[BindProperty]` binds form values and query strings with the same name as the property. `[BindProperty(SupportsGet = true)]` is **required** for binding on HTTP GET requests for **security reasons**.
- `Genres`: Contains the list of genres. `Genres` allows the user to select a genre from the list. `SelectList` requires `using Microsoft.AspNetCore.Mvc.Rendering`;
- `MovieGenre`: Contains the specific genre the user selects. For example, "Western".

and changed `OnGetAsync()` accordingly:

```csharp
public async Task OnGetAsync()
{
    var movies = from m in _context.Movie
                 select m;
    if (!string.IsNullOrEmpty(SearchString))
    {
        movies = movies.Where(s => s.Title.Contains(SearchString));
    }

    Movie = await movies.ToListAsync();
}
```

- The first line of the `OnGetAsync` method creates a *LINQ query* to select the movies. The query is only ***defined*** at this point, it has ***not*** been run against the database.
- If the `SearchString` property is not `null` or empty, the movies query is modified to filter on the search string.

The `s => s.Title.Contains()` code is a *Lambda Expression*. Lambdas are used in method-based LINQ queries as arguments to standard query operator methods such as the *`Where`* method or `Contains`. *LINQ* queries are not executed when they're defined or when they're modified by calling a method, such as `Where`, `Contains`, or `OrderBy`. Rather, query execution is deferred. The evaluation of an expression is *delayed* until its realized value is iterated over or the `ToListAsync` method is called.

Navigate to the Movies page and append a query string such as ?searchString=Ghost to the URL. For example, `https://localhost:5001/Movies?searchString=Ghost`. The filtered movies are displayed.

However if you want to pass the parameter as `URL segment` instead of `Query parameter`, you need to add the following route template to the Index page, the search string can be passed as a URL segment. For example, `https://localhost:5001/Movies/Ghost`. The `?` in `"{searchString?}"` means this is an optional route parameter.

```csharp
@page "{searchString?}"
```

The *ASP.NET Core* runtime uses **model binding** to set the value of the `SearchString` property from the query string (`?searchString=Ghost`) or route data (`https://localhost:5001/Movies/Ghost`). Model binding is **not** case sensitive.

## Sources

- [MS docs](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-7.0&tabs=visual-studio-code)
- [Model binding](https://learn.microsoft.com/en-us/aspnet/core/mvc/models/model-binding?view=aspnetcore-7.0)
