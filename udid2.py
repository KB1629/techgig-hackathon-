import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Read the CSV file
df = pd.read_csv(r"C:\Users\kabi1\Downloads\RS_Session_254_AU_878_1.csv")

# Extract categories
categories = ['1st Dose - HCWs', '1st Dose - FLWs', '1st Dose - 45+ years', '1st Dose - 18-44 years']

# Create a sidebar for smaller bar plots
st.sidebar.title("First 5 Categories")
for i, category in enumerate(categories[:5]):
    fig, ax = plt.subplots(figsize=(8, 4))
    df.plot(kind='bar', x='State/UT', y=category, legend=False, ax=ax)
    ax.set_title(f'First Dose Vaccinations - {category}')
    ax.set_xlabel('State/UT')
    ax.set_ylabel('Number of Vaccinations')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    
    # Save the figure to a BytesIO object
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    
    # Display the image in the sidebar
    st.sidebar.image(img_buffer, caption=category, use_column_width=True)

# Main section for the remaining charts
st.title("Vaccination Data Analysis")

# Animated pie chart for the overall distribution
total_vaccinations = df[['1st Dose - HCWs', '1st Dose - FLWs', '1st Dose - 45+ years', '1st Dose - 18-44 years']].sum()
labels = total_vaccinations.index
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(total_vaccinations, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff6666'])
ax.set_title('Overall Distribution of First Dose Vaccinations')

# Save the figure to a BytesIO object
overall_pie_buffer = io.BytesIO()
plt.savefig(overall_pie_buffer, format='png')

# Display the image in the main section
st.image(overall_pie_buffer, use_column_width=True)
st.write("""
##### We could infer from the pie-chart that people over the age of 45 have been vaccinated the most  over the segments.
""")

# Line chart for the trend of total first dose vaccinations across states/UTs
df['Total 1st Dose Vaccinations'] = df.iloc[:, 1:].sum(axis=1, numeric_only=True)
fig, ax = plt.subplots(figsize=(15, 8))
ax.plot(df['State/UT'], df['Total 1st Dose Vaccinations'], marker='o', linestyle='-', color='b')
ax.set_title('Trend of Total First Dose Vaccinations Across States/UTs')
ax.set_xlabel('State/UT')
ax.set_ylabel('Total 1st Dose Vaccinations')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.grid(True)

# Save the figure to a BytesIO object
trend_line_buffer = io.BytesIO()
plt.savefig(trend_line_buffer, format='png')

# Display the image in the main section
st.image(trend_line_buffer, use_column_width=True)
st.write("""
##### From the line-chart we could see  that Uttar Pradhesh is the highly vaccinated state. Hence it requires the less attention than the other states for preventive measures. 
""")