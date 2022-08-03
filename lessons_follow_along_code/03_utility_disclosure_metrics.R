library(tidyverse)
source(here::here("lessons", "create_table.R"))

# --- Setup -----

set.seed(134)

# Create confidential and synthetic data
conf_data = starwars %>% 
  select(gender, height, mass) %>% 
  drop_na() %>%
  # Filter out one outlier mass value
  filter(mass != 1358)

conf_data %>% 
  head(2) %>% 
  add_row(gender = NA) %>% 
  create_table()


nrow_conf_data = nrow(conf_data)

synth_data = tibble(
  gender = sample(conf_data$gender, size = nrow_conf_data, replace = F)
)

# --- Examples/Demonstration -----


height_gender_model = lm(height ~ gender, data = conf_data)
height_gender_mass_model = lm(mass ~ height + gender, data = conf_data)


predicted_heights = predict(height_gender_model, data = synth_data)
predicted_masses = predict(height_gender_mass_model, data = synth_data)

synth_data = synth_data %>% 
  mutate(
    height = rnorm(n = nrow_conf_data,
                   mean = predicted_heights,
                   sd = sigma(height_gender_model)),
  )

synth_data = synth_data %>% 
  mutate(
    mass = rnorm(n = nrow_conf_data,
                 mean = predicted_masses,
                 sd = sigma(height_gender_mass_model)),
  )

synth_data %>% 
  head(2) %>% 
  add_row(gender = NA) %>% 
  create_table()

conf_data = conf_data %>% 
  mutate(
    gender = if_else(gender == "masculine", 0, 1)
  ) 

synth_data = synth_data %>% 
  mutate(
    gender = if_else(gender == "masculine", 0, 1)
  ) 

#------- Exercise 1 ---------------

## Question 1

# Fill in the blanks below:

# The cor() function can take in a dataframe and compute correlations 
# between all columns in the dataframe and spit out a correlation matrix
conf_data_correlations = cor(###)
synth_data_correlations = cor(###)

correlation_differences = conf_data_correlations - synth_data_correlations

# Correlation fit is the sum of the sqrt of the squared differences between each correlation in the difference matrix.
cor_fit = sum(sqrt( ### ^2))
  
cor_fit
      

## Question 2
# Fill in the blanks below:
combined_data = bind_rows("synthetic" = synth_data, 
                          "confidential" = conf_data,
                          .id = "type")

# Create a density plot of the mass distributions
combined_data %>% 
  ggplot(aes(x = ###,
               fill = type,),
         position = "dodge",
         color = "white") +
  geom_density(alpha = 0.4)

# Create a density plot of the height distributions
combined_data %>% 
  ggplot(aes(x = ###,
               fill = type,),
         position = "dodge",
         color = "white") +
  geom_density(alpha = 0.4)

