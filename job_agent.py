import requests
from pydantic import Field
from uagents import Agent, Context, Protocol, Model
from ai_engine import UAgentResponse, UAgentResponseType

# Define the JobProtocol class extending Protocol
class JobProtocol(Protocol):
    pass

# Create an instance of JobProtocol
job_protocol = JobProtocol(name="job_protocol")

class JobRequest(Model):
    job_description: str = Field(description="Give details of job you are looking for")

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
        return response.json()  # Change to response.json() to properly handle the JSON response
    else:
        return {"error": response.status_code, "message": response.text}

agent = Agent(name="Job Finder Agent")
print(f"Your agent's address is: {agent.address}")

# Hardcoded values for job role and RapidAPI key
job_role = "Software Engineer"
rapidapi_key = "cf5c0e8526mshf9862937a0971b1p1b74dfjsn0f328599cc88"  # Replace with your actual RapidAPI key

@job_protocol.on_message(model=JobRequest, replies={UAgentResponse})
async def load_job(ctx: Context, sender: str, msg: JobRequest):
    ctx.logger.info(f"Received job request: {msg.job_description}")
    details = get_job_details(msg.job_description, rapidapi_key)
    ctx.logger.info(f"Job details for {msg.job_description}: {details}")

    if "error" in details:
        message = f"Error {details['error']}: {details['message']}"
    else:
        # Format the job details into a readable format
        jobs = details.get("jobs", [])
        if jobs:
            message = "Job listings:\n" + "\n".join([f"{job['title']} - {job['company']}" for job in jobs])
        else:
            message = "No job listings found."

    await ctx.send(
        sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
    )

# Include the protocol in the agent
agent.include(job_protocol, publish_manifest=True)

# Run the agent
if __name__ == "__main__":
    agent.run()
