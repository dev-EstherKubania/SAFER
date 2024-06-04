# SAFER

### Project Description

<p>SAFER is a weather monitoring application designed to provide real-time weather updates and alerts to users. The app integrates with a weather API to fetch meteorological data for specified locations. Users can view current weather conditions, forecasts, and receive notifications for weather-related events.</p>

##### SAFER is designed to:

- Provide real-time updates.
- Offer essential information.
- Foster community support for individuals affected by extreme weather.
- Enable user sharing of weather information.
- Provide alerts for areas affected by extreme weather, aiding informed decision-making.

### Features

- Weather Updates and Alerts: Fetches real-time meteorological data from the Open Weather API for specified locations. Users can view current weather conditions, forecasts, and receive notifications for weather-related events.
- Community Support: Fosters a community for sharing weather information and supporting those affected by extreme weather.
- Real-time Notifications: Provides alerts for extreme weather conditions to help users make informed decisions.
- User Sharing: Enables users to share weather information within the community.

### Architecture

    Backend:
    - Django: Python-based web framework for processing inputs and handling backend logic.
    - Websockets: Used for real-time communication.
    - PostgreSQL: Database management.

    Frontend:
    - HTML, CSS, JavaScript: For user interface and interactions.
    - Bootstrap: CSS framework for responsive design.
    - Leaflet.js: JavaScript library for interactive maps (for future features).

    Third-party Services:
    - Open Weather API: Used to get weather data for the locations in the web app.

    ## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dev-EstherKubania/SAFER.git
   
   cd safer
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   # Install virtualenv if not already installed
   pip install virtualenv
   
   # Create a virtual environment
   virtualenv venv
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   - Create a file named `.env` in the project root directory.
   - Add your credentials and sensitive information in this file in the following format:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```

5. **Apply Migrations**:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

6. **Run the Server**:
   ```bash
   python3 manage.py runserver
   ```

<p>Welcome, you can now create your weather community</p>