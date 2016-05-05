
# coding: utf-8

# In[48]:

import agate


# In[49]:

exonerations = agate.Table.from_csv('exonerations-20150828.csv')

print exonerations


# In[50]:

print exonerations.columns[10]


# In[51]:

first_row = exonerations.rows[0]
print first_row
print first_row['dna']


# In[52]:

num_false_confessions = exonerations.aggregate(agate.Count('false_confession', True))

print(num_false_confessions)


# In[53]:

median_age = exonerations.aggregate(agate.Median('age'))

print(median_age)


# In[54]:

num_without_age = exonerations.aggregate(agate.Count('age', None))

print(num_without_age)


# In[55]:

mo = exonerations.aggregate(agate.Count('state', 'MO'))
print mo


# In[56]:

with_age = exonerations.where(lambda row: row['age'] is not None)


# In[57]:

old = len(exonerations.rows)
new = len(with_age.rows)

print(old - new)


# In[58]:

median_age = with_age.aggregate(agate.Median('age'))

print(median_age)


# In[59]:

with_years_in_prison = exonerations.compute([
    ('years_in_prison', agate.Change('convicted', 'exonerated'))
])

median_years = with_years_in_prison.aggregate(agate.Median('years_in_prison'))

print(median_years)


# In[60]:

full_names = exonerations.compute([
    ('full_name', agate.Formula(agate.Text(), lambda row: '%(first_name)s %(last_name)s' % row))
])


# In[61]:

with_computations = exonerations.compute([
    ('full_name', agate.Formula(agate.Text(), lambda row: '%(first_name)s %(last_name)s' % row)),
    ('years_in_prison', agate.Change('convicted', 'exonerated'))
])


# In[62]:

sorted_by_age = exonerations.order_by('age')

youngest_ten = sorted_by_age.limit(10)

youngest_ten.print_table(max_columns=7)


# In[63]:

binned_ages = exonerations.bins('age', 10, 0, 100)
binned_ages.print_bars('age', 'Count', width=80)


# In[64]:

by_state = exonerations.group_by('state')


# In[65]:

state_totals = by_state.aggregate([
        ('count', agate.Length())
])

sorted_totals = state_totals.order_by('count', reverse=True)

sorted_totals.print_table(max_rows=5)


# In[ ]:

with_years_in_prison = exonerations.compute([
    ('years_in_prison', agate.Change('convicted', 'exonerated'))
])

state_totals = with_years_in_prison.group_by('state')

medians = state_totals.aggregate([
    ('count', agate.Length()),
    ('median_years_in_prison', agate.Median('years_in_prison'))
])

sorted_medians = medians.order_by('median_years_in_prison', reverse=True)

sorted_medians.print_table(max_rows=5)


# In[ ]:

# Filters rows without age data
only_with_age = with_years_in_prison.where(
    lambda r: r['age'] is not None
)

# Group by race
race_groups = only_with_age.group_by('race')

# Sub-group by age cohorts (20s, 30s, etc.)
race_and_age_groups = race_groups.group_by(
    lambda r: '%i0s' % (r['age'] // 10),
    key_name='age_group'
)

# Aggregate medians for each group
medians = race_and_age_groups.aggregate([
    ('count', agate.Length()),
    ('median_years_in_prison', agate.Median('years_in_prison'))
])

# Sort the results
sorted_groups = medians.order_by('median_years_in_prison', reverse=True)

# Print out the results
sorted_groups.print_table(max_rows=10)


# In[ ]:



