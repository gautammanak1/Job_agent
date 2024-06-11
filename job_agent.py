import requests
import json
from uagents import Agent, Bureau, Context, Model
from uagents.network import wait_for_tx_to_complete
from uagents.setup import fund_agent_if_low

class JobDetailsRequest(Model):
    job_role: str
    rapidapi_key: str

class JobDetailsResponse(Model):
    details: str


alice = Agent(name="alice", seed="alice secret phrase")
bob = Agent(name="bob", seed="bob secret phrase")

fund_agent_if_low(bob.wallet.address())
fund_agent_if_low(alice.wallet.address())

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


@alice.on_interval(period=30.0)
async def request_job_details(ctx: Context):
    job_role = input("Enter the job role: ")
    rapidapi_key = ""  # cf5c0e8526mshf9862937a0971b1p1b74dfjsn0f328599cc88 (Api)
    details = get_job_details(job_role, rapidapi_key)
    await ctx.send(
        bob.address,
        JobDetailsRequest(
            job_role=job_role,
            rapidapi_key=rapidapi_key
        )
    )
    ctx.logger.info(f"Requested job details {job_role}: {details}")

@bob.on_message(model=JobDetailsRequest, replies=JobDetailsResponse)
async def fetch_job_details(ctx: Context, sender: str, msg: JobDetailsRequest):
    ctx.logger.info(f"Received job details request from {sender}")
    details = get_job_details(msg.job_role, msg.rapidapi_key)
    await ctx.send(
        alice.address,
        JobDetailsResponse(details=details)
    )
    ctx.logger.info(f"Fetched job details: {details}")

async def confirm_transaction(ctx: Context, sender: str, msg: JobDetailsRequest):
    ctx.logger.info(f"Received {sender}: {msg}")
    tx_resp = await wait_for_tx_to_complete(msg.tx_hash, ctx.ledger)
    coin_received = tx_resp.events["coin_received"]
    if (
        coin_received["receiver"] == str(ctx.wallet.address())
    ):
        ctx.logger.info(f"Job Find successful: {coin_received}")

bureau = Bureau()
bureau.add(alice)
bureau.add(bob)

if __name__ == "__main__":
    bureau.run()
