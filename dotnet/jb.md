# micro api from JB

bad:

```scala
def main(server: HttpServer) = {
  val request = server.getRequest()
  if request.address == "/users" && request.method == Method.GET {
    val users = sql.query("select * from users;").toList
    return Response(200, users.toJson)
  }
}
```

napíšeš jako:

```scala
class DatabaseConnection {
  def sql: SQL-DB = ???
  def getUsers() = sql.query("select * from users;").toList
}
```

```scala
trait Endpoint[T] {
  def address: String
  def method: HttpMethod
  def call(): T
}
```

```scala
object handleUsers(db: DatabaseConnection) extends Endpoint[List[User]] {
  def address = "/users"
  def method = GET
  def call() = db.getUsers()
}
```

```scala
def main() = {
  val db = DatabaseConnection()
  val endpoints = [handleUsers(db)]
  server.handleEndpoints(endpoints)
}
```

```scala
def handleEndpoint(request: Request, endpoint: Endpoint) = {
  if request.address == endpoint.address && request.method == endpoint.method { 
    val result = endpoint.call()
    return Some(Response(200, result.toJson))
  }
  return None
}
```

```scala
def handleEndpoints(endpoints: List[Endpoint]) = {
  val request = server.getRequest()
  var response = None
  endpoints.foreach { endpoint =>
    response = handleEndpoint(request, endpoint)
    if response.statusCode == 200 {
      return response
    }
  }
}
```
