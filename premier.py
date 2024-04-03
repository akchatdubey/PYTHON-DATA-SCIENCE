# streamlit run premier.py
import streamlit as st
import pandas as pd 
import plotly.express as px 

st.set_page_config(layout= 'wide',
                   page_title='Premier League Dashboard',
                   page_icon=":soccer:")

@st.cache_data
def load():
    return pd.read_csv('premierleague.csv')

df=load()
st.image('wallpaper.jpg',use_column_width=True)
st.title("Premier League Dashboard")
with st.expander("view raw premiere league data"):
    st.dataframe(df.sample(1000))
    
rows,cols =df.shape
c1,c2 =st.columns(2)
c1.markdown(f'### total Records: {rows}')
c2.markdown(f'###total columns :{cols} ')
numeric_df =df.select_dtypes(include='number')
cat_df=df.select_dtypes(exclude='number')
with st.expander("Column names"):
    st.markdown(f'Column with numbers:{", ".join(numeric_df)}')
    st.markdown(f'Columns without numbers:{", ".join(cat_df)}')
    
#visualization 
c1, c2=st.columns([1,3])
xcol=c1.selectbox("choose a column for x-axis",numeric_df.columns)
ycol=c1.selectbox("choose a column for y-axis",numeric_df.columns)
zcol=c1.selectbox("choose a column for z-axis",numeric_df.columns)
color=c1.selectbox('choose column for color',cat_df.columns)
fig=px.scatter_3d(df,x=xcol,y=ycol,z=zcol,color=color)
c2.plotly_chart(fig,use_container_width=True)

st.title("More analysis")
c1,c2=st.columns(2)
c1.video("https://www.youtube.com/watch?v=cKeL28dPzIw")
c2.markdown('''
            Security:

''')

st.title("Premiere League Club")
clubs=df['HomeTeam'].unique() + df['AwayTeam'].unique()
clubs=sorted(set(clubs))
st.info(",".join(clubs))




    

