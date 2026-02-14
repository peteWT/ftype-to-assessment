"""Tools for mapping FIA forest types to ARB/CAR assessment areas.

This module provides:
- ``FTAALOOKUP``: A DataFrame crosswalk mapping FIA forest type codes to
  assessment areas and common practice values.
- ``SSECT``: A GeoDataFrame of CAR supersection polygons.
- ``attributeSS()``: A function to spatially join supersection attributes
  onto an input GeoDataFrame.
"""

from importlib.resources import files

import geopandas as gpd
import pandas as pd

FTAALOOKUP: pd.DataFrame = pd.read_csv(
    files("ftypeaa.data").joinpath("ftype_to_assessment_crosswalk.csv")
)
"""DataFrame with 3,124 rows mapping FIA forest type codes to assessment areas."""

SSECT: gpd.GeoDataFrame = gpd.read_file(
    files("ftypeaa.data.CAR_supersections").joinpath("CAR_supersections_coded.shp")
)
"""GeoDataFrame with 95 CAR supersection polygons."""


def attributeSS(
    input_layer: gpd.GeoDataFrame,
    dissolve_on: str = "Stand_ID",
) -> gpd.GeoDataFrame:
    """Spatially join CAR supersection attributes onto a GeoDataFrame.

    Reprojects the supersections to match ``input_layer``'s CRS, performs a
    left spatial join, then dissolves on the specified column.

    Args:
        input_layer: A GeoDataFrame of geometries (e.g. forest stands).
        dissolve_on: Column name to dissolve on after the spatial join.

    Returns:
        A GeoDataFrame with supersection columns (``SSection``, ``SS_Name2``,
        ``ss_code``, etc.) joined and dissolved.
    """
    ss_reproj = SSECT.to_crs(input_layer.crs)
    ss_layer = (
        input_layer.sjoin(ss_reproj, how="left")
        .dissolve(by=dissolve_on)
        .reset_index()
    )
    return ss_layer
