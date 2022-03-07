import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, vector, espoo, valkeakoski, pyoratiet # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = {
    "home": {"title": "Palaa etusivulle", "icon": "house"},
    "vector": {"title": "Vector", "icon": "bounding-box"},    
    "espoo": {"title": "Espoo", "icon": "building"},
    "valkeakoski": {"title": "Valkeakoski", "icon": "house-fill"},
    "pyoratiet": {"title": "Kaavoitetut pyörätiet", "icon": "bicycle"}
}

titles = [app["title"] for app in apps.values()]
icons = [app["icon"] for app in apps.values()]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Etusivu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("Sivustosta")
    st.sidebar.info(
        """
        Tämä demosivusto pohjautuu [Qiusheng Wu](https://wetlands.io) Streamlit-pohjaan. 
        
        Alkuperäisen pohjan koodi: <https://github.com/giswqs/streamlit-template>

        Ikonit: <https://icons.getbootstrap.com>
    """
    )

for app in apps:
    if apps[app]["title"] == selected:
        eval(f"{app}.app()")
        break
