import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Jirjir Health Centre", layout="wide")

# XOGTA
over5 = pd.DataFrame({
    'Disease': ['Pneumonia', 'Unknown Fever', 'UTI', 'Skin Disease', 'Cough', 'Trauma/Injury', 'Acute Watery Diarrhoea'],
    'Male': [13, 7, 5, 6, 7, 3, 1],
    'Female': [9, 9, 10, 8, 4, 2, 2],
    'Total': [22, 16, 15, 14, 11, 5, 3]
})
over5['Age'] = 'Over 5'

under5 = pd.DataFrame({
    'Disease': ['Pneumonia', 'Acute Watery Diarrhoea', 'Cough', 'Dysentery', 'Unknown Fever', 'Skin Disease'],
    'Male': [15, 9, 8, 3, 5, 4],
    'Female': [12, 8, 9, 5, 3, 3],
    'Total': [27, 17, 17, 8, 8, 7]
})
under5['Age'] = 'Under 5'

df = pd.concat([over5, under5], ignore_index=True)

# DASHBOARD
st.title("🏥 Jirjir Health Centre")
st.markdown("### OPD Analytics - August 2026")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total OPD", "470")
c2.metric("Male", "228")
c3.metric("Female", "242")
c4.metric("Under 5", "240")

fig1 = px.bar(df, x='Disease', y='Total', color='Age', barmode='group', title='Disease by Age Group')
fig1.update_layout(xaxis=dict(tickangle=-45))
st.plotly_chart(fig1, use_container_width=True)

gender_df = df.melt(id_vars=['Disease', 'Age'], value_vars=['Male', 'Female'], var_name='Gender', value_name='Count')
fig2 = px.bar(gender_df, x='Disease', y='Count', color='Gender', facet_col='Age', title='Gender Analysis')
fig2.update_layout(xaxis=dict(tickangle=-45), xaxis2=dict(tickangle=-45))
st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df, use_container_width=True, hide_index=True)
st.caption("Data: Jirjir Health Centre OPD Register")
