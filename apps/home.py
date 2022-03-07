import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd

def app():
    st.title("Koontinäkymiä kaava-aineistoista")

    st.markdown(
        """
    ### Tutustu vasemman sivupalkin toimintojen avulla kaavatiedoista luotuihin karttanäkymiin.

    """
    )


