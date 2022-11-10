import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def read_gff(file_path):
    gff = pd.read_csv(file_path, sep='\t', comment='t',
                     names=['seqid', 'resourse', 'type', 'start', 'end', 'score', 'strand', 'frame', 'attribute'])
    gff.drop(index = gff[gff['seqid'].str.contains('#')].index, inplace=True)
    gff.reset_index(inplace=True)
    gff['attribute'] = gff['attribute'].astype(str).apply(lambda x: x.split('_')[0].split('=')[1])
    return gff


def read_bed6(file_path):
    bed6 = pd.read_csv(file_path, sep='\t',  names = ['chrom', 'chromStart', 'chromEnd', 'name', 'score', 'strand'])
    return bed6


def rna_count(file_path):
    gff = read_gff(file_path)
    rnas_count = gff.groupby(['seqid','attribute']).size().to_frame().reset_index()
    rnas_count = rnas_count.rename(columns={0:'quantity', 'attribute':'RNA type'})
    return rnas_count


gff = read_gff('/rrna_annotation.gff')
bed = read_bed6('alignment.bed')
gff.join(bed,lsuffix='_caller', rsuffix='_other')

gff_file = rna_count('/rrna_annotation.gff')
gff_file.pivot(index='seqid', columns='RNA type', values='quantity').plot.bar(figsize=(15,8))