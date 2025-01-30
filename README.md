# LLM-FAQ-Assistant
Leveraging LLM/GenAI to Build a Flask-based Intelligent FAQ Assistant
# Flask Project

## Overview
This project is a simple Flask web application designed to demonstrate basic web functionalities like handling requests and rendering templates. It can serve as a starting point for building more complex Flask-based applications.

## Technologies Used
- **Python 3.x**
- **Flask**
- Any other libraries you might be using (e.g., Jinja2, SQLAlchemy)

## Installation Instructions
Follow the steps below to set up the project on your local machine:

1. **Clone the repository**:
    ```bash
    git clone <repository_link>
    ```

2. **Install dependencies**:
    If you have a `requirements.txt` file, install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

    If you don’t have a `requirements.txt` file, you can install Flask manually:
    ```bash
    pip install flask
    ```

3. **Set up the environment (if needed)**:
    If your app requires specific environment variables (e.g., `FLASK_ENV`), set them up accordingly.

## Running the Application
1. Run the Flask application using the following command:
    ```bash
    python app.py
    ```
---

## File Structure

---


faq assistant/

│── app.py/
│── config.json/
│── config.py/
│── __pycache__/
│   ├── index.html  
│── .ipynb_checkpoints/
│   ├── config.cpython-312     
│   ├── config-checkpoint       
│── templates/
│   ├── index.html     
│── static/
│   ├── styles.css     
│   ├── script.js      
│── data/
│   ├── knowledge_base.json 

---

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to see the app in action.

## Usage
- Once the app is running, you can interact with it via the browser. The app should render a basic homepage or any route you've defined.
- You can extend the app by adding more routes and templates as needed.

## Example Output
If your app has any specific output (like a welcome message, data from a database, etc.), include it here.

Example:
- When visiting the homepage, the app displays: "Welcome to my Flask app!"

## Contributing
Feel free to fork the repository and submit pull requests if you'd like to contribute. Please make sure your contributions follow the project's coding style and include tests where applicable.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
