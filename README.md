# 🐟 AI Job Portal Finder — Powered by TinyFish

> **Find internships and real jobs from live career pages using TinyFish Search + Fetch APIs**
> Built by [Rafia Minhaj](https://github.com/Rafiaminhaj) for TinyBounties Drop 001

---

## 🎯 What it does

As a student who applies for internships every week, I built the tool I always wanted:

- 🔍 **Search live job listings** from LinkedIn, Internshala, Naukri, and more
- 📄 **Fetch full job details** from any careers page — clean and readable
- 🎓 **Filter by role, skill, location** (internship / full-time / fresher)
- 🏢 **Search at specific companies** — find exact openings at your dream company
- 🆕 **Fresher-specific search** — 0-1 year experience jobs for new graduates

---

## 🐟 TinyFish APIs Used

| API | Usage |
|-----|-------|
| **TinyFish Search API** | Find live job listings from across the web |
| **TinyFish Fetch API** | Extract full job descriptions from career pages |

Both APIs do real work — no canned answers, no static data. Every result is live.

---

## 🚀 Run Locally

```bash
# Clone
git clone https://github.com/Rafiaminhaj/ai-job-portal-tinyfish
cd ai-job-portal-tinyfish

# Install dependencies
pip install -r requirements.txt

# Set your API key
cp .env.example .env
# Edit .env and add your TinyFish API key

# Run
uvicorn main:app --reload
```

Open: http://localhost:8000/docs

---

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Overview + all endpoints |
| `GET /search-jobs` | Search jobs by role + location |
| `GET /internships` | Find student internships by skill |
| `GET /job-details` | Get full job description from any URL |
| `GET /company-jobs` | Search jobs at a specific company |
| `GET /freshers` | Find fresher/entry-level jobs |

---

## 💡 Example Requests

```bash
# Find Python internships remote
curl "http://localhost:8000/internships?skill=python&location=remote"

# Find ML jobs in Bangalore
curl "http://localhost:8000/search-jobs?role=machine+learning&location=Bangalore"

# Get job details from specific posting
curl "http://localhost:8000/job-details?url=https://careers.google.com/jobs/..."

# Find jobs at Flipkart
curl "http://localhost:8000/company-jobs?company=Flipkart&role=SDE"

# Fresher AI jobs in India
curl "http://localhost:8000/freshers?domain=AI&location=India"
```

---

## 🛠️ Tech Stack

- **Backend**: Python + FastAPI
- **Web Intelligence**: TinyFish Search API + Fetch API
- **Deployment**: Render / Railway
- **Built for**: Students actively job hunting in 2026

---

## 👩‍💻 Built By

**Rafia Minhaj** — Final Year B.Tech CSE @ CIT Ranchi

- 🏆 GSSoC 2026 — Top 0.8% Globally (#29)
- 🔧 Open Source Maintainer — DevPulse AI
- 🌍 Hacktoberfest 2026 Contributor

[![GitHub](https://img.shields.io/badge/GitHub-Rafiaminhaj-black?logo=github)](https://github.com/Rafiaminhaj)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rafia_Minhaj-blue?logo=linkedin)](https://www.linkedin.com/in/rafia-minhaj-69317b308/)

---

*Built with 🐟 TinyFish | TinyBounties Drop 001 Submission*
