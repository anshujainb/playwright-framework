# 🧪 Playwright + Pytest Automation Framework

A scalable and maintainable test automation framework built using **Playwright** and **pytest**.  
This framework supports **UI testing, API testing, schema validation, and reporting** using a structured Page Object Model (POM) design.

---
## Key Highlights

- UI automation using Playwright
- API testing support
- Page Object Model (POM) architecture
- HTML test reporting
- Pytest fixtures for setup & teardown
- Modular and reusable framework design
- JSON schema validation for API responses
- Easy to extend for CI/CD pipelines

---
## 📁 Project Structure
```text
project-root/
│
├── api/ # API test modules
├── pages/ # Page Object Model classes
├── tests/ # UI & API test cases
├── schemas/ # JSON schema validation files
├── utils/ # Helper utilities
├── config/ # Configurations
├── reports/ # Test reports (HTML/logs)
├── conftest.py # Pytest fixtures
├── requirements.txt # Dependencies
└── README.md
```

---
## Setup Instructions

### Clone the repository
```bash
git clone <your-repo-url>
cd playwright-project
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### Activate virtual environment

#### Mac/Linux
```bash
source venv/bin/activate
```

#### Windows
```bash
venv\Scripts\activate
```

### 3. install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers
```bash
playwright install
```

## Run all tests
```bash    
pytest
```

## Run tests in headed mode
```bash
pytest --headed
```

## Run specific test file
```bash
pytest tests/test_login.py
```

## Run tests with HTML report
```bash
pytest --html=reports/report.html
```

## After execution, reports are generated in:
```
/reports
```

## Open report.html in any browser to view:

- Test execution status
- Passed/failed cases
- Execution time
- Error logs


## This framework supports multiple test layers:

### 1. UI Tests
- Browser-based testing using Playwright
- Page Object Model structure
### 2. API Tests
- API validation using requests / API context
- Response validation using JSON schema
### 3. Schema Validation
- Ensures API response structure is consistent
- Prevents contract-breaking changes

## Framework Design Principles
🔹 Separation of concerns (UI / API / Utils)
🔹 Reusable components
🔹 Maintainable Page Object Model
🔹 Scalable folder structure
🔹 Minimal hardcoding of test data
🔹 Clean fixture-based setup

## Tech Stack
🔹 Python 3.x
🔹 Playwright
🔹 Pytest
🔹 Requests
🔹 JSON Schema
🔹 HTML Reporting

## Best Practices Followed
🔹 No hardcoded test data
🔹 Reusable page objects
🔹 Fixtures for browser/session management
🔹 Modular API layer
🔹 Independent test cases
🔹 Clean separation of UI & API tests

## Future Enhancements
🔹 CI/CD integration (GitHub Actions / Jenkins)
🔹 Allure reporting
🔹 Parallel test execution
🔹 Docker support
🔹 Test data management layer