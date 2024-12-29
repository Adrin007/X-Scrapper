# X-Scrapper

X-Scrapper is a web scraping tool designed to extract trending topics from X (formerly Twitter) and display the results in a visually appealing interface. The tool leverages Selenium and Google Chrome for automated web scraping and includes features like proxy support for enhanced security.

## Features

- **Scrapes Trending Topics**: Extracts top 5 trending topics from X.
- **Proxy Integration**: Uses proxies to avoid detection and improve anonymity.
- **Interactive Web Interface**: Displays trends along with the current IP address and raw data in a user-friendly grid layout.
- **Headless Browsing**: Supports headless Chrome for efficient and stealthy scraping.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Adrin007/X-Scrapper.git
    cd X-Scrapper
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set environment variables in a `.env` file:
    ```plaintext
    X_USERNAME=<your_username>
    X_PASSWORD=<your_password>
    ```

4. Install Google Chrome and ChromeDriver:
    - Ensure Google Chrome is installed.
    - Use `webdriver-manager` or download the appropriate ChromeDriver for your system.

5. (Optional) Configure Docker:
    Build and run the Docker container for deployment:
    ```bash
    docker build -t x-scrapper .
    docker run -p 5000:5000 x-scrapper
    ```

## Usage

### Running Locally
1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

### Running with Docker
1. Build the Docker image:
    ```bash
    docker build -t x-scrapper .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 x-scrapper
    ```

## Deployment

### Render Deployment
1. Add the provided `Dockerfile` to the root of your project.
2. Use the following build command during deployment:
    ```bash
    docker build -t x-scrapper .
    ```

### Requirements
- Ensure the `chromedriver` path is set correctly in the project.
- Use a `startup.sh` script if deploying to platforms like Render to manage Google Chrome and dependencies.

## Project Structure

X-Scrapper/ ├── app.py # Main Flask application ├── db.py # Database interaction script ├── ipPicker.py # Proxy selection utility ├── requirements.txt # Python dependencies ├── Dockerfile # Docker configuration ├── templates/ # HTML templates │ ├── index.html # Main UI ├── static/ # Static files (CSS, JS) └── .env # Environment variables

## Local Deployment Sample

![Alt text](c:\Users\DELL\Downloads\Telegram Desktop\x-scrapper.jpg)

![Alt text](c:\Users\DELL\Downloads\Telegram Desktop\x-Scrapper-trends.jpg)