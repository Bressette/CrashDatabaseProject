import pandas


def get_date(s):
    s = s.rsplit("T", maxsplit=1)[0]
    return s


def get_time(s):
    s = s.rsplit("T", maxsplit=1)[1]
    s = s.replace("Z", "")
    return s


#df is the base data frame that the data is stored as
df = pandas.read_csv("All Data.csv")
print(df)
print(list(df))

df_weather = df[['Weather', 'SurfaceCondition', 'DayNight']]
print(df_weather)
df_weather.drop_duplicates(keep='first', inplace=True)
df_weather.reset_index(inplace=True, drop=True)
print(df_weather)
df_weather.to_csv("Weather CSV.csv")

df_location = df[['STREETADDRESS', 'CITYORTOWN', 'RoadCharacteristics']]
df_location.drop_duplicates(keep='first', inplace=True)
df_location.reset_index(inplace=True, drop=True)
df_location.to_csv("location.csv")

df_driver = df[['Impairment', 'InjuryType']]
df_driver.drop_duplicates(keep='first', inplace=True)
df_driver.reset_index(inplace=True, drop=True)
print(df_driver)
df_driver.to_csv("driver.csv")

df_animal = df[['Animal']]
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

df_final_accident.to_csv("accident.csv")











