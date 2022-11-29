import streamlit as st
import random

options = [
    "Analyst not understanding our business", '"Cautious in our guidance"', '"Stable edges"', 'Native Apps', 
    'Performance improvements decrease revenue', 'Investors day', '[Operator botches analyst name]', '[Audio cuts out]', 
    'Macro headwinds', 'Exec caught on hot mic', 'Consumption model', "Bring the processing to the data", 'Net revenue retention',
    'question about migration off competitors', 'Python', 'More color', '"Unit economics / operational efficiency"', 'Summit',
    '"Congratulations on a great quarter"', '"Macro environment"', '"Like I said earlier,..."', '"Long-term"', 'I told you what I\'m going to tell you',
    'Strategic investment', '"We\'re not SaaS"', 'Unistore', '<img src="https://share.streamlit.io/-/build/favicon.svg"/>'
]
random.shuffle(options)


def make_css():
    css = """
    <style>
    td {font-size: 16pt; text-align: center; width: 20%; padding:0 !important}
    td img {width: 90%}
    thead td {font-weight: bold; font-size: 20pt}
    tbody td:click {background-color:'#f00'}
    .btnControl { display: none; }
    label{width: 100%; height: 100%; display:block;pointer:cursor}
    .btnControl:checked + label  {background-color: #29B5E8}
    </style>
    """
    return css

def make_bingo(options):
    i = 0
    incr = 0
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
            html += f"""<td><input type="checkbox" class="btnControl" id="btnControl{incr}"/><label class="btn" for="btnControl{incr}">"""
            
            if row ==2 and col == 2:
                html += "<img src='https://www.snowflake.com/wp-content/themes/snowflake/img/favicons/apple-touch-icon.png'/>"
            else:
                # try:
                html += options[i]
                # except:
                #     html += mylist[0]
            
            html += "</label></td>"
            i += 1
            incr+=1

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