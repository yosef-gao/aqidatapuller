from sae.storage import Bucket
from StringIO import StringIO

class CSVGenerator(object):
    BUCKET_NAME = 'aqi'
    TITLE = 'Site,Parameter,Date(LST),Year,Month,Day,Hour,Value,Unit,Duration\r\n'

    def __init__(self, site):
        self.site = site
        self.filename = '%s.csv' % site
        self.file = StringIO()
        self.file.write(CSVGenerator.TITLE)

    def write_line(self, value, datetime):
        self.file.write(self.site + ',')
        self.file.write('PM2.5,')
        self.file.write(datetime.__str__() + ',')
        self.file.write('%d,' % datetime.year)
        self.file.write('%d,' % datetime.month)
        self.file.write('%d,' % datetime.day)
        self.file.write('%d,' % datetime.hour)
        self.file.write('%d,' % value)
        self.file.write('ug/m3,1 Hr\r\n')

    def generate_csv_file(self):
        bucket = Bucket(CSVGenerator.BUCKET_NAME)
        print self.filename
        bucket.put_object(self.filename, self.file.getvalue())
        return bucket.generate_url(self.filename)
