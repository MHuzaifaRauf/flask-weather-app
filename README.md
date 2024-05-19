# Weather App

Welcome to the Weather App! This repository serves as a great starting point for those new to web development with Python. It's designed to give you a solid foundation in organizing your code and understanding how to build and run a complete, fully working web application.

## Project Overview
![Image](/static/img/weather-app.png)

The Weather App is a simple yet powerful project that demonstrates how to retrieve and display weather information using an API. It's built with Flask, a lightweight web framework for Python, making it an excellent choice for beginners looking to dive into web development.

## Getting Started

To get started with the Weather App, follow these simple steps:

1. **Clone the Repository**: First, clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/MHuzaifaRauf/weather-app.git
   ```

2. **Create a .env File**: Before running the application, you need to create a `.env` file in the root directory of the project. This file will contain your API key, which you can obtain for free from [OpenWeatherMap](https://openweathermap.org) by creating a new account. Once you have your API key, add it to the `.env` file like so:
   ```
   API_KEY=copy_and_paste_the_API_key_here
   ```
   Make sure to replace `copy_and_paste_the_API_key_here` with your actual API key.

3. **Install Dependencies**: Navigate to the project directory and install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
   This command installs all the necessary Python packages listed in the `requirements.txt` file.

4. **Run the Application**: After installing the dependencies and setting up the `.env` file, start the Flask server by running the `main.py` script:
   ```
   python main.py
   ```
   This command starts the Flask development server.

5. **Access the Application**: Open your web browser and navigate to `http://localhost:8000`. This is where the Weather App is hosted by default. You can change the server address and port in the `main.py` file if you wish.

## Contributing

If you're interested in contributing to this project, please feel free to fork the repository and submit a pull request.

## Contact

If you have any questions or feedback about the Weather App, please feel free to reach out. You can contact me on LinkedIn, Twitter (links for which are available on my profile) or open an issue on GitHub.

Happy coding!!!