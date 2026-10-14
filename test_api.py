import requests

API_KEY = "sk-tinyfish-LbLJmwRu6Py7VlvyvPmA6-XdQT8B1l_o"
BASE = "https://api.search.tinyfish.ai"
QUERY = "python internship India 2026"

tests = [
    ("Bearer header", {"Authorization": f"Bearer {API_KEY}"}, {}),
    ("X-API-Key header", {"X-API-Key": API_KEY}, {}),
    ("api_key param", {}, {"api_key": API_KEY}),
    ("key param", {}, {"key": API_KEY}),
]

for name, headers, extra_params in tests:
    try:
        r = requests.get(BASE, params={"query": QUERY, **extra_params}, headers=headers, timeout=12)
        print(f"{name}: {r.status_code} | {r.text[:100]}")
    except Exception as e:
        print(f"{name}: ERROR - {e}")
