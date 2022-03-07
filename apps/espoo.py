import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd

def app():

    st.title("Kaavoituskohteet")

    st.markdown(
        """
    Väritä ja visualisoi asemakaava-aineistoa kartan vasemmasta yläkulmasta avautuvan työkalupakin avulla.

    """
    )

    m = leafmap.Map(center=[60.174, 24.802], zoom=14.5, height=600, widescreen=False)

    gdf = gpd.read_file("http://localhost:5000/collections/koonti_koko_suomi_kaavakohteet/items?f=json&limit=1000")
    gdf_map = gdf[["kaavoitusteema", "kaavamaarayslaji", "tekstiarvo", "numeerinen_arvo", "mittayksikko", "geometry"]]
    m.add_gdf(gdf_map, layer_name="Espoo")

    m.to_streamlit(height=700)

