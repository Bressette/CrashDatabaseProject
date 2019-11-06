import pandas


#function that separates date and time then returns the date
def get_date(s):
    s = s.rsplit("T", maxsplit=1)[0]
    return s

#function that separates date and time then returns the time
def get_time(s):
    s = s.rsplit("T", maxsplit=1)[1]
    s = s.rsplit(".", maxsplit=1)[0]
    return s

#function that declares a dataframe weather drops duplicates and creates new column
#to hold the index of the dataframe and stores it as condID for a primary key column
def export_weather(df):
    df_weather = df[['Weather', 'SurfaceCondition', 'DayNight']]
    df_weather.drop_duplicates(keep='first', inplace=True)
    df_weather.reset_index(inplace=True, drop=True)
    df_weather.index += 1
    df_weather['condID'] = df_weather.index;
    df_weather.to_csv("Weather CSV.csv")
    return df_weather

#function that declares a dataframe location drops duplicates and creates new column
#to hold the index of the dataframe and stores it as locID for a primary key column
def export_location(df):
    df_location = df[['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics']]
    df_location.drop_duplicates(keep='first', inplace=True)
    df_location.reset_index(inplace=True, drop=True)
    df_location.index += 1
    df_location['locID'] = df_location.index;
    return df_location

#function that declares a dataframe driver drops duplicates and creates new column
#to hold the index of the dataframe and stores it as driverID for a primary key column
def export_driver(df):
    df_driver = df[['Impairment', 'InjuryType']]
    df_driver.drop_duplicates(keep='first', inplace=True)
    df_driver.reset_index(inplace=True, drop=True)
    df_driver.index += 1
    df_driver['driverID'] = df_driver.index
    df_driver.to_csv("driver.csv")
    return df_driver


def export_animal(df):
    df['accID'] = df.index
    df_animal = df[['accID', 'Animal']]
    df_animal = df_animal.dropna(axis=0, subset=['Animal'])
    df_export_animal = df_animal[df_animal.Animal != "None/Other"]
    df_export_animal.to_csv("animal.csv")
    return df_export_animal

def export_vehicle(df):
    df_vehicle = df[['accID', 'Involving']]
    df_export_vehicle = df_vehicle[df_vehicle.Involving != "None"]
    df_export_vehicle = df_export_vehicle.dropna(subset=['Involving'])
    df_export_vehicle.to_csv("vehicle.csv")
    return df_export_vehicle

#df is the base data frame that the data is stored as
df = pandas.read_csv("All Data.csv")

#stores dataframes for finished weather, location, driver dataframes
df_weather = export_weather(df)
df_location = export_location(df)
df_driver = export_driver(df)
df_animal = export_animal(df)
df_vehicle = export_vehicle(df)





#create dataframe to store data for accident
df_accident = df[['DirOfCollision', 'ACCIDENTDATE', 'ReportingAgency']]

#set accDate to the date portion of the ACCIDENTDATE field through applying the get_date function
df_accident["accDate"] = df_accident["ACCIDENTDATE"].apply(get_date)


#set accTime to the time portion of the ACCIDENTDATE field through applying the get_time function
df_accident["accTime"] = df_accident["ACCIDENTDATE"].apply(get_time)
#remove the useless end of the time field using rstrip
df_accident["accTime"] = df_accident["accTime"].map(lambda x: x.rstrip('.'));

#drops the now useless datetime field
df_accident.drop(['ACCIDENTDATE'], axis=1, inplace=True)


#create new dataframe to hold only the fields that need to be in the accident table
df_final_accident = df_accident[['DirOfCollision', 'accDate', 'accTime', 'ReportingAgency']]
df_final_accident.rename(columns={'ReportingAgency': 'agency', 'DirOfCollision': 'collisionDir'}, inplace=True)

#merge df and df_location so that the master table has the location primary key
mergedLocation = pandas.merge(df, df_location, how='left', left_on=['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics'],
                      right_on=['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics'])

#merge df and df_weather so that the master table has the weather primary key
mergedWeather = pandas.merge(df, df_weather, how='left', left_on=['Weather', 'SurfaceCondition', 'DayNight'],
                             right_on=['Weather', 'SurfaceCondition', 'DayNight'])

#merge df and df_driver so that the master table has the location primary key
mergedDriver = pandas.merge(df, df_driver, how='left', left_on=['Impairment', 'InjuryType'],
                            right_on=['Impairment', 'InjuryType'])

#create fields in accident to hold foreign key values from merged dataframes
df_final_accident['driverID'] = mergedDriver['driverID']
df_final_accident['condID'] = mergedWeather[['condID']]
df_final_accident['locID'] = mergedLocation[['locID']]
df_export_accident = df_final_accident[['locID', 'condID', 'driverID', 'collisionDir', 'accDate', 'accTime',
                                        'agency']]
df_export_accident.index += 1
df_export_accident['accID'] = df_export_accident.index
df_export_accident = df_export_accident[['accID', 'locID', 'condID', 'driverID', 'collisionDir', 'accDate', 'accTime',
                                        'agency']]
df_export_accident.to_csv("accident.csv", index=False)


df_city = df_location[['locID', 'CITYORTOWN']]
df_location.drop(['CITYORTOWN'], axis=1, inplace=True)
df_location = df_location.rename(columns={"STREETADDRESS": "streetAddress", "RoadCharacteristics": "roadChar"})
df_location = df_location[["locID", "streetAddress", "roadChar"]]
df_location.to_csv("location.csv", index=False)
df_city.to_csv("city.csv", index=False)














