#!/usr/bin/env python
# coding: utf-8

# # Lesson 2: Synthetic Data Methods and Case Studies

# Each section of code is labeled with the corresponding section header in the main lesson. Note that since the random seeds are set differently across R and Python, not all of the values/output will be identical to the R version of the lesson.


# import packages we need
import pandas as pd
import seaborn as sns 
import numpy as np
from palmerpenguins import load_penguins
from numpy import random
from scipy import stats
import math
import statsmodels.api as sm




# set global defaults for all plots
# plot attendee ages
sns.set_theme(style="whitegrid", font = "lato")


# In[55]:


# set a seed so pseudo-random processes are reproducible
random.seed(20200301)

# fake dataframe of conference attendees with missing values
sample_conf_data_na = {'attendee_number': list(range(41,81)),
        'age': [None]*40}
 
sample_conf_na = pd.DataFrame(sample_conf_data_na)

# fake distribution of attendee ages
attendee_ages = np.random.normal(loc=46, scale=13, size=40)

attendee_ages

# fake dataframe of conference attendees using age distribution
sample_conf_data = {'attendee_number': list(range(1,41)),
                   'age': list(attendee_ages)}

sample_conf = pd.DataFrame(sample_conf_data)

# combine for final (fake) conference data
sample_conf_final = pd.concat([sample_conf, sample_conf_na])

sample_conf_final


# In[56]:


# plot distribution of the 40 age observations that are not missing.
sns.histplot(data = sample_conf, x = 'age').set(title = 'Histogram of attendee ages')


# In[57]:


# replace NA values with mean age
sample_conf_final['age'] = sample_conf_final['age'].fillna(sample_conf_final['age'].mean())

sample_conf_final = sample_conf_final.reset_index(drop = True)


# In[58]:


# replot the histogram
sns.histplot(data = sample_conf_final, x = 'age').set(title = 'Histogram of attendee ages (with missing values imputed)')


# ## Demonstration: Fully synthetic `palmerpenguins` data

# In[59]:


# create dataset we will be using
penguins = load_penguins()
penguins = penguins.query("species == 'Adelie'")[['sex', 'bill_length_mm', 'flipper_length_mm']].dropna()


# In[60]:


penguins


# ### Synthesize `sex` variable

# In[61]:


# identify percentage of total that each category (sex) makes up
absolute_freq = penguins['sex'].value_counts()

relative_freq = penguins['sex'].value_counts(normalize = True)

pd.concat([absolute_freq.to_frame(name = "n"), relative_freq.to_frame(name = "relative frequency")], axis = 1)


# In[96]:


# set a seed so pseudo-random processes are reproducible
random.seed(20200301)




# list of sex categories
sex_categories = penguins['sex'].unique().tolist()

# size of sample to generate
synthetic_data_size = len(penguins)

# probability weights
sex_probs = relative_freq.to_numpy()

# use random.choice to generate synthetic sample of sex
sex_synthetic = np.random.choice(a = sex_categories, size = synthetic_data_size, p = sex_probs)


# In[63]:


# use array to generate synthetic gender column
penguins_synthetic = pd.DataFrame(sex_synthetic, columns = ['sex'])

penguins_synthetic


# ### Synthesize `bill_length_mm` variable

# In[64]:


# summarize bill_length_mm
penguins['bill_length_mm'].describe()


# In[65]:


# make sex binary for regression
penguins['sex'] = penguins['sex'].replace(['male', 'female'], [0, 1])
penguins_synthetic['sex'] = penguins_synthetic['sex'].replace(['male', 'female'], [0, 1])

# linear regression with sex as a predictor
bill_length_lm = result = sm.OLS.from_formula(formula="bill_length_mm ~ sex", data=penguins).fit() 
bill_length_lm.summary()


# In[66]:



# predict bill length with model weights
bill_length_synthetic_method1 = bill_length_lm.predict(penguins_synthetic)


# add predictions to synthetic data as bill_length
penguins_synthetic["bill_length_mm"] = bill_length_synthetic_method1


# In[67]:


# create dataframe with both confidential and synthesized values
penguins["data_source"] = "confidential"
penguins_synthetic["data_source"] = "synthetic"

compare_penguins = pd.concat([penguins[["sex", "bill_length_mm", "data_source"]], penguins_synthetic]).reset_index()

# plot comparison of bill_length_mm distributions
sns.histplot(data = compare_penguins, x = 'bill_length_mm', hue = 'data_source').set(title = 'Comparison of Univariate Distributions')


# In[68]:


# Look at first few rows of synthetic data
penguins_synthetic.head()


# In[69]:



# In statsmodels, the sqrt of the scale factor for the covariance matric is the
# residual standard error
sigma = np.sqrt(bill_length_lm.scale)

# predict bill length with model weights
bill_length_predicted = bill_length_lm.predict(penguins_synthetic).to_numpy()

# synthetic column using normal distribution centered on predictions with sd of residual standard error
bill_length_synthetic_method2 = np.random.normal(loc = bill_length_predicted, scale = sigma, size  = penguins.shape[0])


# # add predictions to synthetic data as bill_length
penguins_synthetic["bill_length_mm"] = bill_length_synthetic_method2


# In[70]:


penguins_synthetic["bill_length_mm"]


# In[71]:


# create dataframe with both confidential and synthesized values

compare_penguins = pd.concat([penguins[["sex", "bill_length_mm", "data_source"]], penguins_synthetic]).reset_index()

# plot comparison of bill_length_mm distributions
sns.histplot(data = compare_penguins, x = 'bill_length_mm', hue = 'data_source').set(title = 'Comparison of Univariate Distributions')


# ### Synthesize `flipper_length_mm`

# In[72]:


penguins["flipper_length_mm"].describe()


# In[73]:


# linear regression to predict flipper_length_mm
penguins[['sex',"bill_length_mm"]]

flipper_length_lm  = sm.OLS.from_formula(formula="flipper_length_mm ~ bill_length_mm + sex", data=penguins).fit() 
flipper_length_lm.summary()


# In[75]:


# In statsmodels, the sqrt of the scale factor for the covariance matrix is the
# residual standard error
sigma = np.sqrt(flipper_length_lm.scale)

# predict bill length with model weights
flipper_length_predicted = flipper_length_lm.predict(penguins_synthetic).to_numpy()

# synthetic column using normal distribution centered on predictions with sd of residual standard error
flipper_length_synthetic_method2 = np.random.normal(loc = flipper_length_predicted, scale = sigma, size  = penguins.shape[0])


# # add predictions to synthetic data as bill_length
penguins_synthetic["flipper_length_mm"] = flipper_length_synthetic_method2

penguins_synthetic


# In[79]:


# create dataframe with both confidential and synthesized values
compare_penguins = pd.concat([penguins[["sex", "bill_length_mm", "flipper_length_mm", "data_source"]], penguins_synthetic]).reset_index()


# Make histogram of flipper length
sns.histplot(data = compare_penguins, x = 'flipper_length_mm', hue = "data_source").set(title = 'Histogram of univariate distributions')


# In[80]:


# Make histogram of bill length
sns.histplot(data = compare_penguins, x = 'bill_length_mm', hue = "data_source").set(title = 'Histogram of univariate distributions')


# In[92]:


starwars = pd.read_csv("https://raw.githubusercontent.com/tidyverse/dplyr/main/data-raw/starwars.csv")[["gender", "height"]].dropna()

starwars.head()


# In[99]:


### ---- Exercise 3!

# Question 1: Synthesize gender variable by filling in blanks below

random.seed(20200301)


relative_freq = starwars['###___'].value_counts(normalize = True)

# list of sex categories
gender_categories = starwars['gender'].unique().tolist()

# size of sample to generate
synthetic_data_size = len(starwars)

# probability weights
gender_probs = relative_freq.to_numpy()


# use random.choice to generate synthetic sample of sex
gender_synthetic = np.random.choice(a = ###___, 
                                size = ###___, 
                                p = ###___
                                )

starwars_synthetic = pd.DataFrame({"gender": gender_synthetic})       
starwars_synthetic             


# In[102]:


# Question 2: Synthesize height variable by filling in blanks below
height_lm  = sm.OLS.from_formula(formula="###___ ", 
                                data=###___)\
                                .fit() 

sigma = np.sqrt(height_lm.scale)

# predict height with model weights
height_predicted = flipper_length_lm.predict(###___)
                            .to_numpy()

# synthetic column using normal distribution centered on predictions with sd of residual standard error
flipper_length_synthetic_method2 = np.random.normal(loc = ###___, 
                                        scale = ###___,
                                        size  = starwars.shape[0])


# # add predictions to synthetic data as height column
starwars_synthetic["height"] = ###___

