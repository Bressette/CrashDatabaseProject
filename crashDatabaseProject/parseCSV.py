import pandas
import numpy as np
import sanitizeTables as fix
import exportTables as export

#function that declares a dataframe weather drops duplicates and creates new column
#to hold the index of the dataframe and stores it as condID for a primary key column
def create_weather(df):
    df_weather = df[['Weather', 'SurfaceCondition', 'DayNight']]
    df_weather.drop_duplicates(keep='first', inplace=True)
    df_weather.reset_index(inplace=True, drop=True)
    df_weather.index += 1
    df_weather['condID'] = df_weather.index
    df_weather = df_weather.rename(columns={'Weather': 'weather', 'SurfaceCondition': 'surfaceCond', 'DayNight': 'dayNight'})
    df_weather = df_weather[['condID', 'weather', 'surfaceCond', 'dayNight']]
    return df_weather

#function that declares a dataframe location drops duplicates and creates new column
#to hold the index of the dataframe and stores it as locID for a primary key column
def create_location(df):
    df_location = df[['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics']]
    df_location.drop_duplicates(keep='first', inplace=True)
    df_location.reset_index(inplace=True, drop=True)
    df_location.index += 1
    df_location['locID'] = df_location.index
    return df_location


#function that declares a dataframe driver drops duplicates and creates new column
#to hold the index of the dataframe and stores it as driverID for a primary key column
def create_driver(df):
    df_driver = df[['Impairment', 'InjuryType']]
    df_driver.drop_duplicates(keep='first', inplace=True)
    df_driver.reset_index(inplace=True, drop=True)
    df_driver.index += 1
    df_driver['driverID'] = df_driver.index
    return df_driver

def create_city(df_location):
    df_city = df_location[['CITYORTOWN']]
    df_city.drop_duplicates(keep='first', inplace=True)
    df_city.reset_index(inplace=True, drop=True)
    df_city.index += 1
    df_city['cityID'] = df_city.index
    return df_city





def create_address(df_location):
    df_address = df_location[['STREETADDRESS']]
    df_address['addressID'] = df_address.index
    df_address = df_address.rename(columns={'STREETADDRESS': 'streetAddress'})
    return df_address





def create_accident(df, df_location, df_weather, df_driver):
    # create dataframe to store data for accident
    df_accident = df[['DirOfCollision', 'ACCIDENTDATE', 'ReportingAgency']]

    # set accDate to the date portion of the ACCIDENTDATE field through applying the get_date function
    df_accident["accDate"] = df_accident["ACCIDENTDATE"].apply(fix.get_date)

    # set accTime to the time portion of the ACCIDENTDATE field through applying the get_time function
    df_accident["accTime"] = df_accident["ACCIDENTDATE"].apply(fix.get_time)
    # remove the useless end of the time field using rstrip
    df_accident["accTime"] = df_accident["accTime"].map(lambda x: x.rstrip('.'))

    # drops the now useless datetime field
    df_accident.drop(['ACCIDENTDATE'], axis=1, inplace=True)

    # create new dataframe to hold only the fields that need to be in the accident table
    df_accident = df_accident[['DirOfCollision', 'accDate', 'accTime', 'ReportingAgency']]
    df_accident.rename(columns={'ReportingAgency': 'agency', 'DirOfCollision': 'collisionDir'}, inplace=True)

    # merge df and df_location so that the master table has the location primary key
    mergedLocation = pandas.merge(df, df_location, how='left', left_on=['RoadCharacteristics'],
                                  right_on=['roadChar'])

    # merge df and df_weather so that the master table has the weather primary key
    mergedWeather = pandas.merge(df, df_weather, how='left', left_on=['Weather', 'SurfaceCondition', 'DayNight'],
                                 right_on=['weather', 'surfaceCond', 'dayNight'])

    # merge df and df_driver so that the master table has the location primary key
    mergedDriver = pandas.merge(df, df_driver, how='left', left_on=['Impairment', 'InjuryType'],
                                right_on=['driverImpair', 'driverDamage'])

    # create fields in accident to hold foreign key values from merged dataframes
    df_accident['driverID'] = mergedDriver['driverID']
    df_accident['condID'] = mergedWeather[['condID']]
    df_accident['locID'] = mergedLocation[['locID']]
    return df_accident








#df is the base data frame that the data is stored as
df = pandas.read_csv("All Data.csv")

#stores dataframes for weather, location, driver dataframes
df_weather = create_weather(df)
df_location = create_location(df)
df_driver = create_driver(df)
df_animal = export.export_animal(df)
df_vehicle = export.export_vehicle(df)


df_city = create_city(df_location)
df_address = create_address(df_location)

mergedAddress = fix.merge_city_address(df_location, df_city, df_address)

df_address = export.export_address(mergedAddress, df_location)
df_location = export.export_location(mergedAddress)
df_city = export.export_city(df_city)


df_driver = df_driver.rename(columns={'Impairment': 'driverImpair', 'InjuryType': 'driverDamage'})
df_driver = df_driver[['driverID', 'driverImpair', 'driverDamage']]

df_accident = create_accident(df, df_location, df_weather, df_driver)
df_accident = export.export_accident(df_accident)


df_weather = fix.sanitize_weather(df_weather)
export.export_weather(df_weather)
df_driver = fix.sanitize_driver(df_driver)
export.export_driver(df_driver)








