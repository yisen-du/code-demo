import configparser
import pymysql


def mysqlconnect():
    # To connect MySQL database
    config = configparser.ConfigParser()
    config.read('config.ini')

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password=config['mysql']['password'],
        database='classicmodels'
    )

    cur = conn.cursor()

    # Select query
    cur.execute("select * from employees")
    output = cur.fetchall()

    for i in output:
        print(i)

    # To close the connection
    conn.close()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()
