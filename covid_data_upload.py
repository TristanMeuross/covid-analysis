
import sqlite3
import pandas as pd

from modules.my_modules import upload_gsheets

conn = sqlite3.connect('covid.db')
c = conn.cursor()

QUERY = """
SELECT
    dea.continent,
	dea.location,
	dea.date,
	dea.population,
	dea.total_cases,
	dea.new_cases,
	AVG(dea.new_cases)
	  OVER(
	    PARTITION BY dea.location
	    ORDER BY dea.date
	    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
		) AS new_cases_ma,
	AVG((dea.new_cases/dea.population)*1000000)
	  OVER(
	    PARTITION BY dea.location
	    ORDER BY dea.date
	    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
		) AS new_cases_million_ma,
	dea.total_deaths,
	dea.new_deaths,
	AVG(CAST(dea.new_deaths AS FLOAT))
	  OVER(
	    PARTITION BY dea.location
	    ORDER BY dea.date
	    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
		) AS new_deaths_ma,
    AVG((CAST(new_deaths AS FLOAT)/dea.population)*1000000)
	  OVER(
	    PARTITION BY dea.location
		ORDER BY dea.date
		ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
		) AS new_deaths_million_ma,
	vac.people_vaccinated/dea.population AS vaccinated_percentage,
	vac.people_fully_vaccinated/dea.population AS fully_vaccinated_percentage
FROM CovidDeaths dea
JOIN CovidVaccinations vac
    ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY dea.location, dea.date
"""

covid_summary_df = pd.read_sql_query(QUERY, conn)
covid_summary_df['date'] = pd.to_datetime(
    covid_summary_df['date'],
    format='%Y/%m/%d'
)

covid_summary_africa_df = covid_summary_df.loc[covid_summary_df['continent'] == 'Africa']
covid_summary_asia_df = covid_summary_df.loc[covid_summary_df['continent'] == 'Asia']
covid_summary_europe_df = covid_summary_df.loc[covid_summary_df['continent'] == 'Europe']
covid_summary_north_america_df = covid_summary_df.loc[
    covid_summary_df['continent'] == 'North America']
covid_summary_oceania_df = covid_summary_df.loc[covid_summary_df['continent'] == 'Oceania']
covid_summary_south_america_df = covid_summary_df.loc[
    covid_summary_df['continent'] == 'South America']


upload_gsheets(
    'covid-summary-africa',
    [covid_summary_africa_df],
    sheets=[0]
)
upload_gsheets(
    'covid-summary-asia',
    [covid_summary_asia_df],
    sheets=[0]
)
upload_gsheets(
    'covid-summary-europe',
    [covid_summary_europe_df],
    sheets=[0]
)
upload_gsheets(
    'covid-summary-north-america',
    [covid_summary_north_america_df],
    sheets=[0]
)
upload_gsheets(
    'covid-summary-oceania',
    [covid_summary_oceania_df],
    sheets=[0]
)
upload_gsheets(
    'covid-summary-south-america',
    [covid_summary_south_america_df],
    sheets=[0]
)

conn.close()
