import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

ma_data = pd.read_csv('data/ma_covid_19.csv', index_col=0)

dates = []
for ii in ma_data.index:
    dates.append(dt.datetime.strptime(ii + ' 21:00', '%Y-%m-%d %H:%M'))


fig, ax = plt.subplots()
plt.semilogy(dates, ma_data['Total Tested'], 'b-')
plt.semilogy(dates[-1], ma_data['Total Tested'][-1], 'b.')
ax.annotate('Total Tested: {:,}'.format(int(ma_data['Total Tested'][-1])), (dates[-1]+dt.timedelta(hours=6),
    0.85*ma_data['Total Tested'][-1]), color='blue', fontsize=9)

plt.semilogy(dates, ma_data['Confirmed Cases'], 'k-')
plt.semilogy(dates[-1], ma_data['Confirmed Cases'][-1], 'k.')
ax.annotate('Confirmed Cases: {:,}'.format(int(ma_data['Confirmed Cases'][-1])), (dates[-1]+dt.timedelta(hours=6),
    0.85*ma_data['Confirmed Cases'][-1]), color='black', fontsize=9)

plt.semilogy(dates, ma_data['Deaths'], 'r-')
plt.semilogy(dates[-1], ma_data['Deaths'][-1], 'r.')
ax.annotate('Deaths: {:,}'.format(int(ma_data['Deaths'][-1])), (dates[-1]+dt.timedelta(hours=6), 0.85*ma_data['Deaths'][-1]),
        color='red', fontsize=9)

plt.semilogy(dates, ma_data['Suffolk'],'g-')
plt.semilogy(dates[-1], ma_data['Suffolk'][-1], 'g.')
ax.annotate('Suffolk: {:,}'.format(int(ma_data['Suffolk'][-1])), (dates[-1]+dt.timedelta(hours=6), 0.75*ma_data['Suffolk'][-1]),
        color='green', fontsize=9)

plt.semilogy(dates, ma_data['Middlesex'],'-', color='orange')
plt.semilogy(dates[-1], ma_data['Middlesex'][-1], '.', color='orange')
ax.annotate('Middlesex: {:,}'.format(int(ma_data['Middlesex'][-1])), (dates[-1]+dt.timedelta(hours=6),
    0.95*ma_data['Middlesex'][-1]), color='orange', fontsize=9)

ax.set_ylim([0.9,1e5])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18, right=0.75)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title('COVID-19 in Massachusetts [source: MA DPH]')
plt.show()
