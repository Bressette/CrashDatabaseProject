create table location
(
	locID bigint(20) primary key not null auto_increment,
	cityID bigint(20) not null,
	streetAddress varchar(50) not null,
	roadChar enum("Not at a Junction", "Driveway", "Parking Lot", "Five-point or more", "T - Intersection", "Four-way Intersection", "On Ramp", "Traffic circle / roundabout",
	"Y - Intersection", "Off Ramp", "Not Reported"),
	foreign key(cityID) references city(cityID)
);


create table weather
(
	condID bigint(20) primary key not null auto_increment,
	weather enum("Freezing Precipitation", "Cloudy", "Wind", "Clear", "Rain", "Unknown"),
	surfaceCond enum("Snow", "Ice", "Wet", "Dry", "Slush", "Sand, mud, dirt, oil, gravel", "Water (standing / moving)", "Unknown"),
	dayNight enum("Day", "Night", "Unknown")

);

create table driver
(
	driverID bigint(20) primary key not null auto_increment,
	driverImpair enum("Alcohol", "Drugs", "None"),
	driverDamage enum("Property Damage Only", "Injury", "Fatal", "Unknown")
);

create table accident
(
	accID bigint(20) primary key not null auto_increment,
	locID bigint(20) not null,
	condID bigint(20) not null,
	driverID bigint(20) not null,
	foreign key(locID) references location(locID),
	foreign key(condID) references weather(condID),
	foreign key(driverID) references driver(driverID),
	collisionDir enum("Single Vehicle Crash", "Head On", "Same Direction Sideswipe", "Rear End", "No Turns, Thru moves only, Broadside", "Left Turn and Thru, Angle Broadside", 
	"Opp Direction Sideswipe", "Rear-to-rear", "Right Turn and Thru, Same Direction Sideswipe/Angle Crash", "Left Turn and Thru, Head On", "Right Turn and Thru, Head On", "Unknown"),
	accDate date not null,
	accTime time not null,
	agency varchar(20)
);




create table animal
(
	accID bigint(20) not null,
	animalType enum("Deer", "Moose", "Wild", "Domestic") not null,
	foreign key(accID) references accident(accID),
	primary key(accID, animalType)
	
);

create table vehicle
(
	accID bigint(20) not null,
	vehicleType enum("Heavy Truck", "Bicycle", "Pedestrian", "Motorcycle") not null,
	foreign key(accID) references accident(accID),
	primary key(accID, vehicleType)
	
);

create table city
(
	cityID bigint(20) primary key not null auto_increment,
	cityName varchar(20) not null
);