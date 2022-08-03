
library(tidyverse)
library(urbnthemes)
library(palmerpenguins)
library(kableExtra)
library(gt)

# --- Setup --------

# Source create_table helper function
source(here::here("lessons", "create_table.R"))


# set Urban Institute data visualization styles
set_urbn_defaults(base_size = 12)

# ---- Run examples/demonstration below: -----



# ----- Exercise 3 -------

# run this to get the dataset we will work with
starwars <- dplyr::starwars %>%
  select(gender, height) %>%
  drop_na()

starwars %>% 
  head() %>% 
  create_table()


# set a seed so pseudo-random processes are reproducible
set.seed(20220301)

## Question 1:
# Fill in the blanks!

# probability weights
gender_probs <- starwars %>%
  count(gender) %>%
  mutate(relative_frequency = ### ______) %>%
           pull(relative_frequency)
         
# use sample function to generate synthetic vector of genders
gender_synthetic <- sample(
 x = ###_____, 
   size = ###_____,
   replace = ###_____, 
   prob = ###_____
)

# create starwars_synthetic dataset using generated variable
starwars_synthetic <- tibble(
 gender = gender_synthetic
)

## Question 2
# Fill in the blanks!

# set a seed so pseudo-random processes are reproducible
set.seed(20220301)

# Fill in the blanks!

# linear regression
height_lm <- lm(
  formula = ###_____,
    data = ###______
)

# predict flipper length with model coefficients
height_predicted <- predict(
  object = height_lm, 
  newdata = ###_____
)

# synthetic column using normal distribution centered on predictions with sd of residual standard error
height_synthetic <- rnorm(
  n = ###_______, 
    mean = ###______, 
    sd = ###______
)

# add new values to synthetic data as height
starwars_synthetic <- starwars_synthetic %>%
  mutate(height = height_synthetic)
