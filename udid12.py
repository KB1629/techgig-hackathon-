import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv(r"C:\Users\kabi1\Downloads\RS_Session_255_AU_2856_2 (1).csv")
df = df.drop(36)

# Streamlit app
st.title("Animated Streamlit Visualization of Disability Data")

# Select the disabilities for visualization
selected_disabilities = ['Visual - Persons', 'Locomotor - Persons', 'Hearing - Persons']

# Melt the dataframe for animation
df_melted = pd.melt(df, id_vars=['States/UTs'], value_vars=selected_disabilities,
                    var_name='Disability', value_name='Persons')

# Normalize data for animation
df_melted['Persons'] = (df_melted['Persons'] - df_melted['Persons'].min()) / \
                       (df_melted['Persons'].max() - df_melted['Persons'].min())

# Create animated radar chart with lines connecting dots using Plotly Graph Objects
fig = go.Figure()

for state, data in df_melted.groupby('States/UTs'):
    fig.add_trace(go.Scatterpolar(
        r=data['Persons'],
        theta=data['Disability'],
        mode='lines+markers',
        name=state
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(range=[0, 1], showticklabels=False),
        angularaxis=dict(showticklabels=True, tickmode='array', tickvals=list(range(len(selected_disabilities))),
                         ticktext=selected_disabilities)
    ),
    showlegend=True,
    title='Disability Distribution Over Time'
)

# Show the animated radar chart
st.plotly_chart(fig)
st.write("""
###### Initially the radar chart shows the number of disabled in each of the state and double clicking the legend shows the particular state's disabled counts. 
""")

