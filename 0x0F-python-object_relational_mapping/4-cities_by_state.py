#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa
'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) >= 4:

        db_connection = MySQLdb.connect(host='localhost',
                                        port=3306,
                                        user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db=sys.argv[3])

        cur = db_connection.cursor()

        cur.execute('SELECT cities.id, cities.name, states.name FROM cities' +
                    ' INNER JOIN states ON cities.state_id = states.id' +
                    ' ORDER BY cities.id ASC;'
                    )

        row_result = cur.fetchall()
        for row in row_result:
            print(row)

        db_connection.close()
