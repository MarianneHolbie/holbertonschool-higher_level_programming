#!/usr/bin/python3
"""
    Script to get all cities of a specific state
    from the database hbtn_0e_0_usa

    ARGUMENTS :
            mysql username
            mysql password
            database name
            state_name
    SORTED BY :
        ASC states.id
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Recover argument from user
    user = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect database
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=pswd, db=db_name, port=3306)

    # create cursor
    cur = db.cursor()

    # executing MySQL Queries in Python
    querry = """SELECT cities.name FROM cities \
            LEFT JOIN states ON states.id = cities.state_id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"""
    cur.execute(querry, (state_name,))

    # construct string response
    # cut tuple, add sep
    all_cities = cur.fetchall()
    result = ""
    sep = ""
    for cities in all_cities:
        result = result + sep + cities[0]
        sep =", "
    print(result)

    # close cursor & db
    cur.close()
    db.close()
