import pandas as pd
import seaborn as sns 
import numpy as np
from palmerpenguins import load_penguins
from numpy import random
from scipy import stats
import math
import statsmodels.api as sm

# ---- Setup -----

# Read in conf and synthetic data for exercise
conf_data = pd.read_csv("data/lesson_03_conf_data.csv")
synth_data = pd.read_csv("data/lesson_03_synth_data.csv")


# ---------- Exercise 1 ----------

## Question 1
conf_data_correlations = ###.corr()
synth_data_correlations = ###.corr()


correlation_differences = conf_data_correlations - synth_data_correlations


cor_fit = np.sqrt(np.power(###, 2)).to_numpy().sum()



## Question 2
# Fill in the blanks below:
conf_data["type"] = "confidential"
synth_data["type"] = "synthetic"

combined_data = conf_data.append(synth_data).reset_index()

# Create a density plot of the mass distributions
sns.histplot(data = combined_data, 
            x = ###, 
            hue = 'type').set(title = 'Comparison of mass Distributions')


# Create a density plot of the height distributions
sns.histplot(data = combined_data,
            x = ###, 
            hue = 'type').set(title = 'Comparison of height Distributions')
