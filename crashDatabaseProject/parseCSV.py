import pandas
import sanitizeTables as fix
import exportTables as export
import createTables.py as create


#df is the base data frame that the data is stored as
df = pandas.read_csv("All Data.csv")

#stores dataframes for weather, location, driver dataframes
df_weather = create.create_weather(df)
df_location = create.create_location(df)
df_driver = create.create_driver(df)
df_animal = export.export_animal(df)
df_vehicle = export.export_vehicle(df)


df_city = create.create_city(df_location)
df_address = create.create_address(df_location)

mergedAddress = fix.merge_city_address(df_location, df_city, df_address)

df_address = export.export_address(mergedAddress, df_location)
df_location = export.export_location(mergedAddress)
df_city = export.export_city(df_city)


df_driver = df_driver.rename(columns={'Impairment': 'driverImpair', 'InjuryType': 'driverDamage'})
df_driver = df_driver[['driverID', 'driverImpair', 'driverDamage']]

df_accident = create.create_accident(df, df_location, df_weather, df_driver)
df_accident = export.export_accident(df_accident)


df_weather = fix.sanitize_weather(df_weather)
export.export_weather(df_weather)
df_driver = fix.sanitize_driver(df_driver)
export.export_driver(df_driver)








