import requests
from uagents import Agent, Context, Model

class JobDetailsRequest(Model):
    job_role: str
    rapidapi_key: str

class JobDetailsResponse(Model):
    details: str

# Use the preloaded agent instance
agent = Agent()  # Initialize without name and seed, assuming the preloaded instance is used

# Function to get job details from the API
def get_job_details(job_role, rapidapi_key):
    url = "https://indeed11.p.rapidapi.com/"
    payload = {
        "search_terms": job_role,
        "location": "United States",
        "page": "1"
    }
    headers = {
        'x-rapidapi-key': rapidapi_key,
        'x-rapidapi-host': "indeed11.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code} - {response.text}"

# Hardcoded values for job role and RapidAPI key
job_role = "Software Engineer"
rapidapi_key = ""    # Replace with your actual RapidAPI key   cf5c0e8526mshf9862937a0971b1p1b74dfjsn0f328599cc88 

# Interval task to request job details
@agent.on_interval(period=30.0)
async def request_job_details(ctx: Context):
    details = get_job_details(job_role, rapidapi_key)
    ctx.logger.info(f"Job details for {job_role}: {details}")

# Run the agent
if __name__ == "__main__":
    agent.run()
