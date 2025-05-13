
# 📺 Candy Candy and the (Possible) Decline of "Susana"

This repository contains an exploratory data analysis investigating whether the 1980s anime *Candy Candy* influenced the decline in popularity of the name “Susana” in Spanish-speaking countries, primarily Spain and Uruguay.

## 📊 Objective


## 🔁 EDA Pipeline Overview

```mermaid
graph TD
    A[📂 Raw Data<br>INE & Montevideo CSVs] --> B[🧹 Clean & Aggregate<br>by Decade]
    B --> C[📊 Absolute Frequency<br>Spain & Uruguay]
    C --> D[📈 Relative Frequency<br>Within Each Country]
    D --> E[🖼️ Visualizations<br>(Seaborn)]
    E --> F[🧪 Chi-squared Test<br>Susana vs Patricia]
    F --> G[📝 Markdown Tables<br>for Docs & Blog]
    G --> H[🚀 Outputs:<br>Blog Infographic & GitHub Repo]
```


To examine whether the broadcast of *Candy Candy* had a cultural impact measurable through the frequency of the name “Susana,” using public datasets and comparative name trend analysis.

## 📁 Repository Structure

```
candy-names/
├── data/
│   ├── raw/           # Original downloaded datasets
│   └── processed/     # Cleaned and aggregated data by decade
├── outputs/
│   ├── plots/         # Generated visualizations (PNG)
│   └── tables/        # Final tables (CSV/XLSX)
├── scripts/           # Python scripts for data cleaning, analysis, and visualization
└── docs/              # Supplementary documentation
```

## 🧪 Reproducibility

To reproduce this analysis:

1. Clone this repository.
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Execute the scripts in `/scripts/` following the numerical order.

## 📚 Data Sources

- Instituto Nacional de Estadística (Spain): https://www.ine.es/widgets/nombrefrecuente/
- Civil Registry of Montevideo: https://ckan-data.montevideo.gub.uy/dataset/05609f8f-3141-4000-8d4c-ae3f698e0d9c/resource/6c40038a-4f49-4e9d-8bc6-f8ffa3f95363/download/nombre_nacim_x_anio_sexo.csv

## ✍️ Author

Blanca Vargas — [blancavg.com](https://blancavg.com/)
