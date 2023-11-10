# Speedtest API

This repository contains a Flask application that performs internet speed tests using Ookla's Speedtest CLI and exposes the results through a RESTful API. The application is containerized using Docker, making it easy to build and deploy.

## Features

- Speedtest integration using `speedtest-cli`.
- Caching of speedtest results to optimize performance.
- RESTful API to retrieve the latest speedtest results.
- Docker and Docker Compose support for easy deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installing

1. Clone the Repository
2. Build and Run with Docker Compose
  - Be sure to update the port mapping in the compose file

### Usage

- **Get Speedtest Results**

    Send a GET request to `http://localhost:8080/speedtest` to retrieve the latest speedtest results.

    ```bash
    curl http://localhost:8080/speedtest