import pandas as pd
import plotly.express as px


df = pd.read_csv('score_analysis_2.csv')

# Sort the DataFrame by the 'Score' column in descending order
df.sort_values(by='Score', ascending=False, inplace=True)

# Select the top 10 scores
top_10_scores_df = df.head(10)

# Reset the index of the resulting DataFrame
top_10_scores_df.reset_index(drop=True, inplace=True)

# Display the resulting DataFrame with the top 10 scores
# Sort total
# Sort the DataFrame by the 'Score' column in descending order
sorted_df = df.sort_values(by='Score', ascending=False)

# Sort by theme

# Filter rows where the 'Theme' column is 'Career Exploration'
career_exploration_df = df[df['Theme'] == 'Career Exploration']

# Sort the filtered DataFrame by the 'Score' column in descending order
sorted_career_exploration_df = career_exploration_df.sort_values(by='Score', ascending=False)

# Reset the index of the resulting DataFrame
sorted_career_exploration_df.reset_index(drop=True, inplace=True)

# Filter rows where the 'Theme' column is 'Activating Employer Partnerships'
employer_partner_df = df[df['Theme'] == 'Activating Employer Partnerships']

# Sort the filtered DataFrame by the 'Score' column in descending order
sorted_employer_partner_df = employer_partner_df.sort_values(by='Score', ascending=False)

# Reset the index of the resulting DataFrame
sorted_employer_partner_df.reset_index(drop=True, inplace=True)


import streamlit as st
# Configuration
st.image("images.jpg", use_column_width=True)  # Replace with the path to your logo image
st.title("Catalyze Round 3 Scoring Portfolio Balance")

st.set_page_config(page_title="Catalyze Dashboard")



#tabs
tab1, tab2 = st.tabs(["Balance by scores", "Balance by Theme"])

with tab2:
    st.subheader("Balance by Theme Distribution")
    slider_value = st.slider("Select a value to select minimum percentage of each theme", 0.1, 0.5)
    n = int(slider_value * 10)
    # Select Career Exploration
    selected_career_exploration = sorted_career_exploration_df.head(n)
    
    #selected_career_exploration
    # Select Employer Partnerships
    selected_employer_partners = sorted_employer_partner_df.head(n)
    #selected_employer_partners

    # Calculate the remaining number of rows
    remaining_n = 10 - 2 * n

    # Select the next highest scoring solutions from sorted_df
    remaining_solutions = sorted_df.iloc[:remaining_n]

    # Concatenate the selected subsets to form the final DataFrame
    selected_total = pd.concat([selected_career_exploration, selected_employer_partners, remaining_solutions])

    # Reset the index of the resulting DataFrame
    selected_total.reset_index(drop=True, inplace=True)

    # Display the resulting DataFrame
    selected_data = selected_total

    ## Theme 
    theme_counts = selected_data['Theme'].value_counts()

    # Create a bar chart of the 'Theme'
    # Group the data by 'Stage' and count the occurrences
    theme_counts = selected_data['Theme'].value_counts().reset_index()
    theme_counts.columns = ['Theme', 'Count']

    # Create a pie chart on Theme
    fig = px.pie(theme_counts, names='Theme', values='Count', title='Theme Distribution')
    st.plotly_chart(fig,theme="streamlit")
    
    
    ## Stage 
    stage_counts = selected_data['Stage'].value_counts()

    # Create a bar chart of the 'Stage'
    # Group the data by 'Stage' and count the occurrences
    stage_counts = selected_data['Stage'].value_counts().reset_index()
    stage_counts.columns = ['Stage', 'Count']

    # Create a bar chart on Stage
    fig = px.bar(stage_counts, x='Stage', y='Count', color='Stage', title='Stage Distribution')
    fig.update_layout(xaxis_title='Stage', yaxis_title='Count')
    st.plotly_chart(fig,theme="streamlit")
 

    ## Region 
    region_counts = selected_data['Region'].value_counts()
    # Group the data by 'Region' and count the occurrences
    region_counts = selected_data['Region'].value_counts().reset_index()
    region_counts.columns = ['Region', 'Count']

    # Create a bar chart on Region
    fig = px.bar(region_counts, x='Region', y='Count', color='Region', title='Region Distribution')
    fig.update_layout(xaxis_title='Region', yaxis_title='Count')
    st.plotly_chart(fig,theme="streamlit")


    st.write(selected_total)

with tab1:
    st.subheader("Balance by Top Scores")
    number = st.number_input('Insert a number', step=1)

    selected_top_solutions = sorted_df.head(number)

        ## Theme 
    theme_counts_top = selected_top_solutions['Theme'].value_counts()

    # Create a bar chart of the 'Theme'
    # Group the data by 'Stage' and count the occurrences
    theme_counts_top = selected_top_solutions['Theme'].value_counts().reset_index()
    theme_counts_top.columns = ['Theme', 'Count']

    # Create a pie chart on Theme
    fig = px.pie(theme_counts_top, names='Theme', values='Count', title='Theme Distribution')
    st.plotly_chart(fig,theme="streamlit")
    
    
    ## Stage 
    stage_counts_top = selected_top_solutions['Stage'].value_counts()

    # Create a bar chart of the 'Stage'
    # Group the data by 'Stage' and count the occurrences
    stage_counts_top = selected_top_solutions['Stage'].value_counts().reset_index()
    stage_counts_top.columns = ['Stage', 'Count']

    # Create a bar chart on Stage
    fig = px.bar(stage_counts_top, x='Stage', y='Count', color='Stage', title='Stage Distribution')
    fig.update_layout(xaxis_title='Stage', yaxis_title='Count')
    st.plotly_chart(fig,theme="streamlit")
 

    ## Region 
    region_counts_top = selected_top_solutions['Region'].value_counts()
    # Group the data by 'Region' and count the occurrences
    region_counts_top = selected_top_solutions['Region'].value_counts().reset_index()
    region_counts_top.columns = ['Region', 'Count']

    # Create a bar chart on Region
    fig = px.bar(region_counts_top, x='Region', y='Count', color='Region', title='Region Distribution')
    fig.update_layout(xaxis_title='Region', yaxis_title='Count')
    st.plotly_chart(fig,theme="streamlit")
    
    st.write(selected_top_solutions)

