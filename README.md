# ftypeaa — FIA Forest Type to Assessment Area Crosswalk

A Python package that maps FIA (Forest Inventory and Analysis) forest type codes to ARB/CAR assessment areas and common practice values used in California carbon offset protocols.

## What's included

- **Crosswalk table** (`FTAALOOKUP`): 3,124-row lookup mapping FIA forest type codes → assessment area codes, names, supersection codes, and common practice values (high/low site class).
- **Supersections shapefile** (`SSECT`): 95 CAR (Climate Action Reserve) supersection polygons for CONUS.
- **`attributeSS()`**: Spatial join helper that attributes input geometries with their supersection.

## Installation

```bash
pip install git+https://github.com/peteWT/ftype-to-assessment.git
```

Or from a local clone:

```bash
pip install .
```

## Quick start

```python
from ftypeaa import FTAALOOKUP, SSECT, attributeSS

# Look up assessment areas for FIA forest type 261 (Douglas-fir)
FTAALOOKUP[FTAALOOKUP.ftype_code == 261]

# View supersections
SSECT.plot()

# Attribute a GeoDataFrame of stands with supersection info
attributed = attributeSS(my_stands_gdf, dissolve_on="Stand_ID")
```

## Data provenance

The crosswalk was originally developed at [NewForestsUS](https://github.com/NewForestsUS) by Peter Tittmann and Alec Trusty using:

- FIA forest type codes and common names
- ARB species-to-forest-type mappings
- CAR supersection boundaries
- CarbonPlan assessment area and common practice data

Now maintained by Pete Tittmann ([@peteWT](https://github.com/peteWT)).

## License

MIT
