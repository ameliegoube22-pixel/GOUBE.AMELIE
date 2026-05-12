# Fabre_Museum_Project

## Analysis of Children’s Movement, Spatial Exploration, and Interaction Behaviors in a Museum Environment

By Goubé Amélie *M2 Human Movement Science - MAM2ADMM Project*

---
## 1. Project Overview
This research project investigates children’s movement, spatial exploration, and interaction behaviors at the **Fabre Museum** (Montpellier). By analyzing observational data, we aim to understand how young visitors engage with artworks and navigate the museum environment.

* **Research Question**: How do children explore museum spaces and engage physically and socially with the environment?
* **Main Hypothesis**: Movement and interaction patterns differ significantly based on the gender of the children.

## 2. Methodology & Dimensions
The observational variables are grouped into **four theoretical dimensions**:
1. **Spatial Exploration**: Zones visited, distance travelled, movement autonomy.
2. **Engagement with Artwork**: Body orientation, postural adjustments, physical approach.
3. **Motor Engagement**: Overall physical activity and environmental interactions.
4. **Social Interactions**: Peer-to-peer and child-adult social dynamics.

### Data Pipeline
### Data Preprocessing (Python)
Execute the notebook: `GOUBE.Amelie.ipynb`
* **Process:** Cleaning of raw data, management of missing values (NAs), and dimensional categorization.
* **Outputs:** * Generates exploratory plots in the `/figures` folder.
    * Exports `data_clean.csv` to the `/data` folder for further analysis.

### Inferential Statistics (R)

Open the R Markdown: `GOUBE.amelie.Rmd`
* **Process:** Performs **Shapiro-Wilk** normality tests and **Wilcoxon** non-parametric comparisons.
* **Outputs:** * **7 Statistical Boxplots** (annotated with p-values and effect sizes) automatically saved in `/results/figures/`.
    * **Final Report:** Run "Knit" to produce the HTML synthesis (`GOUBE.amelie.html`).

## 3. Project Structure 
This repository follows this structure: 

```
GOUBE.AMELIE/
├── data/                  # Raw and cleaned datasets (data_clean.csv)
├── notebook/              # Working scripts and Python EDA
├── figures/               # Exploratory plots (Python/R)
├── results/               # FINAL OUTPUTS
│   └── figures/           # Automated statistical boxplots (R)
├── sources/               # References for Fabre project
├── GOUBE.Amelie.ipynb     # Python: Data cleaning & EDA
├── GOUBE.amelie.Rmd       # R: Statistical modeling & Hypothesis testing
├── GOUBE.amelie.html      # Exported final report
├── GOUBE.Amelie.Rproj     # RStudio project file
├── .gitignore             # Files excluded from version control
└── readme.md              # Project documentation
```
## 4.Technical prerequisites
Python Libraries: pandas, numpy, matplotlib, seaborn.

R Packages: tidyverse, rstatix, ggpubr.

## Scientific synthesis
Due to the small sample size and non-normal distribution of the data (confirmed by Shapiro-Wilk tests), we utilized the Wilcoxon Rank Sum Test.

Key Findings:
While several p-values exceed the 0.05 threshold due to limited power, the Effect Sizes (r) suggest moderate behavioral trends (r≈0.35). Specifically, postural adjustment and interaction with adults appear to vary between groups, though these results should be interpreted with caution and would benefit from a larger cohort study.


## 5. Sources 
# 1. Spatial and Material Engagement

Young children’s museum geographies: spatial, material and bodily ways of knowing

Target Population: 3-6 years old.

Methodology: Observation of movements, bodily interactions with space, and trajectory mapping.

Key Findings: Children construct knowledge through movement and bodily engagement; the body acts as a central mediator of the spatial experience in museums.

Relevance to Project: Validates variables such as distance travelled, number of movements, and body/space interaction.

Reference: Children's Geographies | DOI: 10.1080/14733285.2018.1497141

# 2. Psychomotor Space Utilization

L’utilisation de l’espace en psychomotricité

Target Population: 3-7 years old.

Methodology: Clinical observations of space occupation, spatial constructions, and material organization.

Key Findings: The bodily use of space reflects psychomotor development and the child's ability to appropriate an environment and build a physical identity.

Relevance to Project: Justifies metrics for space occupation, spatial organization, and motor engagement.

Reference: Enfances & Psy | DOI: 10.3917/ep.033.0104

# 3. Visiting Patterns and Rhythms

Expériences de visite de jeunes enfants accompagnés

Target Population: 3-6 years old.

Methodology: Observation of movements, stopping rhythms, and spatial grouping.

Key Findings: Rhythms of movement and stillness structure the spatial experience and define the level of engagement within the museum.

Relevance to Project: Supports the analysis of number of movements, stopping duration, and spatial exploration.

Reference: Culture & Musées | DOI: 10.4000/culturemusees.1996

# 4. Meaning Making through Movement

Zigging and zooming all over the place: Young children’s meaning making and movement in the museum

Target Population: 3-6 years old.

Methodology: Ethnographic observations of trajectories, body orientation, and spatial exploration.

Key Findings: "Zigging and zooming" (fluid movements) allow children to build meaning and appropriate the museum space in their own unique way.

Relevance to Project: Validates spatial trajectories, distance travelled, and body orientation towards artworks.

Reference: Journal of Early Childhood Literacy | DOI: 10.1177/1468798412453730
