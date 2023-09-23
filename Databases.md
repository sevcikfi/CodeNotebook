---
alias:
tag: IT/languages CodeNotebook
---

# Database things

## Paradigms

*quick info* about different types and what's popular right know and their pros and cons

Relational-SQL DB:

- MySQL
- MariaDB
- Microsoft-SQL
- PostgreSQL
- SQLite
- Oracle SQL

No-SQL or special:

- MongoDB
- GraphQL
- Cassandra

## SQL stuff

*SQL cheat sheet basically* for MySQL/MariDB and SQLite

### CLI

Connect to local server: `mysql -u [username] -p [database]`

Connect over network: `mariadb -h [host_address] -P [port_number]`

#### CREATE / ALTER / DROP / REMOVE

- create DB: `CREATE DATABASE database_name;`
- Drop DB: `DROP DATABASE [IF EXISTS] database_name;`
- create table:

    ```sql
    CREATE TABLE [IF NOT EXISTS]
    table_name (
    field_name field_type [NOT NULL]
    );
    ```

- alter table:

    ```sql
    ALTER TABLE table_name
    [ADD/MODIFY/DROP] [COLUMN] field_name field_type;
    ```

    or

    ```sql
    ALTER TABLE table_name
    ADD [COLUMN] field_name field_type
    COMMENT 'text' DEFAULT "some-value";
    ```

- drop table: `DROP TABLE [IF EXISTS] table_name;`

#### Constraints

- `NOT NULL` - Ensures that a column cannot have a NULL value
- `UNIQUE` - Ensures that all values in a column are different
- `PRIMARY KEY` - A combination of a `NOT NULL` and `UNIQUE`, uniquely identifies each row in a table
- `FOREIGN KEY` - Prevents actions that would destroy links between tables
- `CHECK` - Ensures that the values in a column satisfies a specific condition

    ```sql
    CHECK (condition);
    CONSTRAINT CHK_name CHECK (condition);
    ```

- `DEFAULT` - Sets a default value for a column if no value is specified
- `CREATE INDEX` - Used to create and retrieve data from the database very quickly

    ```sql
    CREATE [INDEX/FULLTEXT/UNIQUE] index_name
    ON table_name (column1, column2, ...);
    ```

- `AUTO_INCREMENT` - Auto-increment allows a unique number to be generated automatically when a new record is inserted into a table

#### Browsing

- change current DB: `USE database_name;`
- show DBs: `SHOW DATABASES;`
- show tables: `SHOW TABLES;`
- Show table properties: `DESCRIBE table_name;`
- show create table statement: `SHOW CREATE TABLE table_name;`
- Show the field information for a specified table: `SHOW FIELDS FROM table_name / DESCRIBE table_name;`

#### Select basic

- Select all rows from a table: `SELECT * FROM table_name;`
- Select data from columns: `SELECT column1, column2 FROM table_name`
- Select data with a filter using a WHERE clause:

    ```sql
    SELECT field_list
    FROM table_name
    WHERE condition;
    ```

- You may combine conditions using `AND`, `OR` and `NOT` operators

    ```sql
    SELECT field_list
    FROM table_name
    WHERE NOT column1=val1 OR (column2=val2 AND column1=val3) ;
    ```

- You can also add `LIKE` operator to match some pattern using `%` for 0 to n characters and `_` being single one character e.g. *finds values starting with "a" which are at least 3 characters long*

    ```sql
    WHERE CustomerName LIKE 'a__%'
    ```

- `IN` operator allows you to specify multiple values in a `WHERE` clause.

    ```sql
    WHERE column_name IN (SELECT STATEMENT) | (value1, value2);
    ```

- `BETWEEN` operator works like `IN` except instead of discreet list, you give range:

    ```sql
    WHERE column_name BETWEEN value1 AND value2;
    ```

- Select data and order by column in ascending/descending order:

    ```sql
    SELECT field_list
    FROM table_name
    ORDER BY column1, column2 ASC|DESC;
    ```

- Grouping rows using the `GROUP BY` clause with some function like `COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()` and filtering the result with `HAVING`:

    ```sql
    SELECT column_name(s), function(other_column)
    FROM table_name
    WHERE condition
    GROUP BY column_name(s)
    HAVING function(other_column) <some_condition>;
    ```

#### INSERT / UPDATE / DELETE

- Insert a row into a table:

    ```sql
    INSERT INTO table_name (field_name [field_names]) 
    VALUES (value [, values]);
    ```

- Update rows in a table:

    ```sql
    UPDATE table_name SET field_name =
    value ([, field_name = value, ])
    [WHERE condition];
    ```

- Delete rows from a table: `DELETE FROM table_name [WHERE condition];`

- `INSERT INTO SELECT` copies data from one table into another:

    ```sql
    INSERT INTO table2 (column1, column2, column3, ...)
    SELECT column1, column2, column3, ...
    FROM table1
    WHERE condition;
    ```

### Advanced stuff

- Select data from multiple tables using `JOIN`, note that default `JOIN` is `INNER JOIN`:

    ```sql
    SELECT field_list
    FROM table_name_1 [INNER|LEFT|RIGHT|FULL OUTER/CROSS] JOIN
    table_name_2 ON condition;
    ```

- Union data from two tables, it *has* same number of columns with similar data types:

    ```sql
    SELECT column_name(s) FROM table1
    UNION
    SELECT column_name(s) FROM table2;
    ```

### Admin stuff

- truncate table, in other words, deletes all the content: `TRUNCATE table_name;`
- List all users on the database instance: `SELECT user,host FROM mysql.user;`
- Create a new user with a given password: `CREATE USER user[@'host'] IDENTIFIED BY 'plain-textpassword';`
- remove user with `DROP USER 'user'@'host';`

Syntax to grant or revoke privileges on a given database to a particular
user: `GRANT|REVOKE permission ON database.table TO 'user'@'localhost';` For host  ``` `` ``` and `%` is any host/IP, `localhost` is only from the host machine. Always make root `localhost` exclusive for improved security.

- `ALL` - Allows complete access to a specific database. If a database is not specified, it allows complete access to the entirety of MySQL.
- `CREATE` - Allow a user to create databases and tables.
- `DELETE` - Allow a user to delete rows from a table.
- `DROP` - Allow a user to drop databases and tables.
- `EXECUTE` - Allow a user to execute stored routines.
- `GRANT OPTION` - Allow a user to grant or remove another user's privileges.
- `INSERT` - Allow a user to insert rows from a table.
- `SELECT` - Allow a user to select data from a database.
- `SHOW DATABASES`- Allow a user to view a list of all databases.
- `UPDATE` - Allow a user to update rows in a table.

Remember to always refresh the privileges with `FLUSH PRIVILEGES;`

### Secure installation

What happens in the script is basically setting the database root password and removing a test database and users.

```bash
readonly mariadb_root_password=root_secret

if mysqladmin -u root status > /dev/null 2>&1; then
  mysqladmin password "${mariadb_root_password}" > /dev/null 2>&1
  printf "database root password set\n"
else
  printf "skipping database root password: already set\n"
fi
```

After setting the root password with the previous code, the following snippet will remove the test database and anonymous users. The database root user is set to only be allowed to log in from localhost.

```bash
mysql --user=root --password="${mariadb_root_password}" mysql <<_EOF_
DELETE FROM user WHERE User='';
DELETE FROM user WHERE User='root' AND host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
DELETE FROM db WHERE db='test' OR db='test\\_%';
FLUSH PRIVILEGES;
_EOF_
```

Create a database and a user with all privileges for that database (warning: user/db are first removed if they exist):

```bash
readonly db_user=myuser
readonly db_name=mydb
readonly db_password=some_password

mysql --user=root --password="${mariadb_root_password}" <<_EOF_
DROP USER IF EXISTS ${db_user};
DROP DATABASE IF EXISTS ${db_name};
CREATE DATABASE ${db_name};
GRANT ALL ON ${db_name}.* TO '${db_user}'@'%' IDENTIFIED BY PASSWORD('${db_password}');
FLUSH PRIVILEGES;
_EOF_
```

### Others something

TODO: put more info about other type and their use case here

## Sources

[MariaDB cheatsheet](https://)
[SQL scripts](https://bertvv.github.io/cheat-sheets/MySQL-MariaDB.html)
