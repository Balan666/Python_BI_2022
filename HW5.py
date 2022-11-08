import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame


def read_gff(x):
    df = pd.read_csv(x, sep='\t', comment='t',
                     names=['seqid', 'resourse', 'type', 'start', 'end', 'score', 'strand', 'frame', 'attribute'])
    df.drop(index = df[df['seqid'].str.contains('#')].index, inplace=True)
    df.reset_index(inplace=True)
    df['attribute'] = df['attribute'].astype(str).apply(lambda x: x.split('_')[0].split('=')[1])
    return df


def read_bed6(x):
    df = pd.read_csv(x, sep='\t',  names = ['chrom', 'chromStart', 'chromEnd', 'name', 'score', 'strand'])
    return df


def rna_count(x):
    df = read_gff(x)
    df2 = df.groupby(['seqid','attribute']).size()
    return df2.plot()


#print(read_gff('rrna_annotation.gff'))
#print(read_bed6('alignment.bed'))
#print(df.index(df[df['seqid'].str.contains("#")]).tolist())
print(rna_count('rrna_annotation.gff'))
