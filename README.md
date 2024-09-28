# Tobeto Test Project

This repository contains automated and manual tests for the **Tobeto** page and **Tobeto Library** page. The tests were developed as part of a project to ensure the functionality, reliability, and performance of the Tobeto platform.

## Project Overview

The goal of this project is to perform thorough testing of the Tobeto application using both manual and automated testing methods. The main technologies and tools used include:

- **Python**: Writing test scripts.
- **Selenium**: For browser automation.
- **Pytest**: Test framework for running and organizing test cases.
- **Postman**: API testing for backend validation.
- **JMeter**: Performance testing to assess the load capacity.
- **Jira**: For tracking issues and test cases.
- **Excel**: For documenting test cases and results.

## Test Types

### 1. **Manual Testing**
   - Validating functionality by manually interacting with the UI and API endpoints.
   - Creating and executing detailed test cases for different scenarios.

### 2. **Automated Testing**
   - **Selenium** is used for automating UI tests of the Tobeto platform.
   - **Pytest** organizes and runs the automated test suites.
   - Test coverage includes:
     - UI functionality testing
     - Form validation
     - User interactions
     - Navigation and links
     - Error handling

### 3. **API Testing**
   - **Postman** is used for API testing, validating the endpoints of the Tobeto backend.
   - Tests include:
     - **GET requests:** Checking data retrieval.
     - **POST requests:** Validating data creation and input handling.
     - **PUT requests:** Ensuring updates are applied correctly.
     - **DELETE requests:** Confirming deletion of records works as expected.
   - Each API endpoint is tested for:
     - Correct response codes (200, 404, 500, etc.)
     - Data validation
     - Security (authentication and authorization)
   - API tests are automated and run in different environments (development, production) using Postman collections.

### 4. **Performance Testing**
   - **JMeter** is used to simulate high user loads and measure the system’s response and stability under stress.

## Project Structure

- `/tests`: Contains all the test cases, both manual and automated.
- `/reports`: Stores test reports and logs.
- `/data`: Includes test data and configurations.
- `/api_tests`: Postman collections for testing API endpoints.

## How to Run Automated Tests

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tobeto-test-project
    ```

2. Install the necessary Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the automated tests using Pytest:
    ```bash
    pytest tests/
    ```

4. Run the API tests using Postman:
    - Import the Postman collections from the `/api_tests` folder into Postman.
    - Execute the tests from the Postman UI or using the Postman CLI.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out via GitHub or email.
