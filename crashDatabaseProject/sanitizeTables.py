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


#function that formats the location by dropping invalid values
#and renaming the fields to match the database schema
def format_location(mergedCity):
    mergedCity.drop(['CITYORTOWN'], axis=1, inplace=True)
    mergedCity = mergedCity.rename(columns={"STREETADDRESS": "streetAddress", "RoadCharacteristics": "roadChar"})
    mergedCity = mergedCity[["locID", "cityID", "streetAddress", "roadChar"]]
    mergedCity["roadChar"] = mergedCity["roadChar"].replace(to_replace="Other - Explain in Narrative",
                                                                      value="Not Reported")
    mergedCity["roadChar"] = mergedCity["roadChar"].fillna("Not Reported")
    mergedCity["streetAddress"] = mergedCity["streetAddress"].fillna("Not Reported")
    return mergedCity

#function that replaces invalid values in the collisionDir field in accident
def sanitize_collision_dir(df):
    df['collisionDir'] = df['collisionDir'].replace(to_replace="No Turns, Thru moves only, Broadside ^<",
                                                    value="No Turns, Thru moves only, Broadside")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Left Turn and Thru, Angle Broadside -->v--",
                                                    value="Left Turn and Thru, Angle Broadside")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Left Turn and Thru, Broadside v<--",
                                                    value="Left Turn and Thru, Broadside")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Left Turn and Thru, Head On ^v--",
                                                    value="Left Turn and Thru, Head On")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Left Turns, Same Direction, Rear End v--v--",
                                                    value="Left Turns, Same Direction, Rear End")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Right Turn and Thru, Angle Broadside -->^--",
                                                     value="Right Turn and Thru, Angle Broadside")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Right Turn and Thru, Head On v^--",
                                                    value="Right Turn and Thru, Head On")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Right Turn and Thru, Broadside ^<--",
                                                    value="Right Turn and Thru, Broadside")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Left and Right Turns, Simultaneous Turn Crash --vv--",
                                                    value="Left and Right Turns, Simultaneous Turn Crash")
    df['collisionDir'] = df['collisionDir'].replace(to_replace="Right Turn, Same Direction, Rear End ^--^--",
                                                    value="Right Turn, Same Direction, Rear End")
    return df

#function that sanitizes weather by replacing invalid values
def sanitize_weather(df_weather):
    df_weather['surfaceCond'] = df_weather['surfaceCond'].replace(to_replace="Not Reported", value="Unknown")
    df_weather['surfaceCond'] = df_weather['surfaceCond'].replace(to_replace="Other - Explain in Narrative",
                                                                  value="Unknown")
    df_weather['surfaceCond'] = df_weather['surfaceCond'].fillna("Unknown")
    df_weather['dayNight'] = df_weather['dayNight'].fillna("Unknown")
    return df_weather

#function that fills nulls in driver
def sanitize_driver(df_driver):
    df_driver['driverImpair'] = df_driver['driverImpair'].fillna("None")
    df_driver['driverDamage'] = df_driver['driverDamage'].fillna("Unknown")
    return df_driver


#function that merges the city and address table to give address the foreign key from city
def merge_city_address(df_location, df_city, df_address):
    mergedCity = pandas.merge(df_location, df_city, how='left', left_on=['CITYORTOWN'], right_on=['CITYORTOWN'])
    mergedCity = format_location(mergedCity)

    mergedAddress = pandas.merge(mergedCity, df_address, how='left', left_on=['streetAddress'],
                                 right_on=['streetAddress'])
    return mergedAddress