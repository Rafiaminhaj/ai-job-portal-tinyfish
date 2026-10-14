"""
AI Job Portal Finder — Powered by TinyFish 🐟
Built by Rafia Minhaj for TinyBounties Drop 001
GitHub: github.com/Rafiaminhaj/ai-job-portal-tinyfish
"""

import os
import requests
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AI Job Portal Finder 🐟",
    description="Find internships and jobs from live career pages using TinyFish Search + Fetch APIs",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "your_api_key_here")
SEARCH_HEADERS = {"X-API-Key": TINYFISH_API_KEY}
FETCH_HEADERS = {
    "X-API-Key": TINYFISH_API_KEY,
    "Content-Type": "application/json"
}

# Correct TinyFish API endpoints
SEARCH_URL = "https://api.search.tinyfish.ai"
FETCH_URL = "https://api.fetch.tinyfish.ai"


def tinyfish_search(query: str, num_results: int = 10):
    """Search the live web using TinyFish Search API"""
    response = requests.get(
        SEARCH_URL,
        params={"query": query, "num_results": num_results},
        headers=SEARCH_HEADERS,
        timeout=15
    )
    if response.status_code == 200:
        return response.json()
    return {"error": f"Search failed: {response.status_code} - {response.text[:200]}", "results": []}


def tinyfish_fetch(urls):
    """Fetch full page content as clean markdown using TinyFish Fetch API"""
    if isinstance(urls, str):
        urls = [urls]
    response = requests.post(
        FETCH_URL,
        json={"urls": urls},
        headers=FETCH_HEADERS,
        timeout=20
    )
    if response.status_code == 200:
        return response.json()
    return {"error": f"Fetch failed: {response.status_code} - {response.text[:200]}"}


@app.get("/")
def home():
    return {
        "name": "AI Job Portal Finder 🐟",
        "powered_by": "TinyFish Search + Fetch APIs",
        "built_by": "Rafia Minhaj",
        "endpoints": {
            "/search-jobs": "Search live jobs by role + location",
            "/internships": "Find student internships by skill",
            "/job-details": "Get full job details from any URL",
            "/company-jobs": "Search jobs at a specific company",
            "/freshers": "Find fresher/entry-level jobs"
        }
    }


@app.get("/search-jobs")
def search_jobs(
    role: str = Query(..., description="Job role e.g. 'Python Developer'"),
    location: str = Query("India", description="Location e.g. 'Bangalore' or 'remote'"),
    type: str = Query("internship", description="'internship' or 'full-time'")
):
    """
    🔍 Search for jobs using TinyFish Search API
    Pulls live listings from LinkedIn, Internshala, Naukri, and more
    """
    query = f"{role} {type} {location} 2026 apply now"
    results = tinyfish_search(query, num_results=10)

    return {
        "role": role,
        "location": location,
        "type": type,
        "results": results,
        "tip": f"Use /job-details?url=<url> to get full description",
        "powered_by": "TinyFish Search API 🐟"
    }


@app.get("/internships")
def find_internships(
    skill: str = Query("python", description="Your skill e.g. 'python', 'java', 'ML'"),
    location: str = Query("remote", description="Location preference"),
    stipend: bool = Query(True, description="Only paid internships?")
):
    """
    🎓 Find student internships using TinyFish Search API
    Perfect for students actively job hunting!
    """
    paid_filter = "stipend paid" if stipend else ""
    query = f"{skill} internship for students {location} {paid_filter} 2026"
    results = tinyfish_search(query, num_results=10)

    return {
        "skill": skill,
        "location": location,
        "paid_only": stipend,
        "internships": results,
        "powered_by": "TinyFish Search API 🐟"
    }


@app.get("/job-details")
def get_job_details(
    url: str = Query(..., description="Full URL of the job posting")
):
    """
    📄 Fetch full job description from any careers page
    Uses TinyFish Fetch API to extract clean readable content
    """
    details = tinyfish_fetch(url)
    return {
        "url": url,
        "job_details": details,
        "powered_by": "TinyFish Fetch API 🐟"
    }


@app.get("/company-jobs")
def search_company_jobs(
    company: str = Query(..., description="Company name e.g. 'Google', 'Flipkart'"),
    role: str = Query("software engineer", description="Role to search for")
):
    """
    🏢 Search jobs at a specific company using TinyFish Search API
    """
    query = f"{role} jobs at {company} 2026 careers apply"
    results = tinyfish_search(query, num_results=8)

    # Also fetch company careers page
    careers_query = f"{company} careers page jobs site:{company.lower().replace(' ', '')}.com"
    page_results = tinyfish_search(careers_query, num_results=3)

    return {
        "company": company,
        "role": role,
        "job_listings": results,
        "careers_pages": page_results,
        "powered_by": "TinyFish Search + Fetch APIs 🐟"
    }


@app.get("/freshers")
def find_fresher_jobs(
    domain: str = Query("software", description="Domain: 'software', 'AI', 'data science'"),
    location: str = Query("India", description="Location")
):
    """
    🎯 Find fresher/entry-level jobs for new graduates
    Uses TinyFish Search API for live 2026 listings
    """
    query = f"fresher {domain} engineer jobs {location} 0-1 years experience 2026"
    results = tinyfish_search(query, num_results=10)

    # Also search for specific job boards
    naukri_query = f"fresher {domain} jobs site:naukri.com 2026"
    naukri_results = tinyfish_search(naukri_query, num_results=5)

    return {
        "domain": domain,
        "location": location,
        "fresher_jobs": results,
        "naukri_listings": naukri_results,
        "powered_by": "TinyFish Search API 🐟"
    }
