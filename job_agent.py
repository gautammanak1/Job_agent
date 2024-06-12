import requests
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class JobDetailsRequest(Model):
    job_role: str
    rapidapi_key: str

class JobDetailsResponse(Model):
    details: str

agent = Agent(name="job_agent", seed="job_agent_secret_phrase")

fund_agent_if_low(agent.wallet.address())

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

@agent.on_interval(period=30.0)
async def request_job_details(ctx: Context):
    job_role = input("Enter the job role: ")
    rapidapi_key = "cf5c0e8526mshf9862937a0971b1p1b74dfjsn0f328599cc88"  # Add your RapidAPI key here
    details = get_job_details(job_role, rapidapi_key)
    ctx.logger.info(f"Job details for {job_role}: {details}")

if __name__ == "__main__":
    agent.run()
