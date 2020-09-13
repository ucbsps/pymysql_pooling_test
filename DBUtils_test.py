import pymysql
from DBUtils.PooledDB import PooledDB

from secrets import MARIADB_USER, MARIADB_DB, MARIADB_PASSWORD, MARIADB_HOST

pool = PooledDB(creator=pymysql, host=MARIADB_HOST, user=MARIADB_USER,
                password=MARIADB_PASSWORD, database=MARIADB_DB,
                autocommit=True, ping=1)

conns = [None] * 10

for i in range(0, 1000):
    conns.append(pool.connection())
    cur = conns[-1].cursor()
    cur.execute('show status like "Threads_connected"')
    print(cur.fetchone()[1])

    cur.close()
    if conns[0] is not None:
        conns[0].close()
    conns = conns[1:]

print('Finished')
