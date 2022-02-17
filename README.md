
<div align="center">
    <img src="media/radschnellweg-stvo-sign.svg" width="150">
    <h1>Radschnellwege Deutschland</h1>
</div>

> This project is in progress. Accuracy of ways are getting improved as time flows and the Radschnellwege have finished planning.

> There are still Radschnellwege and attributes of them missing. Open a pull-request, an issue or contact me when you want to improve something.

A list, map, database (call it how you like) of planned, currently build and finished cycle highways (Radschnellwege) in Germany. All handmade and updated manually.

The format is a [GeoJSON](https://geojson.org/) file. Just open it in your favorite GeoJSON viewer. The GeoJSON consists of `LineString` and `MultiLineString`, when there are ways which splits (Y-ways).

Contains map data from OpenStreetMap, which has the attribute `copyright="OpenStreetMap"`; © OpenStreetMap contributors. Therefore [LICENSE](LICENSE) does only apply on data which has no copyright attribute.

## Data

Every cycle highway is organized in it's own file. Every cycle highway CAN have multiple variants. 

## Meta Information

Every cycle highway has it's own meta information, independent from the individuals geometry segments. These apply to the cycle highway as a whole.


### Status
A cycle highway MUST have one of the following states, segments CAN have one of the following state:

1. `idea` - Politically discussed and not agreed, planning has not started
2. `agreed` - It has been decided to plan the cycle highway, but planning has not been started
3. `planning` - It is in one of the planning phases
4. `in_progress` - The segments have different planning phases, but as a whole it marches on
5. `done` - The cycle highway part is built, finished and ready for usage 
* `discarded` - While planning it does not meet the requirements or it is not desired anymore

### Stakeholders & Roles

Every organization / institution CAN be part of the `stakeholders` attribute. Every stakeholder MUST have an role. Since `stakeholders` and `roles` are an array there can be multiple stakeholder holding the same role. Stakeholders are also available in *Detail segments*.

**Example:**
```jsonc
"stakeholders": [
    {
        "name": "Regionalverband Ruhr",
        "roles": ["communication"],
        "description": "RVR Ruhr ist zuständig für die Kommunikationsstrategie & -durchführung",
    },
]
```

### Example Meta JSON

The data model is the following [`JSON Schema`](), with allowed/example values.

```jsonc
"meta": {
    "id": "rs1_nrw",
    "general": {
        "ref": "RS1", // official abbreviation
        "name": "Radschnellweg Ruhr RS1",
        "from": "Duisburg, Nordrhein-Westfalen", // State MUST be separated after place name
        "to": "Hamm, Nordrhein-Westfalen",
        "description": "Der RS1 führt auf über 100km von Duisburg nach Hamm unteranderem über Mülheim, Essen, Gelsenkirchen und Dortmund hindurch. Es wurden bereits über 15km fertiggestellt."
    },
    "stakeholders": [
        {
            "name": "Straßen.NRW",
            "roles": ["authority"],
            "description": "",
        },
        {
            "name": "Regionalverband Ruhr",
            "roles": ["communication"],
            "description": "RVR Ruhr ist zuständig für die Kommunikationsstrategie & -durchführung",
        },
    ],
    "status": "planning",
    "planning_phase": "design",
    "detail_level": "exact", 
    "finished": "2024", // [optional] Year (and month) of finishing or expected finishing (format: "YYYY-MM" or "YYYY")
    "cost": 43000, // [optional] All costs summarized, in thousand Euro (€)
    "references": {
        "osm_relation": "5697663", // [optional] Referencing to the complete route, usually after at least one part has been built
        "website": "http://rs1.ruhr",
        "copyright:geometry": "OpenStreetMap", // [optional] If map data from other source
    }
}
```

### Detail Segments

Each segment describes a part of a variant. A segment has attributes describing the condition and information about the cycleway segment. Multiple segments are a variant.

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
"segment": {
    // ..
    "state": "planning",
    "planning_phase": "approval",
}
```

If needed, the planning phase can be further described with the attribute `description:planning_phase`. It MUST contain a `string`, which is usually a text, describing any details.

When a cycle highway get's discarded, the planning phase it stuck and SHOULD still be part of the cycle highway.

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


### Segment attributes

An example for **segment attributes**:
```jsonc
"segment": {
    "id": "rs1_seg598",
    "status": "planning",
    "planning_phase": "design",
    "detail_level": "exact",
    "stakeholders": [
        {
            "name": "Stadt Duisburg",
            "roles": ["authority"],
            "description": "Baulastträger",
        }
    ],
    "variants": ["2a", "2b"], // List of the variants the segment is part of
    "length": 12100 // optional, implicit, MUST be calculated from geometry, in m
}
```

The attribute `segment` would be the properties of the segment in a GeoJSON.

## See more

- [Explanation of Radschnellweg](https://de.wikipedia.org/wiki/Radschnellweg) in German Wikipedia
- [List of Radschnellwege](https://de.wikipedia.org/wiki/Liste_der_Radschnellverbindungen_in_Deutschland) in German Wikipedia
- [Explanation of Cycle Highways](https://cyclehighways.eu/about/what-is-a-cycle-highway.html) in CHIPS EU Project
- [Map of this data: `radschnellwege.chilla.dev`](https://radschnellwege.chilla.dev)