import requests
import json

# SAIF-Protocol Agent Scout v1.0
# TARGET: Identify AI Agents for Standard Adoption

def scout_agents():
    # Searching for 'ai-agents' topic repositories updated recently
    url = "https://api.github.com/search/repositories?q=topic:ai-agents&sort=updated&order=desc"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    
    print("📡 SAIF-Scout: Searching for new AI Agents...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()['items']
        for repo in repos[:5]:  # Focusing on the Top 5 trending
            name = repo['full_name']
            stars = repo['stargazers_count']
            link = repo['html_url']
            
            print(f"\n🚀 FOUND: {name} ({stars} stars)")
            print(f"🔗 URL: {link}")
            print(f"💡 ACTION: Tag developer in SAIF-Protocol Manifesto")
    else:
        print("❌ Error connecting to GitHub API. Check connection.")

if __name__ == "__main__":
    scout_agents()
