# Job Finder 

## Overview

The JJob Finder is a decentralized application (DApp) built using Python and the uAgents framework. It allows two agents, User1 and User2 , to exchange job details securely and efficiently using a decentralized network. This system utilizes RapidAPI to fetch job details based on user input.

## Features

- **Decentralized Communication**: Agents Alice and Bob communicate directly through a decentralized network, ensuring privacy and security.
- **Job Details Exchange**: Alice can request job details from Bob by specifying the job role, and Bob can respond with the relevant details.
- **API Integration**: The system integrates with the RapidAPI platform to fetch job details from external sources.
- **Transaction Confirmation**: Provides transaction confirmation functionality to ensure successful completion of transactions.

## Components

### Agents

- **Alice**: Initiates the request for job details.
- **Bob**: Receives the request from Alice and responds with the requested job details.

### Models

- **JobDetailsRequest**: Defines the structure of the message sent by Alice to request job details from Bob.
- **JobDetailsResponse**: Defines the structure of the message sent by Bob in response to Alice's request.

### Functions

- **get_job_details**: Makes an API call to fetch job details based on the provided job role and RapidAPI key.
- **request_job_details**: Initiates the process of requesting job details from Bob.
- **fetch_job_details**: Handles the request from Alice and fetches the job details from the API.


## Usage

1. Ensure Python and the required libraries are installed.
2. Run the script `job_details_exchange.py`.
3. Follow the prompts to input the job role.
4. Agents Alice and Bob will exchange messages, and job details will be fetched using the RapidAPI integration.

## Configuration

- **RapidAPI Key**: Replace the placeholder with your RapidAPI key in the `request_job_details` function.

## Dependencies

- **uAgents**: A Python framework for building decentralized applications.
- **http.client**: The HTTP client library in Python used for making API requests.
- **json**: A lightweight data interchange format.
- **asyncio**: A library to write concurrent code using the async/await syntax.
- **typing**: Provides support for type hints.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
