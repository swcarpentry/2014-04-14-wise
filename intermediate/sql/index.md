---
layout: lesson
root: ../..
title: SQL for Science
level: intermediate
---

# SQL
SQL stands for Structured Query Language. It's a common language to many
databases. Specifically, relational databases, so called because there
are relationships between the data, letting us link it together.

There are many SQL databases, including Oracle, MySQL, PostgreSQL, etc.
Today we'll use the simplest one, SQLite. SQLite is awesome because it's
small, available anywhere, and its underlying datastore is a file. Super
easy to use.

## Sqlite3

Today we'll use sqlite3 in two ways: the command line interface, and the Firefox
SQLite3 plugin. The Firefox plugin, with its graphical interface, is
optional. Everything can be done at the command line, if not as pretty.

Either way, we need a database file. Today, we'll start with this one:

[restaurants.sqlite](restaurants.sqlite)

## Command line interface

Go to this directory, where restaurants.sqlite is located, and run in
the terminal:

     sqlite3 restaurants.sqlite

This gives a prompt.
The first thing to know is how to exit: `.exit`

The other commands that are specific to this client are listed by
`.help` Use this to explore some available config.

Data in the database is stored in tables. See the tables available with:
`.tables`

Each table has a structure, a set of columns. To see the structure of
the `business` table, try `.schema business`. SQLite doesn't have the
prettiest format: it shows you the command that created the table
structure. You can see the column headers and the type.

Hint: It's good practice to name columns in all lowercase, and use all caps
for keywords. Usually it is not case-sensitive, but there are weird
exceptions. (like on Android.)

Data types: SQLite isn't so picky about data types. The useful ones are
TEXT, INTEGER, and REAL (which means floating-point number). SQLite uses
this as a hint; they're not enforced. You can put a string in a field
marked INTEGER.

### My First SQL

Now let's look at the actual data contained in a table. To see data, use
SELECT. Tell it what columns you want to see (* means all of them), then
what table to look in, then semicolon.

    SELECT * FROM business;

The output isn't pretty. We can make it a little better with:

    .header on
    .mode column

These change all output for the rest of this session. Also let's not see
the whole table, but just a sample:

    SELECT * FROM business LIMIT 10;

That's too much information for my screen width, and not enough of the
name. Be specific about the columns we want:

    SELECT business_id, name, address, postal_code FROM business LIMIT 10;

And then adjust column width configuration:

    .width 5 30 30 5

OK, now we can see what's in the business table. But that was a pain.
I'm going to flip over to Firefox because it'll be easier to show what
is here. You can do that too, or stay in the command line.

## Firefox SQLite plugin

Within Firefox, after installing the plugin, Tools -> SQLite Manager.
Then, File->Open and choose the database file. From here, we can see the
tables on the left, and their contents with Browse & Search.

In Execute SQL, we can run arbitrary SQL statements and see the output.

## Fun with just one table

What kind of values do we have? Maybe we can look at restaurants by
postal code. What are useful values for postal code?

    SELECT DISTINCT postal_code FROM business;

Narrow Results: the WHERE clause lets us pick only certain rows.

    SELECT business_id, name, address, postal_code
    FROM business
    WHERE postal_code = '94131'

Or we can find one by name:

    SELECT *
    FROM business
    WHERE name LIKE '%DONUT%'

### Aggregating
Simple aggregation:

    SELECT AVG(score) FROM inspection;

We can summarize the data. We can say, how many restaurants are in each
postal code? for this, we must GROUP BY the aggregation fields.

    SELECT postal_code,
           COUNT(*) as "count_per_zip"
    FROM business
    GROUP BY postal_code;

And then we'll want to see the most food-filled postal codes at the top:

    SELECT postal_code,
           COUNT(*) as "count_per_zip"
    FROM business
    GROUP BY postal_code
    ORDER BY count_per_zip DESC;

COUNT gets the count of rows. There are other aggregations, like MAX and
MIN and AVG. The full list is [documented
here](http://sqlite.org/lang_aggfunc.html).

Column aliases: I gave the count(\*) result a name using AS. This lets me
reference it in the ORDER_BY clause.

Sorting: ORDER BY will work with column names or numbers. DESC or ASC
specifies the direction of sorting.

## Linking tables together

It gets interesting when we start bringing multiple tables together.

     SELECT name, inspection_date, score, description
     FROM business JOIN inspection ON business.business_id = inspection.business_id
     JOIN score_legend ON min_score <= score and max_score >= score
     WHERE name = 'DONUTS & THINGS'

or here's a more interesting one. Which schools have unresolved vermin
infestations?

    SELECT name, postal_code, violation_date, description,
           CASE WHEN description LIKE '%violation corrected%'
                  THEN "CORRECTED"
                ELSE "OUTSTANDING"
           END as "resolution"
    FROM business "b" JOIN violation "v"
                  ON b.business_id = v.business_id
    WHERE name LIKE '%SCHOOL%'
      AND resolution = "OUTSTANDING"
      AND description like '%vermin%'

Categorization: the CASE statement lets us put in different values based
on any boolean expression. Any number of WHEN/THEN clauses are allowed;
if none match then the ELSE clause kicks in. Don't forget END, and give
it an alias.

Table aliases: tables in the FROM clause can have aliases, which is
handy for shortening the query.

## Nested selects

Select statements inside the where clause can prevent us from
hard-coding values, instead expressing where a value comes from.

    SELECT i.business_id, name, inspection_date, score
    FROM inspection i JOIN business b on b.business_id = i.business_id
    WHERE score >= (SELECT min_score
                    FROM score_legend
                    WHERE description = 'Good');

Even more fun is to use a select statement as a table. This can get us
the most recent inspection for each business.

    SELECT i.business_id,
           i.score,
           i.inspection_date,
           i.inspection_type
    FROM inspection as i
    JOIN (SELECT MAX(inspection_date) as "rd", business_id
          FROM inspection GROUP BY business_id) as r
      ON r.business_id = i.business_id AND r.rd = i.inspection_date;

And that's so useful that we can store make an alias for it:

    CREATE VIEW most_recent_inspection AS
       SELECT i.business_id,
           i.score,
           i.inspection_date,
           i.inspection_type
       FROM inspection as i
       JOIN (SELECT MAX(inspection_date) as "rd", business_id
          FROM inspection GROUP BY business_id) as r
       ON r.business_id = i.business_id AND r.rd = i.inspection_date;

A view always reflects the data in the tables it was defined in terms
of. We could also CREATE TABLE in this way, and that would make a copy
of the data that stays forever.

Another use for the nested select: it's useful for selecting based on
aggregate fields. This ranks schools by average and total score,
excluding any with only one inspection:

    SELECT i.business_id, name, total, mean, countiepoo
    FROM (SELECT business_id,
                 SUM(score) AS "total",
                 AVG(score) AS "mean",
                 COUNT(score) AS "countiepoo"
          FROM inspection GROUP BY business_id) i
    JOIN business b ON b.business_id = i.business_id
    WHERE countiepoo > 1
      AND name LIKE '%SCHOOL%'
    ORDER BY mean DESC, total DESC

notice that we can order by multiple fields, and each is ASCending or
DESCending individually.

### Functions

(incomplete)

Functions: instr() is a function that returns the
location of a string within a larger string, or 0 if not found.
Functions are specific to the database. The functions available for
SQLite are [documented here](http://sqlite.org/lang_corefunc.html).
Watch out - not all of them exist on my version of sqlite3. instr exists
in Firefox but not my default Mac sqlite3.

## Changing data

You can use [INSERT](http://sqlite.org/lang_insert.html) and [UPDATE](http://sqlite.org/lang_update.html) to add rows and alter fields. I feel dirty
when doing this, because where is the traceability of the data?

To remove rows, DELETE them. The syntax is similar to SELECT, which is
unfortunate.

    DELETE FROM violations
    WHERE business_id = '10';

If you accidentally hit run before typing the WHERE clause, then you
just emptied your table. And there's no going back.

## Empty or NULL

in SQL, there are two kinds of empty: empty string, and NULL. NULL is
the absence of a value. It behaves oddly in joins and WHERE clauses,
because it is not equal to anything, not even itself.

    SELECT * FROM business WHERE postal_code = "";

There are rows there. Silly; let's indicate that the value is missing by
setting that field to null.

    UPDATE business SET postal_code = NULL WHERE postal_code = "";

(UPDATE also has the problem that the limiting clause comes last. I've
messed that up often.)

## Backing up

You can stick the whole .sqlite file in your git repository, but you
won't see meaningful differences. You can also dump your database into a
series of commands that can reconstruct it from nothing, in any sqlite
database.

    .output my_backup_file.sql
    .dump
    .output stdout

The `.output` command changes where sqlite3 sends the output of your
commands. Go look at your backup file and see all the commands to
recreate the database.

Put this into version control, and changes will be meaningful.

## Saving commands

In the GUI, cut and paste will do.
In the command line:

* `.read FILE` reads in a file containing commands and runs each of them
* `.output FILE` sends output to that file instead of the screen, so you
can save results without copy-pasting.

## Creating tables

Importing delimited files into sqlite is not too bad if the files are
well-behaved (no commas in the middle of fields, for instance).
See [the script that imported the data](populate_db.sql) for this
database.

It's even easier to use the Database->Import dialog to generate the
CREATE statement for you. This one even understands that the first line
might hold the column headers.

## Data Integrity

In general, SQL databases offer validations on data, especially the
relationships between them. You can explore constraints and foreign
keys if you want the database to perform checks for you.



