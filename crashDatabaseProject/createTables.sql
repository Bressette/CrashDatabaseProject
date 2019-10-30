create table location
(
	locID bigint(20) primary key not null auto_increment,
	streetAddress varchar(50) not null,
	city varchar(20) not null,
	roadChar enum("Not at a Junction", "Driveway", "Parking Lot", "Five-point or more", "T - Intersection", "Four-way Intersection", "On Ramp", "Traffic circle / roundabout",
	"Y - Intersection", "Off Ramp")
);


create table weather
(
	condID bigint(20) primary key not null auto_increment,
	weather enum("Freezing Precipitation", "Cloudy", "Wind", "Clear", "Rain"),
	surfaceCond enum("Snow", "Ice", "Wet", "Dry", "Slush", "Sand, mud, dirt, oil, gravel", "Water (standing / moving)"),
	dayNight enum("Day", "Night")

);

create table driver
(
	driverID bigint(20) primary key not null auto_increment,
	driverImpair enum("Alcohol", "Drugs"),
	driverDamage enum("Property Damage Only", "Injury", "Fatal")
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
	"Opp Direction Sideswipe", "Rear-to-rear", "Right Turn and Thru, Same Direction Sideswipe/Angle Crash", "Left Turn and Thru, Head On", "Right Turn and Thru, Head On"),
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