import pandas
import numpy as np


def get_date(s):
    s = s.rsplit("T", maxsplit=1)[0]
    return s


def get_time(s):
    s = s.rsplit("T", maxsplit=1)[1]
    s = s.replace("Z", "")
    return s


def get_loc_id(df, df_location, df_accident):
    merged = pandas.merge(df, df_location, on=['STREETADDRESS'], how='inner')
    merged.head()
    return df_accident


#df is the base data frame that the data is stored as
df = pandas.read_csv("All Data.csv")
print(df)
print(list(df))

df_weather = df[['Weather', 'SurfaceCondition', 'DayNight']]
print(df_weather)
df_weather.drop_duplicates(keep='first', inplace=True)
df_weather.reset_index(inplace=True, drop=True)
df_weather.index += 1
df_weather['condID'] = df_weather.index;
print(df_weather)
df_weather.to_csv("Weather CSV.csv")

df_location = df[['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics']]
df_location.drop_duplicates(keep='first', inplace=True)
df_location.reset_index(inplace=True, drop=True)
df_location.index += 1
df_location['locID'] = df_location.index;
df_location.to_csv("location.csv")

df_driver = df[['Impairment', 'InjuryType']]
df_driver.drop_duplicates(keep='first', inplace=True)
df_driver.reset_index(inplace=True, drop=True)
df_driver.index += 1
df_driver['driverID'] = df_driver.index
print(df_driver)
df_driver.to_csv("driver.csv")

df.index += 1
df['accID'] = df.index
df_animal = df[['accID', 'Animal']]
df_animal.to_csv("animal.csv")




#creates new columns to store separated date and time
df_accident = df[['DirOfCollision', 'ACCIDENTDATE', 'ReportingAgency']]
df_accident["accDate"] = df_accident["ACCIDENTDATE"].apply(get_date)
print(df_accident)

df_accident["accTime"] = df_accident["ACCIDENTDATE"].apply(get_time)
print(df_accident)

df_accident.drop(['ACCIDENTDATE'], axis=1, inplace=True)

print(df_accident)
print(list(df_accident))

df_final_accident = df_accident[['DirOfCollision', 'accDate', 'accTime', 'ReportingAgency']]
df_final_accident.rename(columns={'ReportingAgency': 'agency', 'DirOfCollision': 'collisionDir'}, inplace=True)

print(df_final_accident)
#df_final_accident.to_csv("accident.csv")

print("Printing Merged")
mergedLocation = pandas.merge(df, df_location, how='left', left_on=['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics'],
                      right_on=['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics'])
print(mergedLocation)
print(list(mergedLocation))

mergedWeather = pandas.merge(df, df_weather, how='left', left_on=['Weather', 'SurfaceCondition', 'DayNight'],
                             right_on=['Weather', 'SurfaceCondition', 'DayNight'])
print(mergedWeather)
print(list(mergedWeather))

mergedDriver = pandas.merge(df, df_driver, how='left', left_on=['Impairment', 'InjuryType'],
                            right_on=['Impairment', 'InjuryType'])

print(mergedDriver)
print(list(mergedDriver))

df_final_accident['driverID'] = mergedDriver['driverID']
df_final_accident['condID'] = mergedWeather[['condID']]
df_final_accident['locID'] = mergedLocation[['locID']]
print("Printing final accident")
print(df_final_accident)
print(list(df_final_accident))
df_export_accident = df_final_accident[['locID', 'condID', 'driverID', 'collisionDir', 'accDate', 'accTime',
                                        'agency']]
df_export_accident.to_csv("accident.csv")

df_vehicle = df[['accID', 'Involving']]
df_vehicle.to_csv("vehicle.csv")







