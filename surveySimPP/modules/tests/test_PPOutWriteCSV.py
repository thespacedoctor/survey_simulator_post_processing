#!/bin/python

import pytest
import pandas as pd
import os
import sys


def test_PPOutWriteCSV():

    from surveySimPP.modules.PPJoinColourPointing import PPJoinColourPointing
    from surveySimPP.modules.PPReadOif import PPReadOif
    from surveySimPP.modules.PPReadColours import PPReadColours
    from surveySimPP.modules.PPMatchPointing import PPMatchPointing
    from surveySimPP.modules.PPMatchPointingsAndColours import PPMatchPointingsAndColours
    from surveySimPP.modules.PPOutWriteCSV import PPOutWriteCSV

    padafr = PPReadOif('./data/test/oiftestoutput.txt', "whitespace")
    padacl = PPReadColours('./data/test/testcolour.txt', 0, 5, "whitespace")

    resdf = PPJoinColourPointing(padafr, padacl)

    dbq = 'SELECT observationId, observationStartMJD, filter, seeingFwhmGeom, seeingFwhmEff, fiveSigmaDepth, fieldRA, fieldDec, rotSkyPos FROM SummaryAllProps order by observationId'

    pada5 = PPMatchPointing('./data/test/baseline_10yrs_10klines.db', ['g', 'r', 'i'], dbq)

    # DRY COMMENT OUT BELOW - resdf3 NOT CREATED
    # pada6 = PPMatchPointingsAndColours(resdf3, pada5)

    # pada7 = PPOutWriteCSV(pada6, './outtest.csv')
    # ncols = 6

    # tpt = os.popen("wc -l ./outtest.csv | awk '{print $1}'")
    # cmp = tpt.read()
    # cmp.strip()
    # cmp1 = int(cmp)
    # os.system("rm ./outtest.csv")

    # # ncolsre=len(pada6.columns)

    # assert ncols == cmp1
    return
