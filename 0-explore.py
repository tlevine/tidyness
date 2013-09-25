#!/usr/bin/env python2
import os
import urllib
import random

import pandas

def strings(sample, template):
    return [template % (portal, id) for portal, id in zip(sample['portal'], sample['id'])]

n = 100 # sample size
random.seed(9884892)

df = pandas.read_csv('socrata-deduplicated.csv')
sample = df[['portal', 'id']].ix[random.sample(range(df.shape[0]), n)]

web = strings(sample, 'https://%s/d/%s')
csv = strings(sample, 'https://%s/api/views/%s/rows.csv?accessType=DOWNLOAD')

for url, id in zip(csv, sample['id']):
    urllib.urlretrieve(url, filename = os.path.join('data', id))
