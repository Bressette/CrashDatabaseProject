load data local infile '/home/jbressette6507/Weather CSV.csv'
into table weather
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;
