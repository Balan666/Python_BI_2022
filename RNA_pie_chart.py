import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gff_file = rna_count('/rrna_annotation.gff')
x = gff_file.pivot(index='seqid', columns='RNA type', values='quantity')

# make data
gff_file = rna_count('/rrna_annotation.gff')
x = gff_file.pivot(index='seqid', columns='RNA type', values='quantity')

# plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

overall_ratios = [x['16S'].sum(),x['23S'].sum(),x['5S'].sum()]
labels = ['16S', '23S', '5S']
explode = [0.1, 0.03, 0.03]

# rotate so that first wedge is split by the x-axis
angle = -40 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode, wedgeprops = {'linewidth': 3})

for i in wedges:
  ax.annotate(i,xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment)

# bar chart parameters
rna_ratios = x['16S']
rna_labels = x.index.values
bottom = 1
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(rna_ratios, rna_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, label=label)
    #ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

ax2.set_title('16S RNA')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r

# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(2)
ax2.add_artist(con)

# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, -116), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(2)

plt.show()
