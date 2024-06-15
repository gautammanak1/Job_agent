import os
import sys
from pydantic import Field
import requests
from ai_engine import UAgentResponse, UAgentResponseType
from uagents import Agent, Context, Protocol, Model
from uagents.setup import fund_agent_if_low

# Pydantic model for JobRequest
class JobRequest(Model):
    job_description: str = Field(description="Give details of job you are looking for")

# Function to get job details from Indeed API
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

    response = requests.post(url, json=payload, headers=headers)
    print(f"API Response Status Code: {response.status_code}")  # Log status code
    print(f"API Response Text: {response.text}")  # Log raw response text

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

# Define the job role and RapidAPI key
job_role = "Software Engineer"
rapidapi_key = ""  # Replace with your actual RapidAPI key  cf5c0e8526mshf9862937a0971b1p1b74dfjsn0f328599cc88

# Create the agent
agent = Agent(name="Job Finder Agent")
print(f"Your agent's address is: {agent.address}")



# Define the protocol
job_protocol = Protocol("Job Finder Protocol")

# Define the handler for the JobRequest message
@job_protocol.on_message(model=JobRequest, replies={UAgentResponse})
async def load_job(ctx: Context, sender: str, msg: JobRequest):
    ctx.logger.info(f"Received job request: {msg.job_description}")
    details = get_job_details(job_role, rapidapi_key)
    ctx.logger.info(f"Job details for {job_role}: {details}")

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
