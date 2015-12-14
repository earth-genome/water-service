## water-service

The objective of this repository is to provision global data on surface water
from Landsat 7 satellite imagery.  This project represents a layer on top of
Earth Engine, operationalizing remote sensing science for web app development.

**Base URL**

http://

| parameter | type  | default         | format      | description                                         |
|-----------|-------|-----------------|-------------|-----------------------------------------------------|
| geometry  | list  | n/a             | [[lat, lon], [lat, lon], ...]        | list of lat-lon tuples defining the are of interest |
| begin     | date  | n/a             | YYYY-MM-DD  | begin date                                          |
| end       | date  | **today**       | YYYY-MM-DD  | end date                                            |

**Example URL**

[http://water-test.appspot.com/water/series?coords=[[-119.93,39.33],[-119.93,39.35],[-119.90,39.35],[-119.90,39.33],[-119.93,39.33]]&begin=2010-02-02&end=2011-02-02](http://water-test.appspot.com/water/series?coords=[[-119.93,39.33],[-119.93,39.35],[-119.90,39.35],[-119.90,39.33],[-119.93,39.33]]&begin=2010-02-02&end=2011-02-02)

```json
{
    "count": 12,
    "begin": "2010-02-02",
    "end": "2011-02-02",
    "result": [
        {
            "date": "2010-02-02",
            "area": 0.546627708789871
        },
        {
            "date": "2010-03-06",
            "area": 0.9044314584855125
        },
        "..."
        {
            "date": "2011-01-01",
            "area": 0.9385196006817629
        }
    ],
    "poly": {
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -119.93,
                        39.33
                    ],
                    [
                        -119.93,
                        39.35
                    ],
                    [
                        -119.9,
                        39.35
                    ],
                    [
                        -119.9,
                        39.33
                    ],
                    [
                        -119.93,
                        39.33
                    ]
                ]
            ]
        },
        "type": "Feature"
    }
}
```

### Using the API: **example web application**

A very simple web app that displays the data allows the user to draw a
bounding box.  The returned geometry is overlaid on the basemap, along with
the water series as a [D3](http://d3js.org/) plot.  The displayed water body
is [Washoe Lake](https://en.wikipedia.org/wiki/Washoe_Lake), just north of
Carson City, Nevada.  Washoe Lake has "dried up a number of times since 1977,"
according to an [article](http://www.kolotv.com/home/headlines/Drought-
evaporation-leaves-popular-Washoe-Lake-dry-Eds-APNewsNow-303790141.html) from
a local news organization.  When and how much?  The web app allows users to
watch the lake cycles and annual average extent of the lake.  You can watch
the change.

![Screenshot](https://dl.dropboxusercontent.com/u/5365589/water.gif)

### Development

The API runs on the Google [App Engine Python SDK](https://cloud.google.com/ap
pengine/downloads#Google_App_Engine_SDK_for_Python), which includes a web
server application you can run on your computer that "simulates your
application running in the App Engine Python runtime environment."  To run
locally, you will first have to contact
[**@danhammer**](https://github.com/danhammer) for credentials to access the
backend.
