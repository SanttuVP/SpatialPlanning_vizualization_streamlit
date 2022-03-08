import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd

def app():

    st.title("Kaavoitetut rakennukset tyypeittäin")

    st.markdown(
        """
    Väritä, visualisoi ja filtteröi aineistoa kartan vasemmasta yläkulmasta avautuvan työkalupakin avulla.

    """
    )

    m = leafmap.Map(center=[60.174, 24.802], zoom=15.5, height=600, widescreen=False)

    gdf = gpd.read_file("http://pygeoapi-testing.gispocoding.fi/collections/koonti_koko_suomi_kaavakohteet/items?f=json&limit=1000")
    gdf['kaavoitusteema'] = gdf['kaavoitusteema'].astype('str')
    gdf['kaavamaarayslaji'] = gdf['kaavamaarayslaji'].astype('str')
    df = gdf[gdf["kaavamaarayslaji"].str.contains("rakennus")]
    df = df[['id_kaava','kaavoitusteema','kaavamaarayslaji', 'numeerinen_arvo']]
    df.groupby('id_kaava')['kaavamaarayslaji'].value_counts()

    m.to_streamlit(height=700)
    
    st.markdown(
        """
        ## Yhteenlaskettu kerrosala kaavakohtaisesti
        """
    )
    df = gdf[["id_kaava","kaavoitusteema", "kaavamaarayslaji", "numeerinen_arvo"]]
    
    st.dataframe(df.groupby('id_kaava')['numeerinen_arvo'].sum().rename_axis('Kaava-id').reset_index(name='Määrä'), width=400)