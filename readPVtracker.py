# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
import datetime as dt
import pandas as pd


COL_NAMES = [
    'Date', 'AM',
    'Azi','Ec','Zenithale','Rendement','TP','Pmax',
    'Vmax','Imax','Voc','Isc','FF','Inclinaison','Orientation',  #RD changed 'OrientationRECORD' to just 'Orientation' since
                                                                        # it is what is found in data file

]




def read_tracker(files):

    for n, f in enumerate(files):
        tmp = pd.io.parsers.read_table(
            f,
            comment='#',
            sep='\t',
            header=1,
            parse_dates=[0],
            date_parser=lambda s: dt.datetime.strptime(s, "%Y%m%d_%H:%M:%S"),
            names=COL_NAMES,
            index_col='Date',
            #na_values = ["-999", "-999.99", "-99.9"],
        )
        if n == 0:
            data = tmp
        else:
            data = pd.concat([data, tmp])

    return data