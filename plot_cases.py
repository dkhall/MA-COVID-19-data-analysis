import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

ma_data = pd.read_csv('data/ma_covid_19.csv', index_col=0)

fig, ax = plt.subplots()
plt.semilogy(ma_data.index, ma_data['Total Tested'], 'bo', mfc='w', ms=5, label='total tested')
plt.semilogy(ma_data.index, ma_data['Confirmed Cases'], 'k.', ms=7, label='confirmed cases')
plt.semilogy(ma_data.index, ma_data['Deaths'], 'rx', ms=7, label='deaths')

ax.set_ylim([0.9,1e5])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title('COVID-19 in Massachusetts [source: MA DPH]')
plt.legend(loc=2)
plt.show()
