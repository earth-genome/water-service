## water-service

The objective of this repository is to serve out surface water data from
Landsat 7 satellite imagery.  


**Base URL**

http://

| parameter | type  | default         | format      | description                                         |
|-----------|-------|-----------------|-------------|-----------------------------------------------------|
| geometry  | list  | n/a             | [[]]        | list of lat-lon tuples defining the are of interest |
| begin     | date  | n/a             | YYYY-MM-DD  | begin date                                          |
| end       | date  | **today**       | YYYY-MM-DD  | end date                                            |


### Example web application

A very simple web app that displays the data allows the user to draw a
bounding box.  The returned geometry is overlaid on the basemap, along with
the water series as a [D3](http://d3js.org/) plot.

![](http://i.imgur.com/3wVCvpa.gifv)