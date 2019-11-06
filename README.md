# crashDatabaseProject

A database that holds data about crashes in vermont in 2016. The database is used
to generate statistics from the dataset that could be used to identify patterns and
relationships between variables.

##Technologies

The raw data that is stored in a CSV is sanitized using the Pandas library in Python
and separate CSV files are generated for each table in the database design. The generated
CSVs are used to import data into a mySQL database. The database is hosted on a MariaDB server
and the layout of the tables was based on an entity relationship diagram that was formed to 
minimize data redundancy and maintain a high level of normalization.
