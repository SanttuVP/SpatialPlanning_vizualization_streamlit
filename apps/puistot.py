import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd

def app():

    st.title("Puistoihin liittyvät kaavamääräykset vuodelta 2021")

    st.markdown(
        """
    Väritä, visualisoi ja filtteröi aineistoa kartan vasemmasta yläkulmasta avautuvan työkalupakin avulla.

    """
    )

    m = leafmap.Map(center=[60.174, 24.802], zoom=14.5, height=600, widescreen=False)

    gdf = gpd.read_file("http://pygeoapi-testing.gispocoding.fi/collections/koonti_koko_suomi_kaavakohteet/items?f=json&limit=1000")
    gdf['kaavoitusteema'] = gdf['kaavoitusteema'].astype('str')
    gdf['kaavamaarayslaji'] = gdf['kaavamaarayslaji'].astype('str')
    gdf = gdf[gdf['kaavamaarayslaji'].str.contains('puisto')]
    gdf_map = gdf[["kaavoitusteema", "kaavamaarayslaji", "tekstiarvo", "geometry"]]
    m.add_gdf(gdf_map, layer_name="Pyoratiet")

    m.to_streamlit(height=700)