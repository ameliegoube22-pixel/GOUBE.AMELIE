# Fabre-Museum-Project

## Analysis of Children’s Movement, Spatial Exploration, and Interaction Behaviors in a Museum Environment

By Goubé Amélie *M2 Human Movement Science - MAM2ADMM Project*

---

This project presents an observational analysis of children’s movement and spatial behaviors in a museum environment, with a particular focus on motor engagement, exploration of space, and interactions with artworks and the environment.

## 1.1 Context

Museums are increasingly considered as environments that support children’s sensory, cognitive, social, and motor development. Beyond learning outcomes, museum visits involve bodily engagement with space, movement through exhibition areas, and interactions with peers, adults, and artworks.

Research in developmental psychology and museum studies suggests that children’s movement patterns and spatial exploration may reflect their level of engagement, autonomy, curiosity, and interaction with the environment.

However, observational data collected in museum settings are often complex and multidimensional, requiring structured preprocessing and exploratory analyses before statistical interpretation.

The present project aims to explore observational indicators related to movement, spatial exploration, and environmental engagement in children observed during museum visits.

### 1.2 Research Objectives
* **Main Objective**: To analyze children’s movement and interaction behaviors in a museum setting using observational data.
* **Research Question**: How do children explore museum spaces and engage physically and socially with the environment during observation sessions?
* **Hypothesis**: Movement and exploration patterns may differ based on the gender of the children.

---

## 2. Scientific Dimensions

The observational indicators are grouped into four theoretical dimensions:
* **Spatial Exploration**: Number of zones visited, distance travelled, and movement autonomy.
* **Engagement with Artwork**: Body orientation, postural adjustments, and physical approach.
* **Motor Engagement**: Overall physical activity and environmental interactions.
* **Social Interactions**: Peer-to-peer and child-adult social dynamics.

---

## 2. Project Architecture (Safe Structure)
The project follows a rigorous structure to ensure the reproducibility of the analysis:

* **data/**: Contains the source data (`data_observation.csv`) and the processed dataset (`data_clean.csv`).
* **results/**: Automatic exports of statistical tables and graphical visualizations (Heatmaps, mean scores).
* **figures/**: (Optional) Additional exploratory analysis plots.
* **GOUBE_Amelie_Analysis.ipynb**: Python Notebook dedicated to cleaning, dimensional structuring, and initial descriptive analysis.
* **Analysis_Script.R**: R script dedicated to inferential statistical testing (ANOVA, T-Tests).
* **README.md**: General project documentation.

---

## 3. Methodology (Python Pipeline)

The pre-processing phase was conducted using Python (Pandas/Seaborn) with the following objectives:

1.  **Data Standardization**: Cleaning variable names (snake_case format), handling missing values (NA), and harmonizing data types.
2.  **Dimensional Analysis**: Categorizing the 15+ raw observation variables into 4 conceptual dimensions:
    * *Spatial Exploration* (e.g., zones explored, movement autonomy).
    * *Engagement with Artwork* (e.g., posture, visual orientation).
    * *Motor Engagement* (e.g., physical interaction with the environment).
    * *Social Interactions* (e.g., exchanges with peers or adults).
3.  **Exploratory Data Analysis (EDA)**: Calculating mean scores by gender and generating a correlation matrix to identify behavioral patterns.

---

## 3. Project Structure

This project follows the **"Safe Project Logic"** for reproducible science:

```text
MAM2ADMM/Fabre_Museum_Project/
├── data/               # Original and cleaned datasets
│   ├── data_observation.csv    # Raw data
│   └── data_clean.csv          # Cleaned data exported from Python
├── results/figures            # Visualizations and exported figures
├── memoire_musee.ipynb          # Python entry point: Cleaning, EDA & Export
├── memoire_musee.Rmd            # R entry point: Normality tests & Statistics
├── memoire_musee.Rproj          # RStudio project file
└── readme.md           # Project documentation
---

