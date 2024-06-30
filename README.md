# flask-celery-on-docker

This project provides a system for logging API request parameters and responses asynchronously using a Flask application. The system consists of a frontend application and a backend application that work together to log and manage API requests.

## Project Overview

1. **Asynchronous API Logging**:
    - The API server processes requests from clients and logs the request parameters and response values by sending asynchronous requests to the `flask-app` API server.
2. **Technologies Used**:
    - **Flask**: The main framework used for the API server.
    - **Celery**: Used to queue tasks for asynchronous processing.
    - **Redis**: Serves as the message broker for Celery and stores the queue.
    - **MySQL**: Stores the logs of the API requests and responses.
3. **Access and Usage**:
    - Access the application at `localhost:3000` to send random API requests to `flask-app`, which logs and allows you to query the API logs.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/woogieReal/flask-celery-on-docker.git
    cd flask-celery-on-docker
    ```

2. Build and start the Docker containers:
    ```sh
    docker-compose up --build
    ```

3. Access the application:
    - Frontend: `http://localhost:3000`
    - Backend: `http://localhost:5000`

## Usage
1. Start the Docker containers as described in the installation steps.
1. Open your browser and navigate to http://localhost:3000.
1. Interact with the frontend to generate random API requests.
1. The flask-app backend will process these requests, log them asynchronously using Celery, and store the logs in MySQL.
1. You can query and view the logs via the backend API.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For more information, please contact:

- Name: woogieReal
- Email: woogiereal@gmail.com

Happy coding!