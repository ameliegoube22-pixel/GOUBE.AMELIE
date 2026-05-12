# Fabre-Museum-Project

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
* **Step 1 (Python)**: Data cleaning, handling missing values, dimensional grouping, and Exploratory Data Analysis (EDA).
* **Step 2 (R)**: Inferential statistics (Normality tests, ANOVA, T-Tests) to validate the research hypotheses.

## 3. Project Structure (Safe Project Logic)
This repository follows the **Safe Project** standards for reproducible science:

```text
ameliegoube22-pixel/
├── data/                  # Original and cleaned datasets (data_clean.csv)
├── figures/               # Exploratory plots and visual assets
├── results/               # Statistical tables and exported analysis outputs
├── GOUBE.Amelie.ipynb     # Python: Data cleaning, EDA & Export
├── GOUBE.amelie.Rmd       # R: Statistical modeling & Hypothesis testing
├── GOUBE.amelie.html      # Exported report of the R analysis
├── GOUBE.Amelie.Rproj     # RStudio project file
├── .gitignore             # Files excluded from version control
└── readme.md              # Project documentation

