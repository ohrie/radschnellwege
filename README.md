
<div align="center">
    <img src="media/radschnellweg-stvo-sign.svg" width="150">
    <h1>Radschnellwege Deutschland</h1>
</div>

> This project is in progress. Accuracy of ways are getting improved as time flows and the Radschnellwege have finished planning.

> There are still Radschnellwege and attributes of them missing. Open a pull-request, an issue or contact me when you want to improve something.

A list, map, database (call it how you like) of planned, currently build and finished fietssnelweg (Radschnellwege) in Germany. All handmade and updated manually.

The format is a [GeoJSON](https://geojson.org/) file. Just open it in your favorite GeoJSON viewer. The GeoJSON consists of `LineString` and `MultiLineString`, when there are ways which splits (Y-ways).

Contains map data from OpenStreetMap, which has the attribute `copyright="OpenStreetMap"`; © OpenStreetMap contributors.

## Attributes

The data model is the following, with example values.

```json
{
    "ref": "RS1", // official abbreviation
    "name": "Radschnellweg Ruhr RS1", // [optional] only if official name
    "from": "Duisburg",
    "to": "Hamm",
    "state": "examined | evaluation | planned | planning | under_construction | partly_built | built | not_realised | test",
    "responsible": "Senatsverwaltung Berlin",
    "accuracy": "corridor | rough | exact", 
    "osm_relation": "5697663", // [optional] Only if relation exists
    "website": "https://www.radschnellwege.nrw/rs1-radschnellweg-ruhr",
    "pilot_study": "", // [optional] Link to PDF
    "length": "104.0", // in kilometer
    "finished": "2024", // [optional] Year of finishing or expected finishing 
    "copyright": "OpenStreetMap" // [optional] If map data from other source
}
```

## See more

- [Explanation of Radschnellweg](https://de.wikipedia.org/wiki/Radschnellweg) in German Wikipedia
- [List of Radschnellwege](https://de.wikipedia.org/wiki/Liste_der_Radschnellverbindungen_in_Deutschland) in German Wikipedia
- [Explanation of Cycle Highways](https://cyclehighways.eu/about/what-is-a-cycle-highway.html) in CHIPS EU Project
