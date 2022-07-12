# Session Outlines

# Session 1
## What is Data Privacy?
  - Data Privacy vs Confidentiality
  - Utility vs Privacy tradeoff
## Why is Data Privacy Important? 
  - Reidentification/record linkage attacks are dangerous and should be limited
    (with examples)
  - Possibilty of increased access to tax data, health data and other formerly confidential datasets
  - Better/more equitable analyses, particularly for subgroups and rural populations
## Overview of SDC field
  - Traditional methods include swapping, noise infusion, suppression, generalization, sampling, and synthetic data
    - In depth definitions of synthetic data, and full vs partial and parametric vs non parametric synthesis
  - Formally Private methods include DP and approximate DP (quick overview of DP, but not in depth)   
  - Difference between Traditional methods and formally private methods is defining the threat model
## Data Privacy Workflow (from Claire's images)
  - Determine thresholds for disclosure risks and Utility
  - Remove PIIs
  - Select variables for anonymization
  - Develop SDC method based on disclosure risks
  - Evaluate data utility
  - Publish final data and statistics
## Additional Definitions
    - Disclosure Risks (identity, attribute, and inferential risks)
    - Utility measures (General vs specific utility)
    
# Session 2
## Overview of Synthetic Data
  - Mathematical definitions
  - Full vs partial synthesis, with examples
  - Connection to multiple imputation approaches
  - Overview of sequential synthesis
## How do we generate synthetic data?
  - Parametric data synthesis
    - data generation based from a parametric distribution or generative model
    - Can be either prob distributions, models, marginal table sampling, or Bayesian frameworks
  - Non Parametric data synthesis
    - data generation based from an empirical distribution
## Code example generating partially synthetic data with starwars data
  - Generate synth data with marginal table sampling, prob distributions, and regression models
## Code example of sequentially generating fully synthetic data with starwars data
  


# Session 3
## Measuring General utility 
  - First 4 moments, correlation fit, pMSE, Specks
## Measuring Specific utility
  - CI overlaps 
  - Any BEA specific utility metrics
## Measuring disclosure risk (need some more meat here...)
## Code example of calculating several utility measures with starwars data
## Synthetic Data Applications in the Wild
  - ACS Group Quarters, SIPP, SCF, SynPUF, MLDS, Synth Data Server at Cornell

# Session 4

## Interactive vs. Non-Interactive Sanitizer
- definitions (with images from Claire)
- how much noise should be added/how much should queries be limited?

## Motivation
- formal, mathematical definition of privacy
- allows researchers to quantify and adjust the privacy-utility tradeoff
- differential vs formal privacy (\*\*ask - what *is* the difference)
- strong guarantees (so strong it may perturb data more than we would like)

## Privacy Loss Budget
- differential privacy is a statement about the method rather than the data
- uses the idea of a privacy loss "budget" (defined mathematically as e); this budget quantifies the amount of information leaked with each released statistic, data, or query result
  - budget is selected before release of data, query result, or statistic
  - quantifies privacy-utility tradeoff (larger e = more accuracy, but less privacy; smaller e = less accuracy, but more privacy)
  - extreme cases: e = 0, e = infinity
- who sets the budget? still open question
  - implications for researchers/policymakers

## Features
- sacrifices intuition/produces potentially messier data in exchange for > privacy protection
- does not make predictions about how an attack will occur or the external attack an actor has access to
- assumes worst-case scenario (actor has information on every observation except one, unlimited computational power, the missing individual is the most extreme possible) 
  - Bezos example w/ income
- requires the data steward(s) to determine an appropriate privacy loss budget (will discuss "how" later)

## Mathematical Definition of DP
- formal equation definition here
- walk through each element of the equation
- use graphics from Claire's slides to explain the "difference of 1"
- include epsilon definition for now

# Session 5
## Refreshers
- privacy loss budget: larger privacy loss budget means the data is less private, but more accurate to the original values 
- definition of differential privacy (mathematical)

## Global vs Local Sensitivity
- sensitivity: how robust or resistant analysis is to being influenced by outliers
- Global
  - L1
  - L2
- Local
  - data dependent and not formally private
- this may fit better in the "details" class

## Example with Laplace Sanitizer
- define laplace distribution (with graphics) and normal distribution
- demonstrate application for differential privacy

## Other Fundamental Mechanisms
- Gaussian mechanism (define/demonstrate)
- Exponential mechanism (define/demonstrate)

## Composition Theorems
- Sequential
- Parallel

## Other Theorems
- database reconstruction
- post-processing
- move these? as appropriate

## Approximate Differential Privacy
- formal epsilon + delta definition
- other examples of relaxation of diff privacy definition - probabilistic differential privacy

# Session 6
## Common applications and challenges 
- counts
- means
- order statistics

## Case Studies - Reading
- discuss assigned reading here

## Case Studies - Other
- 2020 Decennial Census
- Census Bureau's on the Map
- Netflix
- Google COVID mobility
- NIST DP Synthetic Data Challenge

## Special Case
- differentially private synthetic data
  - if we haven't discussed parametric vs non parametric, do it here
    - parametric: probability distributions, models, bayesian framework

## Implications for Future Analysis
- e budgets originally conceived with budget near 1; now much higher
  - how to define e budgets?
- more applied research needed
