import pandas

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


