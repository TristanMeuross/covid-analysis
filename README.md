# COVID-19 Data Exploration
This project explores COVID-19 data and visualizes it through a Tableau dashboard.

## Why?
A project to show my ability to explore data with sql and create an engaging visualisation from it. In addition, it aims to answer the following questions:
- Which countries have experienced the COVID-19 pandemic the worst?
- Which countries are receiving the most vaccinations relative to their population?
- How has global/country cases and deaths tracked since the start of the pandemic?

## How?
- COVID-19 data was sourced from ourworldindata.org/coronavirus and split into a covid cases/deaths file ([covid-deaths.xlsx](data_files/covid-deaths.xlsx)) and vaccinations file ([vaccinations.xlsx](data_files/covid-vaccinations.xlsx))
- Data files were uploaded to Microsoft SQL Server 2019 and analysed in the management tool ([data_exploration.sql](data_exploration.sql))
- Exploratory dataset was extracted to an excel file for visualization in Tableau
- [COVID-19 dashboard](https://public.tableau.com/views/GlobalCOVID-19CasesDeathsandVaccinationsTracker/Dashboard1?:language=en-GB&:display_count=n&:origin=viz_share_link) was created, highlighting global cases, deaths and vaccination rates

## Sources
- Hannah Ritchie, Edouard Mathieu, Lucas Rodés-Guirao, Cameron Appel, Charlie Giattino, Esteban Ortiz-Ospina, Joe Hasell, Bobbie Macdonald, Diana Beltekian and Max Roser (2020) - "Coronavirus Pandemic (COVID-19)". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]
