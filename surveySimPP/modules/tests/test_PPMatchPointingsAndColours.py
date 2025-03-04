#!/bin/python

import pytest
import pandas as pd


def test_PPMatchPointingsAndColours():

    from surveySimPP.modules.PPJoinColourPointing import PPJoinColourPointing
    from surveySimPP.modules.PPReadOif import PPReadOif
    from surveySimPP.modules.PPReadColours import PPReadColours
    from surveySimPP.modules.PPMatchPointing import PPMatchPointing
    from surveySimPP.modules.PPMatchPointingsAndColours import PPMatchPointingsAndColours

    padafr = PPReadOif('./data/test/oiftestoutput.txt', 'whitespace')
    padacl = PPReadColours('./data/test/testcolour.txt', 0, 5, 'whitespace')

    resdf = PPJoinColourPointing(padafr, padacl)

    # DRY COMMENT OUT BELOW - PPhookBrightnessWithColour NO LONGER EXISTS
    # resdf1=PPhookBrightnessWithColour(resdf, 'r', 'i-r', 'i')
    # resdf3=PPhookBrightnessWithColour(resdf1, 'r', 'g-r', 'g')

    dbq = 'SELECT observationId, observationStartMJD, filter, seeingFwhmGeom, seeingFwhmEff, fiveSigmaDepth, fieldRA, fieldDec, rotSkyPos FROM SummaryAllProps order by observationId'

    pada5 = PPMatchPointing('./data/test/baseline_10yrs_10klines.db', ['g', 'r', 'i'], dbq)
    # pada6=PPMatchPointingsAndColours(resdf3,pada5)

    # ncols=38
    # ncolsre=len(pada6.columns)

    # assert ncols==ncolsre
    return
