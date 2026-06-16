# Task 3: Interactive Visualizations with Plotly
 
import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

print('first 10 lines:')
print(df.head(10))

print('last 10 lines:')
print(df.tail(10))

# print(df['strength'].unique())

convert = {'0-1':0.5, '1-2': 1.5, '2-3': 2.5, '3-4': 3.5, '4-4': 4.0, '4-5': 4.5, '5-6': 5.5, '6+': 6.5}

df['strength'] = df['strength'].map(convert)

# for i in df['strength'].unique():
#     print(f'{type(i)}: {i}')

fig = px.scatter(df, x='frequency', y='strength', color='direction', title="Wind Strength, Direction vs. Frequency", hover_data="frequency")
fig.write_html("wind.html", auto_open=True)