load data local infile '/home/jbressette6507/Weather CSV.csv'
into table weather
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile '/home/jbressette6507/driver.csv'
into table driver
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile '/home/jbressette6507/location.csv'
into table location
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile '/home/jbressette6507/animal.csv'
into table animal
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile '/home/jbressette6507/accident.csv'
into table accident
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile '/home/jbressette6507/vehicle.csv'
into table vehicle
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile '/home/jbressette6507/city.csv'
into table city
fields terminated by ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile '/home/jbressette6507/address.csv'
into table address
fields terminated by ','
OPTIONALLY ENCLOSED by ','
OPTIONALLY ENCLOSED by '"'
lines terminated by '\r\n'
ignore 1 lines;