import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

ma_data = pd.read_csv('data/ma_covid_19.csv', index_col=0)

dates = []
for ii in ma_data.index:
    dates.append(dt.datetime.strptime(ii + ' 21:00', '%Y-%m-%d %H:%M'))


fig, ax = plt.subplots()
#plt.semilogy(dates, ma_data['Total Tested'], 'b-')
#plt.semilogy(dates[-1], ma_data['Total Tested'][-1], 'b.')
#ax.annotate('Total Tested: {:,}'.format(int(ma_data['Total Tested'][-1])), (dates[-1]+dt.timedelta(hours=6),
#    0.85*ma_data['Total Tested'][-1]), color='blue', fontsize=9)

plt.semilogy(dates, ma_data['Confirmed Cases'], 'k.', ms=3)
#plt.semilogy(dates[-1], ma_data['Confirmed Cases'][-1], 'k.')
ax.annotate('Confirmed Cases: {:,}'.format(int(ma_data['Confirmed Cases'][-1])), (dates[-1]+dt.timedelta(hours=24),
    0.8*ma_data['Confirmed Cases'][-1]), color='black', fontsize=9)

plt.semilogy(dates, ma_data['Deaths'], 'r.', ms=3)
#plt.semilogy(dates[-1], ma_data['Deaths'][-1], 'r.')
ax.annotate('Deaths: {:,}'.format(int(ma_data['Deaths'][-1])), (dates[-1]+dt.timedelta(hours=24), 0.8*ma_data['Deaths'][-1]),
        color='red', fontsize=9)

#plt.semilogy(dates, ma_data['Suffolk'],'g-')
#plt.semilogy(dates[-1], ma_data['Suffolk'][-1], 'g.')
#ax.annotate('Suffolk: {:,}'.format(int(ma_data['Suffolk'][-1])), (dates[-1]+dt.timedelta(hours=12), 0.65*ma_data['Suffolk'][-1]),
#        color='green', fontsize=9)
#
#plt.semilogy(dates, ma_data['Middlesex'],'-', color='orange')
#plt.semilogy(dates[-1], ma_data['Middlesex'][-1], '.', color='orange')
#ax.annotate('Middlesex: {:,}'.format(int(ma_data['Middlesex'][-1])), (dates[-1]+dt.timedelta(hours=12),
#    1.15*ma_data['Middlesex'][-1]), color='orange', fontsize=9)

ax.set_ylim([0.9,7e6])
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18, right=0.75)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title('COVID-19 in Massachusetts [source: MA DPH]')
plt.show()

daily_deaths = ma_data['Deaths'].values[1:] - ma_data['Deaths'].values[:-1]
fig, ax = plt.subplots()
plt.bar(dates[1:], daily_deaths, width=1)
plt.plot(dates[7:], (daily_deaths[:-6]+daily_deaths[1:-5]+daily_deaths[2:-4]+daily_deaths[3:-3]+daily_deaths[4:-2]+daily_deaths[5:-1]+daily_deaths[6:])/7, 'r.-')
ax.xaxis.set_tick_params(rotation=45, labelsize=10)
fig.subplots_adjust(bottom=0.18)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylabel('new reported deaths by day [source: MA DPH]')
plt.show()
