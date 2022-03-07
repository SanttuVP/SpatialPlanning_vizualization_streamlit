import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Vector data")
    m = leafmap.Map(center=[64, 24], zoom=7)

    in_geojson = 'http://localhost:5000/collections/koonti_koko_suomi_kaavakohteet/items?f=json'
    m.add_geojson(in_geojson, layer_name="Cable lines")

    m.to_streamlit(height=700)