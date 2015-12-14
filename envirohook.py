from utils import utils
from utils import water


def water_service(coords, date, viewer=False):
    poly = utils.to_poly(coords, viewer=viewer)
    year = int(date.split("-")[0])
    res = water.surface_water(poly['geometry']['coordinates'], year)

    return dict(
        area=res['area'],
        result=res['geom'],
        date=date,
        poly=poly
    )


def water_series_service(coords, begin, end, viewer=False):
    poly = utils.to_poly(coords, viewer=viewer)
    res = water.water_series(poly['geometry']['coordinates'], begin, end)

    return dict(
        count=len(res),
        result=res,
        begin=begin,
        end=end,
        poly=poly
    )
