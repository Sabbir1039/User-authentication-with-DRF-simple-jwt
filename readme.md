# User Authentication with DRF and Simple JWT

This project implements user authentication using Django Rest Framework (DRF) and Simple JWT.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Django Rest Framework
- Other project dependencies (install using `pip install -r requirements.txt`)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sabbir1039/User-authentication-with-DRF-simple-jwt.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd User-authentication-with-DRF-simple-jwt
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in browser to access the API.**

## Usage

- Use the provided API endpoints for user registration and authentication.



