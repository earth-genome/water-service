import paths
paths.fix_path()

import ee
from datetime import datetime
import numpy as np


def surface_water(coords, year):

    loc = "L7_TOA_1YEAR/%s" % year

    weights = {
        "b(0)": 0.2626,
        "b(1)": 0.2141,
        "b(2)": 0.0926,
        "b(3)": 0.0656,
        "b(4)": -0.7629,
        "b(6)": -0.5388
    }

    exp = '+'.join(['%s*%s' % (k, v) for k, v in weights.items()])
    poly = ee.Geometry.Polygon(*coords)
    img = ee.Image(loc).clip(poly)
    water = img.expression(exp)
    threshold_exp = "(b(0) > 4) ? 1 : 0"
    binary = water.expression(threshold_exp)

    area = binary.reduceRegion(
        ee.Reducer.mean(),
        poly,
        30,
        None,
        None,
        True
    ).getInfo()

    ct = binary.mask(binary).connectedPixelCount(200)
    x = ct.clip(poly).reduceToVectors(
        ee.Reducer.countEvery(),
        poly,
        100,
        "polygon",
        True,
        "label",
        None,
        None,
        False,
        500000
    )
    res = dict(area=area, geom=x.getInfo())
    return res


def binary_water(img, poly):
    secs = img.get('system:time_start')
    weights = {
        'b("B1")': 0.2626,
        'b("B2")': 0.2141,
        'b("B3")': 0.0926,
        'b("B4")': 0.0656,
        'b("B5")': -0.7629,
        'b("B7")': -0.5388
    }

    exp = '+'.join(['%s*%s' % (k, v) for k, v in weights.items()])
    water = img.expression(exp)
    threshold_exp = '(b(0) > 4) ? 1 : 0'
    binary = water.expression(threshold_exp)

    area = binary.reduceRegion(
        ee.Reducer.mean(),
        poly,
        30,
        None,
        None,
        True
    )

    res = {'area': area, 'date': secs}
    return ee.Feature(None, res)


def water_series(coords, begin, end, N=6):
    coll = ee.ImageCollection('LANDSAT/LE7_L1T_32DAY_RAW')
    poly = ee.Geometry.Polygon(*coords)
    fcoll = coll.filterBounds(poly).filterDate(begin, end)
    feats = fcoll.map(lambda x: binary_water(x, poly)).getInfo()['features']

    def _process(x):
        area = x['properties']['area']['constant']
        secs = x['properties']['date']/1000
        dt = datetime.fromtimestamp(secs).strftime('%Y-%m-%d')
        return {'area': area, 'date': dt}

    entries = sorted([_process(x) for x in feats], key=lambda k: k['date'])
    return entries


