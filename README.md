# GurshaFundWebApp

GurshaFundWebApp is a Django web application built for a hackathon to digitalize how people donate money to social causes and raise funds.

![GurshaFundWebApp home page](GurshaShare/Screenshot (915).png)
## Installation

To install and run GurshaFundWebApp, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/DagmawiSolomon/GurshaFund.git
   ```

2. Navigate to the project directory:
   ```
   cd GurshaFundWebApp
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv env
   source env/bin/activate  # On Unix/Linux
   env\Scripts\activate  # On Windows
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Perform database migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the application:
   ```
   Open your web browser and visit http://localhost:8000/
   ```

## Usage

GurshaFundWebApp allows users to donate money to social causes and raise funds. The application provides the following functionality:

- User registration and authentication.
- Make donations to specific causes.
- Create fundraising campaigns and share them with others.
- Track and manage donations and funds raised.

