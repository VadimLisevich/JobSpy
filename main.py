from jobspy import scrape_jobs
import pandas as pd

jobs = scrape_jobs(
    site_name=["linkedin", "indeed"],
    search_term="project manager",
    location="Lisbon, Portugal",
    results_wanted=20,
    hours_old=24,
    country_indeed="PT"
)

print(f"Found {len(jobs)} jobs")
jobs.to_csv("jobs.csv", index=False)
