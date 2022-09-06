# -*- coding: utf-8 -*-
"""Space_Missions_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jELvNC6uyoUKn2f2H9Fv4Tfvyl8hbCAV

# Introduction

<center><img src="https://i.imgur.com/9hLRsjZ.jpg" height=400></center>

This dataset was scraped from [nextspaceflight.com](https://nextspaceflight.com/launches/past/?page=1) and includes all the space missions since the beginning of Space Race between the USA and the Soviet Union in 1957!

### Install Package with Country Codes
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install iso3166

"""### Upgrade Plotly

Run the cell below if you are working with Google Colab.
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install --upgrade plotly

# Commented out IPython magic to ensure Python compatibility.
# %pip install pycountry

"""### Import Statements"""

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# These might be helpful:
from iso3166 import countries
from datetime import datetime, timedelta
import pycountry

"""### Notebook Presentation"""

pd.options.display.float_format = '{:,.2f}'.format

"""### Load the Data"""

df_data = pd.read_csv('mission_launches.csv')

"""# Preliminary Data Exploration

* What is the shape of `df_data`? 
* How many rows and columns does it have?
* What are the column names?
* Are there any NaN values or duplicates?
"""

df_data.shape  # (rows, columns)

df_data.columns

"""## Data Cleaning - Check for Missing Values and Duplicates

Consider removing columns containing junk data. 
"""

df_data.isna().values.any()

# remove N/A values

df_data.dropna(inplace=True)
df_data.isna().values.any()  # check if cleared

df_data.duplicated().values.any()  # no duplicates so we can move on

"""## Descriptive Statistics"""

df_data.head()

df_data.info

df_data.describe()

"""We see this unnamed column here, and we see that it's value is equivalent to the index value, so let's get rid of both."""

# If using the old csv file, uncomment the first 2 lines and comment the 3rd and 4th ones

# df_data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)  # we removed them already so rerunning this code will cause an error if you don't reload the df
# df_data

df_data.drop(['Unnamed: 0'], axis=1, inplace=True)
df_data

"""# Number of Launches per Company

Create a chart that shows the number of space mission launches by organisation.
"""

df_data.Organisation.value_counts()

df_data.Organisation.unique()

plt.figure(figsize=(12,8), dpi=150)

plt.pie(df_data.Organisation.value_counts(),
        labels = df_data.Organisation.unique(),  # get the cols
        labeldistance = None,  # remove labels because they are too cluttereds
)

plt.legend(loc='best')  # moves the legend to the best place

plt.axis('equal')  # makes sure pie chart is drawn as a circle

plt.show()

"""# Number of Active versus Retired Rockets

How many rockets are active compared to those that are decomissioned? 
"""

# if using old csv, change to 'StatusActive' instead of 'Active'

active_rockets = df_data[df_data.Rocket_Status == 'Active'].count()[0]
decom_rockets = df_data[df_data.Rocket_Status != 'Active'].count()[0]  # specify 0 because otherwise it returns the count for every column

print(f"There are {active_rockets} active rockets and {decom_rockets} decommissioned rockets.\nThe percentage of active rockets is {active_rockets*100/(active_rockets+decom_rockets):.4}% and the percentage of"
      +f" decommissioned rockets is {decom_rockets*100/(active_rockets+decom_rockets):.4}%.")

"""# Distribution of Mission Status

How many missions were successful?
How many missions failed?
"""

successes = df_data[df_data.Mission_Status == 'Success'].count()[0]
failures = df_data[df_data.Mission_Status != 'Success'].count()[0]  # specify 0 because otherwise it returns the count for every column

print(f"There are {successes} mission successes and {failures} mission failures.")  # omit percentages because there are partial failures

"""# How Expensive are the Launches? 

Create a histogram and visualise the distribution. The price column is given in USD millions (careful of missing values). 
"""

df_data.Price = df_data.Price.replace(',','', regex=True)  # remove the commas
df_data = df_data.astype({'Price':'float'})  # cast price into float values so we can plot it easier

df_data.Price.describe()

plt.figure(figsize=(12,8), dpi=150)

plt.hist(
    x = df_data.Price,
    bins=20,
    # range=[5,1200]  #uncomment this if using old csv
    rwidth=0.9,
)

plt.xlabel('Launch Price in USD Million $')
plt.ylabel('Count')
plt.title('Distribution of Launch Prices')

plt.xticks(np.arange(0, 450, step=25), np.arange(0, 470, step=25))
# plt.xticks(np.arange(0, 1200, step=50), np.arange(0, 1200, step=50)) uncomment if using old csv

plt.show()

"""# Use a Choropleth Map to Show the Number of Launches by Country

* Create a choropleth map using [the plotly documentation](https://plotly.com/python/choropleth-maps/)
* Experiment with [plotly's available colours](https://plotly.com/python/builtin-colorscales/). I quite like the sequential colour `matter` on this map. 
* You'll need to extract a `country` feature as well as change the country names that no longer exist.

Wrangle the Country Names

You'll need to use a 3 letter country code for each country. You might have to change some country names.

* Russia is the Russian Federation
* New Mexico should be USA
* Yellow Sea refers to China
* Shahrud Missile Test Site should be Iran
* Pacific Missile Range Facility should be USA
* Barents Sea should be Russian Federation
* Gran Canaria should be USA


You can use the iso3166 package to convert the country names to Alpha3 format.
"""

# create a new column with only the country name because we only have location data for our dataframe

df_data['Country'] = df_data.Location.str.split(', ').str[-1]

# change the countries that no longer exist so we can get the 3 letter codes

df_data.Country = df_data.Country.str.replace('Gran Canaria', 'USA')
df_data.Country = df_data.Country.str.replace('Yellow Sea', 'China')
df_data.Country = df_data.Country.str.replace('Russia', 'Russian Federation')
df_data.Country = df_data.Country.str.replace('Pacific Missile Range Facility', 'Iran')
df_data.Country = df_data.Country.str.replace('Barents Sea', 'Russian Federation')
df_data.Country = df_data.Country.str.replace('Shahrud Missile Test Site', 'Iran')
df_data.Country = df_data.Country.str.replace('New Mexico', 'USA')

country_codes = []

for country in df_data.Country:
  try:
    country_codes.append(pycountry.countries.get(name=country).alpha_3)
  except AttributeError:
    country_codes.append(country)  # alpha 3 code for USA is USA, trying to get it using the above line of code will give an error as it returns None

df_data['Country_Codes'] = country_codes  # create a new col with alpha 3 codes so we can easily create chloropleths from now on 
country_code_vs_launches =  df_data.Country_Codes.value_counts()  # create a new df which includes country codes and number of launches (which is number of rows for each country)

country_code_vs_launches

fig = px.choropleth(
    country_code_vs_launches,  # base dataframe
    locations=country_code_vs_launches.index,  # ISO codes
    locationmode='ISO-3',
    color=country_code_vs_launches,  # specify to color each country by the number of launches
    color_continuous_scale=px.colors.sequential.matter,  # color scale
    title='Launches Per Country',
    labels={'color':'Launches'},  # change colors to launches
)

fig.show()

"""# Use a Choropleth Map to Show the Number of Failures by Country

"""

country_total_fails = df_data.Country_Codes[df_data.Mission_Status == 'Failure'].value_counts()

fig2 = px.choropleth(
    country_total_fails,  # base dataframe
    locations=country_total_fails.index,  # ISO codes
    locationmode='ISO-3',
    color=country_total_fails,  # specify to color each country by the number of launches
    color_continuous_scale=px.colors.sequential.matter,  # color scale
    title='Launches Per Country',
    labels={'color':'Failed Launches'},  # change colors to launches
)

fig2.show()

"""# Create a Plotly Sunburst Chart of the countries, organisations, and mission status. """

fig3 = px.sunburst(
    df_data,
    path=['Country', 'Organisation', 'Mission_Status']
)

fig3.show()

"""# Analyse the Total Amount of Money Spent by Organisation on Space Missions"""

total_spent_per_org = df_data.groupby('Organisation').agg({'Price':pd.Series.sum})
total_spent_per_org.rename(columns={'Price':'Total_Spent'}, inplace=True)

total_spent_per_org

"""# Analyse the Amount of Money Spent by Organisation per Launch"""

launches_per_org = df_data.groupby('Organisation').agg({'Organisation':pd.Series.count})
launches_per_org.rename(columns={'Organisation':'Launches'}, inplace=True)

total_spent_per_org['Avg_Per_Launch'] = total_spent_per_org['Total_Spent']/launches_per_org.Launches

total_spent_per_org

"""# Chart the Number of Launches per Year"""

# split once by comma to get 2nd half of string, then split again by space and take the first string
# since to_datetime() is now working for this data

yearly_launches = df_data.Date.str.split(', ').str[1].str.split(' ').str[0]
yearly_launches = yearly_launches.value_counts(sort=False)

plt.figure(figsize=(20, 10), dpi=200)

plt.plot(yearly_launches.index, yearly_launches)

plt.xticks(ticks=yearly_launches.index, rotation=45)

plt.title('Launches Per Year')

plt.show()

"""# Launches per Month: Which months are most popular and least popular for launches?

Some months have better weather than others. Which time of year seems to be best for space missions?
"""

monthly_launches = df_data.Date.str.split(' ').str[1]
monthly_launches = monthly_launches.value_counts()

monthly_launches  # december is the most popular month, but not by alot, there doesn't seem to be a trend

"""# How has the Launch Price varied Over Time? 

Create a line chart that shows the average price of rocket launches over time. 
"""

# let's get the average price of rocket launches per year
df_data['Year'] = df_data.Date.str.split(', ').str[1].str.split(' ').str[0]

avg_price_per_year = df_data.groupby('Year').agg({'Price':pd.Series.mean})

plt.figure(figsize=(13, 7), dpi=100)

plt.plot(avg_price_per_year.index, avg_price_per_year.Price)

plt.xticks(ticks=avg_price_per_year.index, rotation=45)

plt.title('Launches Price Variance Over Time')

plt.show()

"""# Chart the Number of Launches over Time by the Top 10 Organisations. 

How has the dominance of launches changed over time between the different players? 
"""

top_10_orgs = df_data.groupby(['Organisation', 'Year']).agg({'Price':pd.Series.mean})

top_10_orgs

# use get_level_values because we have a multiindex, this allows us to create a sunburst

fig5 = px.sunburst(top_10_orgs, path=[top_10_orgs.index.get_level_values(0), top_10_orgs.index.get_level_values(1), 'Price'])
fig5.show()

"""# Cold War Space Race: USA vs USSR

The cold war lasted from the start of the dataset up until 1991.
"""

df_data.Year = pd.to_numeric(df_data.Year)

df_cold_war = df_data[df_data.Year <= 1991]  # get all data from before and up until 1991

df_cold_war.head()  # we can see from the latest data is from 1991 now

"""## Create a Pie Chart comparing the total number of launches of the USSR and the USA

Hint: Remember to include former Soviet Republics like Kazakhstan when analysing the total number of launches. 
"""

df_cold_war = df_cold_war[(df_cold_war.Country == 'Russian Federation') | (df_cold_war.Country == 'Kazakhstan') | (df_cold_war.Country == 'USA')]  # get USSR launches and USA launches as seperate DFs

df_cold_war.Country = df_cold_war.Country.str.replace('Russian Federation', 'USSR')
df_cold_war.Country = df_cold_war.Country.str.replace('Kazakhstan', 'USSR')
df_cold_war.rename(columns={'Country':'Region'}, inplace=True)

USA_vs_USSR_launches = pd.DataFrame({'Region': ['USA', 'USSR'], 'Launches': [df_cold_war[df_cold_war.Region == 'USA'].count()[0], df_cold_war[df_cold_war.Region == 'USSR'].count()[0]]})
USA_vs_USSR_launches  # create this array so we can easily plot it on the pie chart

plt.figure(figsize=(8,8), dpi=100)

fig6 = px.pie(
    USA_vs_USSR_launches,
    names='Region',
    values='Launches',
    title='USA vs USSR Launches Before and During the Cold War Space Race'
)

fig6.show()

"""## Create a Chart that Shows the Total Number of Launches Year-On-Year by the Two Superpowers"""

launches_per_year = df_cold_war.groupby(['Year', 'Region']).size().reset_index(name='Launches')
launches_per_year.head()

fig7 = px.line(
    launches_per_year,
    x='Year',
    y='Launches',
    color='Region',
)

fig7.show()

"""## Chart the Total Number of Mission Failures Year on Year."""

failures_per_year = df_cold_war[df_cold_war.Mission_Status == 'Failure'].groupby(['Year', 'Region']).size().reset_index(name='Launches')
failures_per_year.head()

fig8 = px.line(
    failures_per_year,
    x='Year',
    y='Launches',
    color='Region',
)

fig8.show()

"""# For Every Year Show which Country was in the Lead in terms of Total Number of Successful Launches up to and including including 2020)

Do the results change if we only look at the number of successful launches? 
"""

yearly_successes = df_data[(df_data.Mission_Status == 'Success') & (df_data.Year <= 2020)].groupby(['Year', 'Country']).size().reset_index(name='Launches')
yearly_successes.head()

fig9 = px.line(
    yearly_successes,
    x='Year',
    y='Launches',
    color='Country',
)

fig9.show()

"""# Create a Year-on-Year Chart Showing the Organisation Doing the Most Number of Launches

Which organisation was dominant in the 1970s and 1980s? Which organisation was dominant in 2018, 2019 and 2020? 
"""

yearly_org_launches = df_data.groupby(['Year', 'Organisation']).size().reset_index(name='Launches')
yearly_org_launches.head()

fig10 = px.line(
    yearly_org_launches,
    x='Year',
    y='Launches',
    color='Organisation',
)

fig10.show()