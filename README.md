# Job Agent

This project sets up a single agent that periodically requests job details from the Indeed API using RapidAPI. The agent prompts the user for a job role and retrieves job details based on the provided role.

## Prerequisites

- Python 3.6 or higher
- RapidAPI account and subscription to the Indeed API
- Installed Python packages: `requests`, `uagents`

## Installation

1. **Clone the repository** (or download the script directly):
   ```sh
   git clone https://github.com/yourusername/job-agent.git
   cd job-agent


## Install the required Python packages

```sh
pip install uagents

```
## Setup
1. **Subscribe to the Indeed API on RapidAPI:**

- Go to RapidAPI.
- Search for the Indeed API.
- Subscribe to the API and get your API key.
  
2.**Update the Script with Your API Key 🔑 :**

- Open the job_agent.py file.
- Find the line where rapidapi_key is defined and add your RapidAPI key

```sh
rapidapi_key = "your_rapidapi_key_here"  # Add your RapidAPI key here

```

## Usage

### Run the Script:

```sh
python job_agent.py
```

## Enter the Job Role:

When prompted, enter the job role you want to search for (e.g., Web Developer).

## View Job Details:

The agent will fetch and log the job details for the specified role.

# Project Structure

## job-agent/
- `job_agent.py`: The main script that sets up and runs the agent.
- `README.md`: This readme file.

## Description
`job_agent.py` is the main script responsible for setting up and running the agent. This project is licensed under the MIT License.

## Instructions
Save this content to a file named `README.md` in the same directory as your `job_agent.py` script. This file provides clear instructions and information about the project, helping others understand how to set it up and use it effectively.
## License

This project is licensed under the MIT License. 

For any inquiries or support, feel free to reach out to [gautammanak1@gmail.com](mailto:gautammanak1@gmail.com).



