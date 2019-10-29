import pandas

def get_date(s):
    s = s.rsplit("T", maxsplit=1)[0]
    return s

def get_time(s):
    s = s.rsplit("T", maxsplit=1)[1]
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





df_accident = df[['ACCIDENTDATE']]
df_accident["date"] = df_accident["ACCIDENTDATE"].apply(get_date)
print(df_accident)

#df_accident["date"] = df_accident["Dateandtime"].apply(get_date)
#separates the first segment change index to 1 for second part of string
"""
s = "DateTDate2"
s = s.rsplit("T", maxsplit=1)[0]
print(s)
"""










