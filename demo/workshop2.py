import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

st.title("Data Manipulation and Visualization")

st.subheader("Fichier")
uploaded_file = st.file_uploader("Choose a file")
dataframe = None
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)


if dataframe is not None:
    st.subheader("CSV")
    st.write(dataframe.head())
    column_names = list(dataframe.columns.values)
    
  
    # HISTOGRAMME
    st.subheader("Histogram")
    colhisto1, colhisto2 = st.columns(2)
    binsValue = None
    chartvalue = None
    with colhisto1:
        binsValue = st.slider('Bins', 0, 130, 25)

    with colhisto2:
          selectBoxValue = st.selectbox(
            'Selectionner une colonnes',
            column_names)
    
    fig, ax = plt.subplots()
    ax.hist(dataframe[selectBoxValue].to_list(), bins=binsValue)
    ax.set_xlabel(selectBoxValue)
    ax.set_ylabel('Value')
    ax.set_title('Diagramme de ' + selectBoxValue)
    st.pyplot(fig)

    # CHART
    st.subheader("Chart")
    chartType = st.selectbox(
        'Selectionner votre type de chart',
        ('ligne', 'barre', 'nuage de points'))
    
    optionsLigne = st.multiselect(
                'Selectionner x et y',
                column_names,
                default=['name', 'age'],
                max_selections=2)
            
    fig2, ax2 = plt.subplots()
    
    match chartType:
        case 'ligne':
            ax2.plot(dataframe[optionsLigne[0]].to_list(), dataframe[optionsLigne[1]].to_list())
        case 'barre':
            ax2.bar(dataframe[optionsLigne[0]].to_list(), dataframe[optionsLigne[1]].to_list())
        case 'nuage de points':
            ax2.scatter(dataframe[optionsLigne[0]].to_list(), dataframe[optionsLigne[1]].to_list())

    ax2.set_xlabel(optionsLigne[0])
    ax2.set_ylabel(optionsLigne[1])
    ax2.set_title(optionsLigne[0] + ' vs '+ optionsLigne[1] )
    st.pyplot(fig2)