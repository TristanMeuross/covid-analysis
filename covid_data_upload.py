
import sqlite3
import pandas as pd

from modules.my_modules import upload_gsheets, format_gsheets

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
    covid_summary_df['date'], format='%Y/%m/%d')

WORKBOOK_NAME = 'covid-summary'
upload_gsheets(
    WORKBOOK_NAME,
    [covid_summary_df],
    sheets=[0]
)

format_gsheets(
    WORKBOOK_NAME,
    'G:H',
    'NUMBER',
    '0.00',
    sheets=[0]
)

format_gsheets(
    WORKBOOK_NAME,
    'K:L',
    'NUMBER',
    '0.00',
    sheets=[0]
)

format_gsheets(
    WORKBOOK_NAME,
    'M:N',
    'NUMBER',
    '0.00',
    sheets=[0]
)

conn.close()
