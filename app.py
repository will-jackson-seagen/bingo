import streamlit as st
import random


options = [
    "Analyst not understanding our business", '"Cautious in our guidance"', '"Stable edges"', 'Native Apps', 
    'Performance improvements decrease revenue', 'Investors day', '[Operator botches analyst name]', '[Audio cuts out]', 
    'Macro headwinds', 'Exec caught on hot mic', 'Consumption model', "Bring the processing to the data", 'Net revenue retention',
    'question about migration off competitors', 'Python', 'More color', '"Unit economics / operational efficiency"', 'Summit',
    '"Congratulations on a great quarter"', '"Macro environment"', '"Like I said earlier,..."', '"Long-term"', 'I told you what I\'m going to tell you',
    'Strategic investment'
]
random.shuffle(options)


def make_css():
    css = ""
    css += "<style>"
    css += "td {font-size: 16pt; text-align: center; width: 20%}"
    css += "td img {width: 100%}"
    css += "thead td {font-weight: bold; font-size: 20pt}"
    css += "</style>"
    return css

def make_bingo(options):
    i = 0
    html = "<table>"
    html += "<thead>"
    html += "<tr>"
    html += "<td>B</td>"
    html += "<td>I</td>"
    html += "<td>N</td>"
    html += "<td>G</td>"
    html += "<td>O</td>"
    html += "</tr>"
    html += "</thead>"
    html += "<tbody>"
    for row in range(5):
        html += "<tr>"
        for col in range(5):
            html += "<td>"
            
            if row ==2 and col == 2:
                html += "<img src='https://www.snowflake.com/wp-content/themes/snowflake/img/favicons/apple-touch-icon.png'/>"
            else:
                # try:
                html += options[i]
                # except:
                #     html += mylist[0]
            
            html += "</td>"
            i += 1

            if i>=len(options):
                i=0
        html += "</tr>"
    html += "</tbody>"
    html += "</table>"
    return html

st.title("Snowflake Bingo!")
st.markdown(make_css(), unsafe_allow_html=True)
st.markdown(make_bingo(options), unsafe_allow_html=True)
st.caption("Refresh the page to get a new card!")