import pandas as pd
import plotly.express as px
import streamlit as st
# import warnings
# warnings.filterwarnings("ignore")

st.sidebar.header('User Input Parameters')

filename = st.sidebar.selectbox(label='filename:', options=['RTopConvictions20200626.csv', 'STOXX50_20200831.csv', 'S&P100_20200831.csv'], index=0)
axex = st.sidebar.selectbox(label='X Axe:', options=['Prob_Put', 'Vida_Media'], index=0)
axey = st.sidebar.selectbox(label='Y Axe:', options=['Cupon', 'Rentabilidad'], index=0)
myby = st.sidebar.selectbox(label='By:', options=['Trigger - Strike', 'Bloque'], index=0)
showtop = st.sidebar.checkbox('Show only top baskets')
mysize = st.sidebar.slider('Select size:', 500, 1100, 700, step=50)
myheight = int(mysize)
mywidth = int(mysize)*1.6180

def process(df):
    df['Trigger - Strike'] = 'Trigger ' + df['Trigger'].astype(str) + ' - Strike ' + df['Strike'].astype(str)
    df['Bloque'] = df['Bloque'].astype(str)
    lista = ['Cupon', 'Rentabilidad', 'ProbNeut_Put', 'Prob_Put', 'NPVNeut_Put', 'NPV_Put', 'VaR95', 'ES95', 'Vida_Media', 'rhoCesta', 'volatCesta']
    for k in lista:
        df[k] = df[k].round(4)
    return df

if filename == 'RTopConvictions20200626.csv' and not showtop:
    df = pd.read_csv(filename)
    df = process(df)
    st.title("Reverse Convertible Notes")
    st.write(filename)
    fig = px.scatter(df, x=axex, y=axey, color=myby, width=mywidth, height=myheight, # size='Vida_Media',
                     hover_name='Composicion_1', hover_data=['Rentabilidad','Vida_Media', 'rhoCesta', 'volatCesta'])
    fig.update_traces(marker=dict(size=8, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))
    fig.update_layout(font=dict(family='Arial', size=18, color='#494747'))
    st.write(fig.update_layout(width = mywidth, height = myheight))

elif filename == 'RTopConvictions20200626.csv' and showtop:
    df = pd.read_csv(filename)
    df = process(df)
    dfx = df.copy()
    kk = pd.DataFrame()
    nselect = 10
    for ix in range(1,21):
        aux = dfx[(dfx[axex] > (ix/20-0.05)) & (dfx[axex] <= ix/20)].sort_values(by='Rentabilidad', ascending=False)
        kk = pd.concat([kk, aux.head(nselect)])
    kk.reset_index(drop=True, inplace=True)
    st.title("Reverse Convertible Notes. Top Baskets")
    st.write(filename)
    fig = px.scatter(kk, x=axex, y=axey, color=myby, width=mywidth, height=myheight, # size='Vida_Media',
                     hover_name='Composicion_1', hover_data=['Rentabilidad','Vida_Media', 'rhoCesta', 'volatCesta'])
    fig.update_traces(marker=dict(size=8, line=dict(width=1, color='DarkSlateGrey')), selector=dict(mode='markers'))
    fig.update_layout(font=dict(family='Arial', size=18, color='#494747'))
    st.write(fig.update_layout(width = mywidth, height = myheight))
    
else:
    st.markdown("Coming soon...")
    

    
    
    
    
    
    
    
    
    
    
    
    
# https://docs.streamlit.io/en/stable/api.html
# https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace
# https://discuss.streamlit.io/t/where-to-set-page-width-when-set-into-non-widescreeen-mode/959
# http://awesome-streamlit.org/
# https://towardsdatascience.com/from-streamlit-to-heroku-62a655b7319
