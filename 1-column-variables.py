#!/usr/bin/env python
'''
"column headers are values, not variable names"
'''

import pymc as mc

observed_column_variableness = [True, False, False, True]



naive_chance_column_is_variable = mc.Beta(1, 1)

column_is_a_variable = mc.Bernoulli('column_is_a_variable',
    naive_chance_column_is_variable, value=observed_column_variableness, observed=True)
