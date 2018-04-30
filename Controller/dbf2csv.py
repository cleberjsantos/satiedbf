# -*- coding: utf-8 -*-

from Controller.Utils import DBFRead, pyqt_pdb
from Controller.config import ENCODING_SUPPORT
from Controller.dbfread.exceptions import MissingMemoFile
import csv


def Tocsv(self, header=[], data=[]):
    """ """
    delimiter = ','
    quotechar = '"'
    quoting = csv.QUOTE_ALL

    if header and data:
        with open(self, 'w') as f:
            writer = csv.writer(f, delimiter=delimiter,
                                quotechar=quotechar, quoting=quoting)
            writer.writerow(header)
            writer.writerows(data)
    else:
        path = self

        if path.endswith('.dbf'):
            pathcsv = path.replace('.dbf',
                                   '.csv')
            try:
                dbf = DBFRead(path).dbf
                with open(pathcsv, 'w') as f:
                    writer = csv.writer(f, delimiter=delimiter,
                                        quotechar=quotechar, quoting=quoting)
                    # Header
                    writer.writerow(dbf.field_names)

                    # Data
                    for record in dbf:
                        writer.writerow(list(unicode(s).encode("utf-8") for s in record.values()))
            except Exception as e:
                raise
