# allegheny-county-synthetic-data-trainings

This repo contains the lessons and the code used for Allegheny County's Intro to Data Privacy 3 part training series. The course website can be accessed at either of the following links:

- [https://urbaninstitute.github.io/allegheny-county-synthetic-data-trainings/](https://urbaninstitute.github.io/allegheny-county-synthetic-data-trainings/)
- [https://golden-kelpie-4213b8.netlify.app/](https://golden-kelpie-4213b8.netlify.app/)

# Overview of Files

All the lesson HTML files linked above were created in R Markdown and can be found in the lessons/ folder.This repo also has some follow along code templates and code solutions fo each weeks lesson. Below is an overview of all the folders in this repo:

```
.
├── README.md
├── bea-data-privacy-trainings.Rproj
├── solutions/ # Solutions to all code in lessons_follow_along_code/ folder
├── data/ # Data used in lessons and follow along code
├── lessons/ # Rmds used to create the lesson pages
│   ├── 02_synthetic_data_methods.R
│   ├── 02_synthetic_data_methods.py
│   ├── 03_utility_disclosure_metrics.R
│   └── 03_utility_disclosure_metrics.py
├── lessons_follow_along_code/ # Follow along code templates for each lesson in R and Python
└── www/ # images and housekeeping stuff used in lessons
```


<br>

## Code Requirements

In order to run the R scripts in `lessons_follow_along_code`, you will need the following R packages installed:
  
  - tidyverse
  - palmerpenguins
  - kableExtra
  - gt
  - here
  - smoothmest
  - urbnthemes (can be installed with `remotes::install_github("UrbanInstitute/urbnthemes")`)



In order to run the python scripts in `lessons_follow_along_code`, you will need the following python modules installed:
  
  - pandas
  - numpy
  - seaborn
  - palmerpenguins
  - scipy
  - statsmodels
   
