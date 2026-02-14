"""Basic tests for the ftypeaa package."""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point


def test_ftaalookup_loads():
    from ftypeaa import FTAALOOKUP

    assert isinstance(FTAALOOKUP, pd.DataFrame)
    assert len(FTAALOOKUP) > 3000
    assert "ftype_code" in FTAALOOKUP.columns
    assert "aa_code" in FTAALOOKUP.columns
    assert "ss_code" in FTAALOOKUP.columns


def test_ssect_loads():
    from ftypeaa import SSECT

    assert isinstance(SSECT, gpd.GeoDataFrame)
    assert len(SSECT) == 95
    assert SSECT.crs is not None


def test_attribute_ss():
    from ftypeaa import attributeSS

    # A point in the Sierra Nevada, California
    gdf = gpd.GeoDataFrame(
        {"Stand_ID": ["test1"], "val": [1]},
        geometry=[Point(-120.5, 38.5)],
        crs="EPSG:4326",
    )
    result = attributeSS(gdf, dissolve_on="Stand_ID")
    assert "SSection" in result.columns
    assert len(result) == 1
    # Should have gotten a supersection name
    assert pd.notna(result.iloc[0]["SSection"])
