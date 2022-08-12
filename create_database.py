
import sqlite3

conn = sqlite3.connect('covid.db')
c = conn.cursor()

c.execute("""CREATE TABLE CovidDeaths (
            iso_code INTEGER,
            continent TEXT,
            location TEXT,
            date TEXT,
            population INTEGER,
            total_cases INTEGER,
            new_cases INTEGER,
            new_cases_smoothed INTEGER,
            total_deaths INTEGER,
            new_deaths INTEGER,
            new_deaths_smoothed INTEGER,
            total_cases_per_million REAL,
            new_cases_per_million REAL,
            new_cases_smoothed_per_million REAL,
            total_deaths_per_million REAL,
            new_deaths_per_million REAL,
            new_deaths_smoothed_per_million REAL,
            reproduction_rate REAL,
            icu_patients INTEGER,
            icu_patients_per_million REAL,
            hosp_patients INTEGER,
            hosp_patients_per_million REAL,
            weekly_icu_admissions INTEGER,
            weekly_icu_admissions_per_million REAL,
            weekly_hosp_admissions INTEGER,
            weekly_hosp_admissions_per_million REAL
)""")

c.execute("""CREATE TABLE CovidVaccinations (
            iso_code INTEGER,
            continent TEXT,
            location TEXT,
            date TEXT,
            total_tests INTEGER,
            new_tests INTEGER,
            total_tests_per_thousand REAL,
            new_tests_per_thousand REAL,
            new_tests_smoothed INTEGER,
            new_tests_smoothed_per_thousand REAL,
            positive_rate REAL,
            tests_per_case REAL,
            tests_units INTEGER,
            total_vaccinations INTEGER,
            people_vaccinated INTEGER,
            people_fully_vaccinated INTEGER,
            total_boosters INTEGER,
            new_vaccinations INTEGER,
            new_vaccinations_smoothed INTEGER,
            total_vaccinations_per_hundred REAL,
            people_vaccinated_per_hundred REAL,
            people_fully_vaccinated_per_hundred REAL,
            total_boosters_per_hundred REAL,
            new_vaccinations_smoothed_per_million REAL,
            new_people_vaccinated_smoothed INTEGER,
            new_people_vaccinated_smoothed_per_hundred REAL,
            stringency_index REAL,
            population INTEGER,
            population_density REAL,
            median_age REAL,
            aged_65_older INTEGER,
            aged_70_older INTEGER,
            gdp_per_capita REAL,
            extreme_poverty REAL,
            cardiovasc_death_rate REAL,
            diabetes_prevalence REAL,
            female_smokers REAL,
            male_smokers REAL,
            handwashing_facilities REAL,
            hospital_beds_per_thousand REAL,
            life_expectancy REAL,
            human_development_index REAL
)""")

conn.commit()

conn.close()
