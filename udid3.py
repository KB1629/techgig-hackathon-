import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df_demographics = pd.read_csv(r"C:\Users\kabi1\Downloads\rs_session-241_as314_1.1 (1).csv")
df_attacks = pd.read_csv(r"C:\Users\kabi1\Downloads\NCRB_CII_2018_State_Table10B.4.csv")
df_moratorium = pd.read_csv(r"C:\Users\kabi1\Downloads\CEPI_Scores_and_Status_of_Moratorium.csv")

# Load data frames
# Assuming you have already created the data frames as df_demographics, df_attacks, and df_moratorium
# If not, you need to load or create them first

# Sidebar for selecting data
selected_data = st.sidebar.radio("Select Data", ["Demographics", "Attacks", "Moratorium"])

if selected_data == "Demographics":
    st.title("Demographic Data")
    st.dataframe(df_demographics)

    # Visualize rural and urban percentages
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="States/Uts", y="Rural - Percentage of Persons", data=df_demographics, color="skyblue", label="Rural")
    sns.barplot(x="States/Uts", y="Urban - Percentage of Persons", data=df_demographics, color="orange", label="Urban")
    plt.xticks(rotation=90)
    plt.title("Rural and Urban Percentages by State")
    plt.legend()
    st.pyplot(fig)



# ... (your existing code)

elif selected_data == "Attacks":
    st.title("Attack Data")
    st.dataframe(df_attacks)

    # Visualize total incidents of attacks by category (animated bar chart)
    df_attacks_plot = df_attacks.melt(id_vars="SL", var_name="Attack Category", value_name="Count")

    fig = px.bar(df_attacks_plot, 
                 x="Count", 
                 y="SL", 
                 color="Attack Category", 
                 orientation="h",
                 animation_frame="Attack Category",
                 labels={"SL": "State/UT", "Count": "Incident Count"},
                 title="Total Incidents of Attacks by Category (Animated)")

    st.plotly_chart(fig)



elif selected_data == "Moratorium":
    st.title("Moratorium Data")
    st.dataframe(df_moratorium)

    # Visualize changes in CEPI SCORE over time for specific locations
    selected_locations = st.multiselect("Select Locations", df_moratorium["Industrial Cluster / Area"].unique())
    if selected_locations:
        fig, ax = plt.subplots(figsize=(10, 6))
        for location in selected_locations:
            df_location = df_moratorium[df_moratorium["Industrial Cluster / Area"] == location]
            plt.plot(df_location["CEPI SCORE-2009"], label=f"{location} - 2009", marker="o")
            plt.plot(df_location["CEPI SCORE-2011"], label=f"{location} - 2011", marker="o")
            plt.plot(df_location["CEPI SCORE-2013"], label=f"{location} - 2013", marker="o")
        plt.xlabel("Years")
        plt.ylabel("CEPI SCORE")
        plt.title("Changes in CEPI SCORE Over Time for Selected Locations")
        plt.legend()
        st.pyplot(fig)
