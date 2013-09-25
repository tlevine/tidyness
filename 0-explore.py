#!/usr/bin/env python2
import random

import pandas

def strings(sample, template):
    urls = [template % (portal, id) for portal, id in zip(sample['portal'], sample['id'])]

n = 100 # sample size
random.seed(9884892)

df = pandas.read_csv('socrata-deduplicated.csv')
sample = df[['portal', 'id']].ix[random.sample(range(df.shape[0]), n)]

web = strings(sample, 'https://%s/d/%s')
csv = strings(sample, 'https://%s/api/views/%s/rows.csv?accessType=DOWNLOAD')

