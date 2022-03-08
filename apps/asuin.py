import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd

def app():

    st.title("Asumiseen liittyvät kaavamääräykset")

    st.markdown(
        """
    Väritä, visualisoi ja filtteröi aineistoa kartan vasemmasta yläkulmasta avautuvan työkalupakin avulla.

    """
    )

    m = leafmap.Map(center=[60.174, 24.802], zoom=15.5, height=600, widescreen=False)

    gdf = gpd.read_file("http://pygeoapi-testing.gispocoding.fi/collections/koonti_koko_suomi_kaavakohteet/items?f=json&limit=1000")
    gdf['kaavoitusteema'] = gdf['kaavoitusteema'].astype('str')
    gdf['kaavamaarayslaji'] = gdf['kaavamaarayslaji'].astype('str')
    gdf = gdf[gdf['kaavamaarayslaji'].str.contains('asuin', case=False, na=False)]
    gdf_map = gdf[["kaavoitusteema", "kaavamaarayslaji", "tekstiarvo", "geometry"]]
    m.add_gdf(gdf_map, layer_name="Asuminen")

    m.to_streamlit(height=700)
    
    st.markdown(
        """
        ## Asuinkohteiden jakautuminen kaavamaaräyslajeihin
        """
    )
    df = gdf[["id_kaava","kaavoitusteema", "kaavamaarayslaji"]]
    st.dataframe(df['kaavamaarayslaji'].value_counts().rename_axis('Kaavamääräyslaji').reset_index(name='Määrä'), width=400)