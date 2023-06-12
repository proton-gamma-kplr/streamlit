import streamlit as st
import numpy as np 
import time

st.title("Mon application Streamlit avec Markdown")
st.subheader("Exemple d'utilisation du Markdown")
st.markdown("Voici un **texte en gras** et un *texte en italique*")

st.markdown(""" Voici une liste numérotée :
1. élément 1
2. élément 2
3. élément 3
""")
st.markdown("> Voici une citation.")
st.markdown("---")

st.markdown("![Alt texte](https://img.freepik.com/photos-premium/adorable-mignon-chat-potele-rendu-3d_784625-1053.jpg)")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

color = st.select_slider(
    'Select a color of the rainbow',
    options=['100', 'orange', 'yellow', 'green', 'blue', 'indigo', '100'])
st.write('My favorite color is', color)

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

options2 = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options2)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

number = st.number_input('Insert a number', min_value =0, max_value =100, step = 10, value=50)
st.write('The current number is ', number)

txt = st.text_area('Text to analyze', 
'''    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', txt)


progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
