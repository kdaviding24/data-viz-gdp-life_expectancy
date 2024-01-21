import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

df = pd.read_csv('all_data.csv')

print(df.info())

fig = px.scatter_3d(df, x = 'Year', y = 'Life expectancy at birth (years)', z = 'GDP', color = 'Country')
fig.show()

# Based on the scatter plot, GDP has a strong affect on the life expectancy of each nation. Zimbabwe has the most apparent change although it is hard to see.
# The life expectancy in Zimbabwe was about 44 years while there GDP was around 5-6 billion dollars.
# The achieved a sharp in increase in GDP and Life expentancy (10 billion and 16 years respectively) between 2005 - 2015.
# The other countries graphed saw a hefty increase in GDP but remained stagnent in life exptancy.
# This could suggest that at a certain point GDP stops having an affect on life exptancy. This could be due to a lack of substantial break throughs in medicine among other things.
# While Zimbabwe's life expectancy has not caught the other nations it has increased and will continue to as GDP increases until it reaches that of the other nations.
# Barring any medical advances it will also reach a point in Life Expectancy that will achieve stagnation.

# Next Scatter plots will highlight the difference in growth for zimbabwe and other nations as the GDP increased and also the stagnation of other nations
Life_ex = list(df)[2]

df_countries = [df[df.Country == f'{i}'] for i in list(df.Country.unique())]
for country in df_countries:
    sns.scatterplot(country, x = 'GDP', y= Life_ex)
    ax = plt.subplot()
    ax.set_yticks(range(40, 101, 5))
    plt.title(list(country.Country)[0])
    plt.show()



