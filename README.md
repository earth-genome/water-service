## water-service

The objective of this repository is to serve out surface water data from
Landsat 7 satellite imagery.  

**Base URL**

http://

| parameter | type  | default         | format      | description                                         |
|-----------|-------|-----------------|-------------|-----------------------------------------------------|
| geometry  | list  | n/a             | [[lat, lon], [lat, lon], ...]        | list of lat-lon tuples defining the are of interest |
| begin     | date  | n/a             | YYYY-MM-DD  | begin date                                          |
| end       | date  | **today**       | YYYY-MM-DD  | end date                                            |



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

![Screenshot](http://i.imgur.com/AzFhiAB.gif)