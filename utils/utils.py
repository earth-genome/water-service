import paths
paths.fix_path()

import urllib
import random
import json


def in_polygon(point, poly):
    """Accepts a point [lon, lat] and a polygon [[lon1, lat1], [lon2, lat2],
    ...] and determines whether the point is within the supplied polygon.
    Returns a boolean."""
    x, y = point
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def gen_point(bbox):
    x = random.uniform(bbox['xmin'], bbox['xmax'])
    y = random.uniform(bbox['ymin'], bbox['ymax'])
    return [x, y]


def bounding_box(coords):
    xs = [x for x, y in coords]
    ys = [y for x, y in coords]
    return dict(
        xmin=min(xs),
        xmax=max(xs),
        ymin=min(ys),
        ymax=max(ys)
    )


def to_point(x, y):
    conf = random.uniform(0, 1)
    return {
        "type": "Feature",
        "properties": {
            "conf": conf
        },
        "geometry": {
            "type": "Point",
            "coordinates": [x, y]
        }
    }


def get_url(geo):
    base = 'http://geojson.io/#data=data:application/json,'
    url = base + urllib.quote(json.JSONEncoder().encode(geo))
    return url


def to_poly(coords, viewer=True):

    if coords[0] != coords[-1]:
        coords = coords + [coords[0]]

    geo = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [coords]
        }
    }

    base = 'http://geojson.io/#data=data:application/json,'
    url = base + urllib.quote(json.JSONEncoder().encode(geo))
    if viewer is True:
        geo['properties'] = dict(url=url)

    return geo


def scale_poly(coords, scale=0.5):
    def _average(s): return sum(s) * 1.0 / len(s)

    mean_x = _average([x for x, y in coords])
    mean_y = _average([y for x, y in coords])

    def _scale(x, y):
        sx = mean_x + scale * (x - mean_x)
        sy = mean_y + scale * (y - mean_y)
        return [sx, sy]

    return [_scale(x, y) for x, y in coords]


def poly_area(coords):
    n = len(coords)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
        print area
    area = abs(area) / 2.0
    return area
