import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

ma_data = pd.read_csv('data/ma_covid_19.csv', index_col=0)

fig, ax = plt.subplots()
plt.semilogy(ma_data.index, ma_data['Total Tested'], 'bo-', mfc='w', ms=4,
        label='Total Tested: ' + str(int(ma_data['Total Tested'].iloc[-1])))
plt.semilogy(ma_data.index, ma_data['Confirmed Cases'], 'k.-', ms=5,
        label='Confirmed Cases: ' + str(int(ma_data['Confirmed Cases'].iloc[-1])))
plt.semilogy(ma_data.index, ma_data['Deaths'], 'r+-', ms=4,
        label='Deaths: ' + str(int(ma_data['Deaths'].iloc[-1])))

ax.set_ylim([0.9,1e5])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title('COVID-19 in Massachusetts [source: MA DPH]')
plt.legend(loc=2)
plt.show()
