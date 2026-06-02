import configparser

config = configparser.ConfigParser()
config.read('config.ini')

print(f'Snowflake Username is : {config["Snowflake"]["uid"]}; Snowflake Password is : {config["Snowflake"]["password"]}')

snowflake_username = config["Snowflake"]["uid"]
snowflake_password = config["Snowflake"]["password"]

print(snowflake_username)
print(snowflake_password)

config.set("Xactly", "uid", "Deepak7069")

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print(config['Xactly']['uid'])