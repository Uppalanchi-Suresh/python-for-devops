def update_server_config(file_path, key, value):

    with open(file_path, 'r') as file:
        lines = file.readlines() # readlines() is an inbuilt function (it will copy everything in to lines variable)

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n") # if file has the key which I provide only then update it
            else:
                file.write(line) # if file doesn't have the key provided, then return the same value.

update_server_config ('server.conf', 'LOG_LEVEL', 'INFO')
            