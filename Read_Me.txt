# QaFramework

The QaFramework represents an advanced Python-based architecture meticulously crafted to enable automated testing through a sophisticated structure for managing test cases, API validation, and seamless integration with prominent tools such as Pytest and Selenium.

---

## Features

- **API Testing:** Provides robust utilities for engaging with APIs, verifying responses, and managing intricate test datasets.
- **UI Testing:** Incorporates Selenium for comprehensive web UI automation, supporting complex testing scenarios.
- **Database Testing:** Enables validation of database operations and ensures data integrity.
- **Custom Test Markers:** Facilitates systematic categorization of tests, optimizing organization and enabling targeted execution.


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

```
QaFramework/
│
├── core/                # Core utilities and configurations.
├── tests/               # Test cases categorized by feature or function.
├── ui/                  # UI testing modules and resources.
├── database/            # Database interaction utilities and tests.
├── github.py            # Module for GitHub API interactions.
├── requirements.txt     # Project dependencies.
├── .env.example         # Example environment variables file.
├── pytest.ini           # Pytest configuration and markers.
└── README.md            # Project documentation (this file).
```

---

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

