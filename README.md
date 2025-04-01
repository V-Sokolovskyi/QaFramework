# QaFramework

QaFramework is a simple Python-based testing framework that I'm building to learn more about automated testing tools like Pytest, Selenium, Playwright, and API testing.
This project helps me explore how to organize test cases, use environment variables, create custom markers, and work with different testing tools in real scenarios.
It's still a work in progress, but it already has a basic structure and might be helpful for others who are also just getting started with Python test automation.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Custom Markers](#custom-markers)
5. [Environment Variables](#environment-variables)
6. [Contributing](#contributing)
7. [License](#license)





---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/V-Sokolovskyi/QaFramework.git
   cd QaFramework
   ```

2. **Create a virtual environment (highly recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the root directory with the following structure:
     ```
     GITHUB_TOKEN=your_github_personal_access_token
     BASE_URL=https://your-api-base-url.com
     DATABASE_URL=your-database-connection-string
     ```

---

## Usage

### Executing Tests

Leverage `pytest` to execute tests, utilizing custom markers for precise test selection.

1. **Run all tests:**
   ```bash
   pytest
   ```

2. **Run specific tests by marker:**
   - For API-related tests:
     ```bash
     pytest -m api
     ```
   - For UI automation tests:
     ```bash
     pytest -m ui
     ```
   - For database tests:
     ```bash
     pytest -m database
     ```

3. **Generate an HTML test report:**
   ```bash
   pytest --html=report.html
   ```

---

## Project Structure


```plaintext

QaFramework
│   
│   
├───.github
│   │   CODE_OF_CONDUCT.md
│   │   CONTRIBUTING.md
│   │   pull_request_template.md
│   │   SECURITY.md
│   │   
│   └───ISSUE_TEMPLATE
│           bug_report.md
│           feature_request.md
│                         
│       
├───config
│       config.py
│       
├───modules
│   ├───api
│   │   └───clients
│   │       │   github.py
│   │      
│   │               
│   ├───common
│   │   │   Alchemy_database.py
│   │   │   database.py
│   │     
│   │           
│   └───ui
│       └───page_objects
│           │   base_page.py
│           │   ing_playwright.py
│           │   singin_page_amazon.py
│           │   sing_in_page_amazon_playwright.py
│           │   sing_in_page_github.py
│          
│                   
├───tests
│   │   test_http.py
│   │   
│   ├───api
│   │   │   test_api.py
│   │   │   test_github_api.py
│   │   
│   │           
│   ├───database
│   │   │   test_database.py
│   │   │   test_database_alchemy.py
│   │  
│   │           
│   ├───ui
│   │   │   test_ingweb.py
│   │   │   test_ui_page_object.py
|
|
│   .env
│   .gitignore
│   become_qa_auto.db
│   conftest.py
│   data_for_test.py
│   LICENSE
│   login_generator.py
│   pytest.ini
│   README.md
│   requirements.txt        
```


## Custom Markers


This project employs the following markers to classify and manage test executions:

    change:     Tests that modify the name of a user.
    check:      Tests that check the users name.
    http:       Tests that validate the HTTP protocol.
    api:        Tests for the GitHub API.
    database:   Tests related to database functionality.
    uiAmazon:   Tests for UI interactions on the Rozetka website.
    uiGit:      Tests for UI interactions on GitHub 
    
    api:            Tests related to GitHub API functionality.
    
        user:       Tests that fetch or validate user details.
        repo:       Tests that involve repositories (search, create, delete).
        create:     Tests for creating repositories.
        delete:     Tests for deleting repositories.
        update:     Tests for updating repository details.
        misc:       Miscellaneous tests, such as fetching emojis or other metadata.
    

---

## Environment Variables
---
To ensure seamless execution, define the following variables in your `.env` file:

- **`GITHUB_TOKEN`**: A personal access token required for GitHub API authentication.
- **`BASE_URL`**: The foundational URL for API requests.
- **`DATABASE_URL`**: The connection string for accessing the database.

---

## Contributing

We welcome contributions from the community! Please adhere to the following workflow:

1. Fork the repository.
2. Create a dedicated feature branch:
   ```bash
   git checkout -b my-feature
   ```
3. Commit your changes with a clear message:
   ```bash
   git commit -m "Add feature: description"
   ```
4. Push your changes to the branch:
   ```bash
   git push origin my-feature
   ```
5. Initiate a pull request for review.

---

## License

This project is distributed under the terms of the [MIT License](LICENSE).

