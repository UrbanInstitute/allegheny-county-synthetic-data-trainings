import pandas as pd
import seaborn as sns 
import numpy as np
from palmerpenguins import load_penguins
from numpy import random
from scipy import stats
import math
import statsmodels.api as sm 

# ---- Setup -----

# set global defaults for all plots
sns.set_theme(style="whitegrid", font = "lato")

# set a seed so pseudo-random processes are reproducible
random.seed(20200301)


# --- Demo: Fully synthetic `palmerpenguins` data ----

# create dataset we will be using
penguins = load_penguins()
penguins = penguins.query("species == 'Adelie'")[['sex', 'bill_length_mm', 'flipper_length_mm']].dropna()

## Synthesize `sex` variable
# identify percentage of total that each category (sex) makes up
absolute_freq = penguins['sex'].value_counts()
relative_freq = penguins['sex'].value_counts(normalize = True)

pd.concat([absolute_freq.to_frame(name = "n"), relative_freq.to_frame(name = "relative frequency")], axis = 1)

# list of sex categories
sex_categories = penguins['sex'].unique().tolist()

# size of sample to generate
synthetic_data_size = len(penguins)

# probability weights
sex_probs = relative_freq.to_numpy()

# use random.choice to generate synthetic sample of sex
sex_synthetic = np.random.choice(a = sex_categories, size = synthetic_data_size, p = sex_probs)

# use array to generate synthetic gender column
penguins_synthetic = pd.DataFrame(sex_synthetic, columns = ['sex'])

## Synthesize `bill_length_mm` variable
# summarize bill_length_mm
penguins['bill_length_mm'].describe()

# make sex binary for regression
penguins['sex'] = penguins['sex'].replace(['male', 'female'], [0, 1])
penguins_synthetic['sex'] = penguins_synthetic['sex'].replace(['male', 'female'], [0, 1])

# linear regression with sex as a predictor
bill_length_lm = result = sm.OLS.from_formula(formula="bill_length_mm ~ sex", data=penguins).fit() 
bill_length_lm.summary()

# predict bill length with model weights
bill_length_synthetic_method1 = bill_length_lm.predict(penguins_synthetic)

# add predictions to synthetic data as bill_length
penguins_synthetic["bill_length_mm"] = bill_length_synthetic_method1

# create dataframe with both confidential and synthesized values
penguins["data_source"] = "confidential"
penguins_synthetic["data_source"] = "synthetic"

compare_penguins = pd.concat([penguins[["sex", "bill_length_mm", "data_source"]], penguins_synthetic]).reset_index()

# plot comparison of bill_length_mm distributions
sns.histplot(data = compare_penguins, x = 'bill_length_mm', hue = 'data_source').set(title = 'Comparison of Univariate Distributions')

# Look at first few rows of synthetic data
penguins_synthetic.head()


# In statsmodels, the sqrt of the scale factor for the covariance matric is the
# residual standard error
sigma = np.sqrt(bill_length_lm.scale)

# predict bill length with model weights
bill_length_predicted = bill_length_lm.predict(penguins_synthetic).to_numpy()

# synthetic column using normal distribution centered on predictions with sd of residual standard error
bill_length_synthetic_method2 = np.random.normal(loc = bill_length_predicted, scale = sigma, size  = penguins.shape[0])

# add predictions to synthetic data as bill_length
penguins_synthetic["bill_length_mm"] = bill_length_synthetic_method2

penguins_synthetic["bill_length_mm"]

# create dataframe with both confidential and synthesized values
compare_penguins = pd.concat([penguins[["sex", "bill_length_mm", "data_source"]], penguins_synthetic]).reset_index()

# plot comparison of bill_length_mm distributions
sns.histplot(data = compare_penguins, x = 'bill_length_mm', hue = 'data_source').set(title = 'Comparison of Univariate Distributions')


## Synthesize `flipper_length_mm`
penguins["flipper_length_mm"].describe()

# linear regression to predict flipper_length_mm
penguins[['sex',"bill_length_mm"]]

flipper_length_lm  = sm.OLS.from_formula(formula="flipper_length_mm ~ bill_length_mm + sex", data=penguins).fit() 
flipper_length_lm.summary()

# In statsmodels, the sqrt of the scale factor for the covariance matrix is the
# residual standard error
sigma = np.sqrt(flipper_length_lm.scale)

# predict bill length with model weights
flipper_length_predicted = flipper_length_lm.predict(penguins_synthetic).to_numpy()

# synthetic column using normal distribution centered on predictions with sd of residual standard error
flipper_length_synthetic_method2 = np.random.normal(loc = flipper_length_predicted, scale = sigma, size  = penguins.shape[0])

# add predictions to synthetic data as bill_length
penguins_synthetic["flipper_length_mm"] = flipper_length_synthetic_method2

# create dataframe with both confidential and synthesized values
compare_penguins = pd.concat([penguins[["sex", "bill_length_mm", "flipper_length_mm", "data_source"]], penguins_synthetic]).reset_index()

# Make histogram of flipper length
sns.histplot(data = compare_penguins, x = 'flipper_length_mm', hue = "data_source").set(title = 'Histogram of univariate distributions')

# Make histogram of bill length
sns.histplot(data = compare_penguins, x = 'bill_length_mm', hue = "data_source").set(title = 'Histogram of univariate distributions')



# --- Exercise 3 ---- 

# Read in starwars data
starwars = pd.read_csv("https://raw.githubusercontent.com/tidyverse/dplyr/main/data-raw/starwars.csv")[["gender", "height"]].dropna()

random.seed(20200301)

# Question 1: Synthesize gender variable by filling in blanks below
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
