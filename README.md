# candy-names-impact

Exploratory data analysis on the cultural impact of media on name trends, using *Candy Candy* and the name "Susana" as a case study.

## 🎯 Objective

We explore whether the 1980s anime *Candy Candy* had a cultural impact measurable in the popularity of the name **"Susana"**. Using open name frequency datasets from Spain and Uruguay, the project explores name frequency trends, cultural context, visualizations, and statistical validation.

## 🔁 EDA Pipeline Overview

```mermaid
graph TD
    A[Raw Data\nINE & Montevideo CSVs] --> B[Clean & Aggregate\nby Decade]
    B --> C[Absolute Frequency\nSpain & Uruguay]
    C --> D[Relative Frequency\nWithin Each Country]
    D --> E[Visualizations\n(Seaborn)]
    E --> F[Chi-squared Test\nSusana vs Patricia]
    F --> G[Markdown Tables\nfor Docs & Blog]
    G --> H[Outputs:\nBlog Infographic & GitHub Repo]
```

## 📘 Notebook Preview

You can explore the summary notebook [here](./Candy_Candy_EDA_Report.ipynb) for a visual and reproducible walkthrough of the analysis.

[![Open in GitHub](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](./Candy_Candy_EDA_Report.ipynb)
