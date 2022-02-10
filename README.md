
<div align="center">
    <img src="media/radschnellweg-stvo-sign.svg" width="150">
    <h1>Radschnellwege Deutschland</h1>
</div>

> This project is in progress. Accuracy of ways are getting improved as time flows and the Radschnellwege have finished planning.

> There are still Radschnellwege and attributes of them missing. Open a pull-request, an issue or contact me when you want to improve something.

A list, map, database (call it how you like) of planned, currently build and finished fietssnelweg (Radschnellwege) in Germany. All handmade and updated manually.

The format is a [GeoJSON](https://geojson.org/) file. Just open it in your favorite GeoJSON viewer. The GeoJSON consists of `LineString` and `MultiLineString`, when there are ways which splits (Y-ways).

Contains map data from OpenStreetMap, which has the attribute `copyright="OpenStreetMap"`; © OpenStreetMap contributors. Therefore [LICENSE](LICENSE) does only apply on data which has no copyright attribute.

## Data

Every cycle highway is organized in it's own folder. Every cycle highway CAN have multiple versions because of 

### States
A cycle highway can be in the following states [attribute `state`]:
* `planning` - It is in one of the planning phases
* `built` - The cycle highway part is finished and ready for usage 
* `discarded` - While planning it does not meet the requirements or it is not disred anymore

### Planning Phases

Since this repository should represent build status of the cycle highways, these are the planning phases used exclusively in this order:
1. Pilot study [`pilot`]
2. Preliminary planning [`preliminary`]
3. Design planning [`design`]
4. Approval procedure [`approval`]
5. Execution planning [`execution`]
6. Building [`building`]

Planning phases are assigned through attribute `planning_phase`. The attribute is empty, when the cycle highway is finished. For example a cycle highway in *approval procedure* SHOULD be assigned like this: 
```jsonc
{
    // ..
    "state": "planning",
    "planning_phase": "approval",
    // ..
}
```

If needed, the planning phase can be further described with the attribute `description:planning_phase`. It MUST contain a `string`, which is usually a text, describing any details.

When a cycle highway get's discarded, the planning phase it stucked and SHOULD still be part of the cycle highway.
Politically discussed cycle highways, where planning has not begun, SHOULD NOT be part of this dataset. 

### Variants
Usually in the early planning phases there are multiple possible variants of the cycle highway. Every variant includes the complete route from start to end. It additionally has the following `variant` attribute.

```jsonc
{
    // ..
    "variant": {
        "ref": "2",
        "name": "Trassenvariante 2"
    }
}
```
 The preferred route CAN have the `"ref": "default"`, but MUST be present.

### Example (Geo)JSON

The data model is the following [`JSON Schema`](), with allowed/example values.

```jsonc
{
    "relation": {
        "ref": "RS1", // official abbreviation
        "name": "Radschnellweg Ruhr RS1",
        "from": "Duisburg",
        "to": "Hamm",
    },
    "status": "planning",
    "planning_phase": "design",
    "authority": "Ministerium für Verkehr des Landes Nordrhein-Westfalen", // contracting authority who ordered / paying the cycle highway
    "region": "Nordrhein-Westfalen", // 
    "detail_level": "exact", 
    "length": 104.0, // in kilometer
    "finished": "2024", // [optional] Year of finishing or expected finishing 
    "cost": "", // [optional] All costs summarized, usually in Euro (€)
    "copyright:geometry": "OpenStreetMap", // [optional] If map data from other source
    "references": {
        "osm_relation": "5697663", // [optional] Referencing to the complete route, usually after at least one part has been built
        "website": "https://www.radschnellwege.nrw/rs1-radschnellweg-ruhr",
        "download:pilot_study": "", // [optional] Link to PDF
    }
}
```

## See more

- [Explanation of Radschnellweg](https://de.wikipedia.org/wiki/Radschnellweg) in German Wikipedia
- [List of Radschnellwege](https://de.wikipedia.org/wiki/Liste_der_Radschnellverbindungen_in_Deutschland) in German Wikipedia
- [Explanation of Cycle Highways](https://cyclehighways.eu/about/what-is-a-cycle-highway.html) in CHIPS EU Project
- [Map of this data](https://radschnellwege.chilla.dev)