import MySQLdb
import sae.const

MYSQL_DB = sae.const.MYSQL_DB
MYSQL_USER = sae.const.MYSQL_USER
MYSQL_PASS = sae.const.MYSQL_PASS
MYSQL_HOST_M = sae.const.MYSQL_HOST
MYSQL_HOST_S = sae.const.MYSQL_HOST_S
MYSQL_PORT = int(sae.const.MYSQL_PORT)

class Mysql:
    def __init__(self):
        self.db = MySQLdb.Connection(host=MYSQL_HOST_M, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB)
        self.cur = self.db.cursor()

    def query_site_id(self, site):
        count = self.cur.execute(''' select site_id from site_table where site = '%s' ''' % site)
        if count == 0:
            return 0
        else:
            return self.cur.fetchone()[0]

    def query_data(self, site):
            try:
                site_id = self.query_site_id(site)
                if site_id == 0:
                    print 'site %s has no data' % site
                else:
                    self.cur.execute('select value, date from pm25_value_table where site_id = %d order by date' % site_id)
                    results = self.cur.fetchall()
                    return results
            except MySQLdb.Error, e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def insert_site(self, site):
        count = self.cur.execute(''' insert into site_table (`site`) values('%s') ''' % site)
        site_id = self.cur.lastrowid
        self.db.commit()
        if count == 0:
            return 0
        else:
            return site_id

    def insert_data(self, site, value):
        try:
            site_id = self.query_site_id(site)
            # if no such site, create it
            if site_id == 0:
                site_id = self.insert_site(site)
            count = self.cur.execute(''' insert into pm25_value_table (`date`, `value`, `site_id`) values(now(), %d, %d) ''' % (value, site_id))
            self.db.commit()
            return count
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])


