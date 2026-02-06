#Hugo KINGKEOMANIVONG Christ-Ivan PGE1 EN

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Iris Dataset Dashboard")
st.write("This dashboard shows information about the Iris flower dataset.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Question: Why does the app automatically update when you type?
#Because Streamlit reruns the script when any value changes.

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

st.subheader("Dataset Overview")
st.write("First 5 rows")
st.write(df.head())

st.write(f"Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")
st.write("Column names:", list(df.columns))

# Question: Why is displaying the full dataset often a bad idea in a dashboard?
#Because the data can be too large and slow down the dashboard.

st.subheader("Basic Statistics")
st.write("Summary statistics:")
st.write(df.describe())

# Show specific statistic
mean_sepal_length = df['sepal_length'].mean()
st.write(f"Mean sepal length: {mean_sepal_length:.2f}")

st.subheader("Filters")

species_list = df['species'].unique().tolist()
selected_species = st.selectbox("Select a species:", species_list)

filtered_df = df[df['species'] == selected_species]

# Numerical filter
st.write("Numerical filter:")
min_sepal_length = st.slider(
    "Minimum sepal length:", 
    float(df['sepal_length'].min()), 
    float(df['sepal_length'].max()),
    float(df['sepal_length'].min())
)

filtered_df = filtered_df[filtered_df['sepal_length'] >= min_sepal_length]

st.subheader("Filter Summary")
st.write(f"Number of remaining rows: {filtered_df.shape[0]}")
st.write(f"Filters applied: Species = {selected_species}, Min sepal length = {min_sepal_length}")

st.subheader("Visualizations")

# Plots
fig1, ax1 = plt.subplots()
ax1.hist(filtered_df['sepal_length'], bins=20, edgecolor='black')
ax1.set_title('Sepal Length Distribution')
ax1.set_xlabel('Sepal Length')
ax1.set_ylabel('Frequency')
st.pyplot(fig1)

# Scatter plot
fig2, ax2 = plt.subplots()
ax2.scatter(filtered_df['sepal_length'], filtered_df['petal_length'])
ax2.set_title('Sepal Length vs Petal Length')
ax2.set_xlabel('Sepal Length')
ax2.set_ylabel('Petal Length')
st.pyplot(fig2)

plot_type = st.radio("Select plot type:", ['Histogram', 'Scatter Plot'])

if plot_type == 'Histogram':
    st.pyplot(fig1)
elif plot_type == 'Scatter Plot':
    st.pyplot(fig2)

#Move controls to sidebar
st.sidebar.title("Dashboard Controls")

#Species filter in sidebar
selected_species = st.sidebar.selectbox("Select a species:", species_list)

#Numerical filter in sidebar
min_sepal_length = st.sidebar.slider(
    "Minimum sepal length:", 
    float(df['sepal_length'].min()), 
    float(df['sepal_length'].max()),
    float(df['sepal_length'].min())
)

plot_type = st.sidebar.radio("Select plot type:", ['Histogram', 'Scatter Plot'])

filtered_df = df[df['species'] == selected_species]
filtered_df = filtered_df[filtered_df['sepal_length'] >= min_sepal_length]

# Frontend summary
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Overview")
    st.write(f"Total rows: {df.shape[0]}")
    st.write(f"Filtered rows: {filtered_df.shape[0]}")

with col2:
    st.subheader("Active Filters")
    st.write(f"Species: {selected_species}")
    st.write(f"Min sepal length: {min_sepal_length}")

st.subheader("Visualizations")
if plot_type == 'Histogram':
    fig1, ax1 = plt.subplots()
    ax1.hist(filtered_df['sepal_length'], bins=20, edgecolor='black')
    ax1.set_title('Sepal Length Distribution')
    ax1.set_xlabel('Sepal Length')
    ax1.set_ylabel('Frequency')
    st.pyplot(fig1)
elif plot_type == 'Scatter Plot':
    fig2, ax2 = plt.subplots()
    ax2.scatter(filtered_df['sepal_length'], filtered_df['petal_length'])
    ax2.set_title('Sepal Length vs Petal Length')
    ax2.set_xlabel('Sepal Length')
    ax2.set_ylabel('Petal Length')
    st.pyplot(fig2)

# Improve readability, just text trying to make it look nicer and professional
st.subheader("About")
st.write("This dashboard shows the Iris flower dataset.")
st.write("Use the sidebar controls to filter data and select visualizations.")


# 1.Practical to vizualie data, plot, graphs.
# 2.You can zoom, select certain option depending of the plot tool used.
# 3.You have to relauch the app to see the changes, takes time.

#I already have done a streamlit dashboard before, but I have learned way more on this exercise.(Hugo)
#Here the github link of another streamlit project:
#https://github.com/Keogo811/gender_equality
#A dashboard about HR(human ressources) data.