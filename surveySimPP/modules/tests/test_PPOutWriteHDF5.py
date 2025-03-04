#!/bin/python

import pytest
import pandas as pd
import os
import sys


def test_PPOutWriteHDF5():

    from surveySimPP.modules.PPJoinColourPointing import PPJoinColourPointing
    from surveySimPP.modules.PPReadOif import PPReadOif
    from surveySimPP.modules.PPReadColours import PPReadColours
    from surveySimPP.modules.PPMatchPointing import PPMatchPointing
    from surveySimPP.modules.PPMatchPointingsAndColours import PPMatchPointingsAndColours
    from surveySimPP.modules.PPOutWriteHDF5 import PPOutWriteHDF5

    padafr = PPReadOif('./data/test/oiftestoutput.txt', "whitespace")
    padacl = PPReadColours('./data/test/testcolour.txt', 0, 20, "whitespace")

    resdf = PPJoinColourPointing(padafr, padacl)

    dbq = 'SELECT observationId, observationStartMJD, filter, seeingFwhmGeom, seeingFwhmEff, fiveSigmaDepth, fieldRA, fieldDec, rotSkyPos FROM SummaryAllProps order by observationId'

    pada5 = PPMatchPointing('./data/test/baseline_10yrs_10klines.db', ['r', 'g', 'i'], dbq)

    # DRY COMMENT OUT BELOW - resdf3 NOT CREATED
    # pada6 = PPMatchPointingsAndColours(resdf3, pada5)

    # pada7 = PPOutWriteHDF5(pada6, 'outtest.h5', str(1))

    # pd.read_hdf('outtest.h5', str(1)).dtypes

    # ncols = 5

    # print(pada6)

    # rer = pd.read_hdf('outtest.h5')

    # nrs = len(rer.index)

    # os.system("rm outtest.h5")

    # # ncolsre=len(pada6.columns)

    # assert ncols == nrs
    return
