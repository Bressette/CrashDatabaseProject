import pandas
import sanitizeTables as fix


#function that exports the dataframe passed in to "Weather CSV.csv"
def export_weather(df_weather):
    df_weather.to_csv("Weather CSV.csv", index=False)

#function that exports the dataframe passed in to "driver.csv"
def export_driver(df_driver):
    df_driver.to_csv("driver.csv", index=False)

#function that sanitizes the accident dataframe passed in and exports it
#to "accident.csv"
def export_accident(df_accident):
    df_export_accident = df_accident[['locID', 'condID', 'driverID', 'collisionDir', 'accDate', 'accTime',
                                      'agency']]
    df_export_accident.index += 1
    df_export_accident['accID'] = df_export_accident.index
    df_export_accident = df_export_accident[
        ['accID', 'locID', 'condID', 'driverID', 'collisionDir', 'accDate', 'accTime',
         'agency']]
    df_export_accident['collisionDir'] = df_export_accident['collisionDir'].replace(
        to_replace="Other - Explain in Narrative", value="Unknown")
    df_export_accident['collisionDir'] = df_export_accident['collisionDir'].fillna("Unknown")
    df_export_accident = fix.sanitize_collision_dir(df_export_accident)
    df_export_accident.to_csv("accident.csv", index=False)
    return df_export_accident


#function that reformats the location table and exports it to "location.csv"
def export_location(mergedAddress):
    mergedAddress.drop(['locID'], axis=1, inplace=True)
    mergedAddress.drop_duplicates(keep='first', inplace=True)
    mergedAddress.reset_index(inplace=True, drop=True)
    mergedAddress.index += 1
    mergedAddress['locID'] = mergedAddress.index
    mergedAddress = mergedAddress[['locID', 'addressID', 'roadChar']]
    mergedAddress.to_csv("location.csv", index=False)
    return mergedAddress


#function that reformats city and exports it to "city.csv"
def export_city(df_city):
    df_city.rename(columns={'CITYORTOWN': 'cityName'}, inplace=True)
    df_city = df_city[['cityID', 'cityName']]
    df_city.to_csv("city.csv", index=False)
    return df_city


#function that reformats address and exports it to "address.csv"
def export_address(mergedAddress, df_location):
    df_export_address = mergedAddress[['streetAddress', 'cityID']]
    df_export_address.drop_duplicates(keep='first', inplace=True)
    df_export_address.reset_index(inplace=True, drop=True)
    df_export_address.index += 1
    df_export_address['addressID'] = df_export_address.index
    df_export_address = df_export_address[['addressID', 'streetAddress', 'cityID']]
    df_export_address.to_csv("address.csv", index=False)
    return df_export_address


#function that reformats animal and exports it to "animal.csv"
def export_animal(df):
    df['accID'] = df.index
    df_animal = df[['accID', 'Animal']]
    df_animal = df_animal.dropna(axis=0, subset=['Animal'])
    df_export_animal = df_animal[df_animal.Animal != "None/Other"]
    df_export_animal = df_export_animal.rename(columns={'Animal': 'animalType'})
    df_export_animal.to_csv("animal.csv", index=False)
    return df_export_animal


#function that reformats vehicle and exports it to "vehicle.csv"
def export_vehicle(df):
    df_vehicle = df[['accID', 'Involving']]
    df_export_vehicle = df_vehicle[df_vehicle.Involving != "None"]
    df_export_vehicle = df_export_vehicle.dropna(subset=['Involving'])
    df_export_vehicle.to_csv("vehicle.csv", index=False)
    return df_export_vehicle