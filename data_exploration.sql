
-- EXPLORING THE DATA

-- Selecting all data

SELECT *
FROM SQLExploration.dbo.CovidVaccinations
ORDER BY location, date

SELECT *
FROM SQLExploration.dbo.CovidDeaths
ORDER BY location, date

-- Looking at total cases and new cases vs population

SELECT 
    location, 
    date,
    total_cases,
    new_cases,
    population,
    ROUND((total_cases/population)*100, 2) AS percentage_cases,
    ROUND(
	  AVG((new_cases/population)*1000000)
	  OVER(
	    PARTITION BY location
		ORDER BY date
		ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
		), 2
	  ) AS new_cases_million_ma
FROM SQLExploration.dbo.CovidDeaths
WHERE continent IS NOT NULL
ORDER BY date

-- View highest current proportion of cases to population

SELECT 
    location, 
    MAX(total_cases) AS total_current_cases,
    population,
    ROUND((MAX(total_cases)/population)*100, 2) AS highest_percentage_cases
FROM SQLExploration.dbo.CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY highest_percentage_cases DESC

-- Looking at total cases vs total deaths and likelihood of death

SELECT 
    location,
	date,
	total_cases,
	total_deaths,
	(total_deaths/total_cases)*100 AS death_percentage
FROM SQLExploration.dbo.CovidDeaths
ORDER BY location, date

-- Look at highest number of deaths per population at country level
 
SELECT 
    location, 
    MAX(cast(total_deaths AS int)) AS total_current_deaths,
    population
FROM SQLExploration.dbo.CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY total_current_deaths DESC

-- Look at highest number of deaths per population at continent level
 
SELECT 
    location,
    MAX(cast(total_deaths AS int)) AS total_current_deaths
FROM SQLExploration.dbo.CovidDeaths
WHERE continent IS NULL
	AND location IN (
			SELECT continent
			FROM SQLExploration.dbo.CovidDeaths
			WHERE continent IS NOT NULL
			GROUP BY continent
			)
GROUP BY location
ORDER BY total_current_deaths DESC

-- Looking at total population vs vaccinations

SELECT
    dea.continent,
	dea.location,
	dea.date,
	dea.population,
	vac.people_fully_vaccinated,
	(vac.people_fully_vaccinated / dea.population) AS fully_vaccinated_percentage
FROM SQLExploration.dbo.CovidDeaths dea
JOIN SQLExploration.dbo.CovidVaccinations vac
    ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY dea.location, dea.date


-- SETTING UP VIZ DATA

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
FROM SQLExploration.dbo.CovidDeaths dea
JOIN SQLExploration.dbo.CovidVaccinations vac
    ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY dea.location, dea.date


