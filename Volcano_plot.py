import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

diffexpr_data = pd.read_csv('/diffexpr_data.tsv.gz', header=0, sep='\t', quotechar='"')
print(diffexpr_data)

data_for_volcano = diffexpr_data[['logFC','log_pval']]
print(data_for_volcano)

s_down = data_for_volcano.query('`logFC`<0 and `log_pval`>0.5')
s_up = data_for_volcano.query('`logFC`>0 and `log_pval`>0.5')
ns_down = data_for_volcano.query('`logFC`<0 and `log_pval`<0.5')
ns_up = data_for_volcano.query('`logFC`>0 and `log_pval`<0.5')

fig, ax = plt.subplots(figsize=(20, 12))

ax.set_xticks([i for i in range(-10,11,2)], minor=False)
ax.set_xticks([i for i in range(-10,11)], minor=True)
ax.set_yticks([i for i in range(0,101,20)], minor=False)
ax.set_yticks([i for i in range(0,101,5)], minor=True)
ax.tick_params(axis='both', length=10, width=3)
ax.tick_params(which='minor', length=4, color='black')
plt.rc("xtick.minor", visible=True)
plt.rc("ytick.minor", visible=True)
plt.rc("xtick.minor", width=0.05)
plt.rc("ytick.minor", width=0.05)

plt.scatter(s_down['logFC'],s_down['log_pval'], color = 'steelblue', s=5, label='Significantly downregulated')
plt.scatter(s_up['logFC'],s_up['log_pval'], color = 'orange', s=5, label='Significantly upregulated')
plt.scatter(ns_down['logFC'],ns_down['log_pval'], color = 'yellowgreen', s=5, label='Non-significantly downregulated')
plt.scatter(ns_up['logFC'],ns_up['log_pval'], color = 'crimson', s=5, label='Non-significantly upregulated')

ax.axhline(0.5, linestyle="--", alpha=0.5, color='black', linewidth=2)
ax.axvline(0, linestyle="--", alpha=0.5, color='black', linewidth=2)

plt.legend(shadow=True, markerscale=5.0, borderaxespad=1, prop={'size':16, 'weight':'bold'})
ax.set_xlim(-54 * width, 54 * width)

plt.xlabel('log$_2$(fold change)', size=20, style='italic', weight="bold", color="black",fontfamily = 'sans-serif')
plt.ylabel("-log$_{10}$(p-value corrected)", size=20, style='italic', weight="bold", color="black",fontfamily = 'sans-serif')
plt.title("Volcano plot", size=35, style='italic', weight="bold", color="black",fontfamily = 'sans-serif')

ax.text(0.95, 0.06, 'p value = 0.05',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='grey', fontsize=14)

s_up_2 = diffexpr_data[diffexpr_data['log_pval']>0.05].head(2)[['Sample', 'logFC','log_pval']] # 2 Significantly upregulated samples to annotate
s_down_2 = diffexpr_data[diffexpr_data['log_pval']>0.05].tail(2)[['Sample', 'logFC','log_pval']] # 2 Significantly downregulated samples to annotate

ax.annotate('UMOD',
            xy=(-10.661093, 52.117378), xycoords='data',weight='bold',
            xytext=(15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05, edgecolor='red'),
            horizontalalignment='left', verticalalignment='bottom')
ax.annotate('MUC7',
            xy=(-9.196481, 2.171498), xycoords='data',weight='bold',
            xytext=(15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05, edgecolor='red'),
            horizontalalignment='left', verticalalignment='bottom')
ax.annotate('CA9',
            xy=(4.617241, 0.935710), xycoords='data',weight='bold',
            xytext=(15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05, edgecolor='red'),
            horizontalalignment='left', verticalalignment='bottom')
ax.annotate('ZIC2',
            xy=(4.571915, 3.075183), xycoords='data', weight='bold',
            xytext=(15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05, edgecolor='red'),
            horizontalalignment='right', verticalalignment='bottom')

plt.show()
