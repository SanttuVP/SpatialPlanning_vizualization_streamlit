import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd

def app():

    st.title("Kaavoituskohteet")

    st.markdown(
    """
    Väritä, visualisoi ja filtteröi asemakaava-aineistoa kartan vasemmasta yläkulmasta avautuvan työkalupakin avulla.

    """
    )

    m = leafmap.Map(center=[61.2954196,23.9996492], zoom=14.5, height=600, widescreen=False)

    gdf = gpd.read_file("http://pygeoapi-testing.gispocoding.fi/collections/koonti_koko_suomi_kaavakohteet/items?f=json&limit=1000")
    gdf_map = gdf[["kaavoitusteema", "kaavamaarayslaji", "tekstiarvo", "numeerinen_arvo", "mittayksikko", "geometry"]]
    m.add_gdf(gdf_map, layer_name="Valkeakoski")

    m.to_streamlit(height=700)

