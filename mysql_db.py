import MySQLdb
import sae.const

MYSQL_DB = sae.const.MYSQL_DB
MYSQL_USER = sae.const.MYSQL_USER
MYSQL_PASS = sae.const.MYSQL_PASS
MYSQL_HOST_M = sae.const.MYSQL_HOST
MYSQL_HOST_S = sae.const.MYSQL_HOST_S
MYSQL_PORT = int(sae.const.MYSQL_PORT)

def mysql():
    connection = MySQLdb.connection(host=MYSQL_HOST_M, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS)
    connection.select_db(MYSQL_DB)
    connection.query("""select * from site_table""")
    r = connection.store_result()
    result = r.fetch_row()
    return result

