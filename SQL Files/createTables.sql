create table location
(
	locID int primary key not null auto_increment,
	addressID int not null,
	roadChar enum("Not at a Junction", "Driveway", "Parking Lot", "Five-point or more", "T - Intersection", "Four-way Intersection", "On Ramp", "Traffic circle / roundabout",
	"Y - Intersection", "Off Ramp", "Not Reported"),
	foreign key(addressID) references address(addressID)
);

create table address
(
	addressID int primary key not null auto_increment,
	streetAddress varchar(50) not null,
	cityID int not null,
	foreign key(cityID) references city(cityID)
);

create table weather
(
	condID int primary key not null auto_increment,
	weather enum("Freezing Precipitation", "Cloudy", "Wind", "Clear", "Rain", "Unknown"),
	surfaceCond enum("Snow", "Ice", "Wet", "Dry", "Slush", "Sand, mud, dirt, oil, gravel", "Water (standing / moving)", "Unknown"),
	dayNight enum("Day", "Night", "Unknown")

);

create table driver
(
	driverID int primary key not null auto_increment,
	driverImpair enum("Alcohol", "Drugs", "None"),
	driverDamage enum("Property Damage Only", "Injury", "Fatal", "Unknown")
);

create table accident
(
	accID int primary key not null auto_increment,
	locID int not null,
	condID int not null,
	driverID int not null,
	foreign key(locID) references location(locID),
	foreign key(condID) references weather(condID),
	foreign key(driverID) references driver(driverID),
	collisionDir varchar(50),
	accDate date not null,
	accTime time not null,
	agency varchar(20)
);





create table animal
(
	accID int not null,
	animalType enum("Deer", "Moose", "Wild", "Domestic") not null,
	foreign key(accID) references accident(accID),
	primary key(accID, animalType)
	
);

create table vehicle
(
	accID int not null,
	vehicleType enum("Heavy Truck", "Bicycle", "Pedestrian", "Motorcycle") not null,
	foreign key(accID) references accident(accID),
	primary key(accID, vehicleType)
	
);

create table city
(
	cityID int primary key not null auto_increment,
	cityName varchar(20) not null
);