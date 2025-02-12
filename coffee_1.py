# version v0.0.0
import numpy as np
import plotly.express as px
import pandas as pd

presence_coffee = np.random.normal(loc=5, scale=2, size=100)
presence_sandwich = np.random.normal(loc=5, scale=2, size=100)
capacity_index = 10 

sustainable = presence_coffee + presence_sandwich <= capacity_index

data = {
    'Presence Coffee': presence_coffee,
    'Presence Sandwich': presence_sandwich,
    'Sustainable': sustainable
}

df = pd.DataFrame(data)

fig = px.scatter(df, x='Presence Coffee', y='Presence Sandwich', color='Sustainable',
                 title='Sustainable Area', labels={'Presence Coffee': 'Presence Coffee', 'Presence Sandwich': 'Presence Sandwich'})

x = np.linspace(min(presence_coffee), max(presence_coffee), 100)
y = capacity_index - x
fig.add_scatter(x=x, y=y, mode='lines', name='Sustainability Line')

fig.show()