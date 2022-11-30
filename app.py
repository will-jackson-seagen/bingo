import streamlit as st
import random
import os
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Snowflake Bingo!",
    page_icon="❄️"
)

# Default Bingo options
# Any option starting with http:// or https:// will automatically turn into an image
default_options = [
    "Analyst not understanding our business", '"Cautious in our guidance"', '"Stable edges"', 'Native Apps', 
    'Performance improvements decrease revenue', 'Investors day', '[Operator botches analyst name]', '[Audio cuts out]', 
    'Macro headwinds', 'Exec caught on hot mic', 'Consumption model', "Bring the processing to the data", 'Net revenue retention',
    'Question about migration off competitors', 'Python', 'More color', '"Unit economics / operational efficiency"', 'Summit',
    '"Congrats on a great quarter"', '"Macro environment"', '"Like I said earlier..."', '"Long-term"', 'I told you what I\'m going to tell you',
    'Strategic investment', '"We\'re not SaaS"', 'Unistore', 'https://share.streamlit.io/-/build/favicon.svg',
    '"Yes" or "No" (one word answer)',
    'Sailing reference',
    'Snow Day',
    'Mike: "I\'m not going to tell you that/guide to that"',
    'https://uploads-ssl.webflow.com/6152faba362df06f290c14c5/6177d926bba58f6ff9032531_logo%20black.svg',
    'Analyst suggests we move to SaaS / subscription model',
    'Audio issues from an analyst',
    'Analyst names a competitor (bonus points for Databricks)',
    'Snide comments about GCP',
    'Redirects question to Christian',
    'References to tech downturn / layoffs',
    'Stream buffers'
]

# Component Dev Mode
# Set this to True when running "npm run start"
# Set this to False after running "npm run build"
COMPONENT_DEV_MODE = False

if(COMPONENT_DEV_MODE):
    bingo_component = components.declare_component("bingo_component", url='http://localhost:3001')
else:
    parent_dir = (os.path.dirname(os.path.abspath(__file__)))
    build_dir = os.path.join(parent_dir, "frontend/build")

    bingo_component = components.declare_component("bingo_component", path=build_dir)

st.title("Snowflake Bingo!")

center_piece = 'https://www.snowflake.com/wp-content/themes/snowflake/img/favicons/apple-touch-icon.png'
options = '\n'.join(default_options)
win_animation = 'Snowflakes'

with st.expander("Settings"):
    with st.form(key="settings"):
        center_piece = st.text_input('Center Piece', value='https://www.snowflake.com/wp-content/themes/snowflake/img/favicons/apple-touch-icon.png')
        bingo_options = st.text_area("Bingo Options", '\n'.join(default_options), help="One line per bingo piece")

        # Selector to choose which Bingo Animation to use
        win_animation = st.selectbox("Bingo Animation", [
            'Balloons',
            'Snowflakes'
        ], index=1)

        st.form_submit_button("Apply")

bingo_options = bingo_options.splitlines()

# Use a session to store a seed for shuffling the options
if 'seed' not in st.session_state:
    st.session_state['seed'] = random.randint(0,1000)

# Use the seed to always shuffle the same way
random.Random(st.session_state['seed']).shuffle(bingo_options)

# Use key to prevent component from redrawing
is_bingo = bingo_component(center_piece=center_piece, bingo_options=bingo_options, key="bingo_time")

st.caption("Refresh the page to get a new card!")
st.caption(f"Streamilt v:{st.__version__}")

if(is_bingo == True):
    if(win_animation=="Balloons"):
        st.balloons()
    else:
        st.snow()