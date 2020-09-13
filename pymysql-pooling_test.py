from pymysqlpool.pool import Pool
from secrets import MARIADB_USER, MARIADB_DB, MARIADB_PASSWORD, MARIADB_HOST

pool = Pool(host=MARIADB_HOST, user=MARIADB_USER, password=MARIADB_PASSWORD,
            db=MARIADB_DB, autocommit=True)
pool.init()

connection = pool.get_conn()
cur = connection.cursor()
cur.execute('SELECT * FROM web2020_events WHERE location IS NULL')
print(cur.fetchone())

pool.release(connection)

print('Finished')
