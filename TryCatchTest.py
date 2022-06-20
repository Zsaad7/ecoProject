import numpy as np
import pymysql.cursors
# Connect to the database

connection = pymysql.connect(host='127.0.0.1',
                             user='szridi',
                             password='szridi',
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try: 
    with connection:
 
        with connection.cursor() as cursor:
        # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('saadzridi@zsaadcode.org', 'hellohello'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection.commit()

        with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('saadzridi@zsaadcode.org',))
            result = cursor.fetchone()
            print(result)
except Exception : 
    print('Error akhi,khasha tban f SonarQube a bebe ')        
        
