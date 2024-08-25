
# API PetStore Testing Project

This project is an automated test framework for testing REST APIs using the [PetStore API](https://petstore.swagger.io/#/). It leverages the Pytest framework for creating, organizing, and running tests.

## Project Structure

```plaintext
C:\API_Testing\PythonAPI_Testing
│
├── API_PetStoreTests
│   ├── __init__.py
│   ├── test_basics.py         # Basic test cases for initial setup
│   ├── test_pets.py           # Test cases specifically for pet operations
│   ├── .pytest_cache          # Pytest cache directory
│   └── __pycache__            # Compiled Python files
│
├── config                     # Configuration files for the project
├── logs                       # Log files generated during test runs
├── utils                      # Utility functions and helper scripts
├── .gitignore                 # Git ignore file for excluding unnecessary files
├── pytest.ini                 # Pytest configuration file
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies for the project
└── test_loggings.py           # Tests for logging functionalities
```

## Getting Started

### Prerequisites

To run this project, you'll need Python installed on your system along with `pip` (Python package installer). 

### Installation

1. Clone the repository to your local machine.
   
   ```bash
   git clone https://github.com/NaveenKumarDongre/PythonAutomation-API_Testing-.git
   ```

2. Navigate to the project directory.

   ```bash
   cd PythonAPI_Testing
   ```

3. Install the required Python packages using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

### Running the Tests

To run the tests, navigate to the project root directory and execute the following command:

```bash
pytest
```

This command will automatically discover and run all test cases defined in the `API_PetStoreTests` directory.

### Test Files

- **test_basics.py**: Contains basic tests to verify the initial setup and configuration.
- **test_pets.py**: Contains test cases that specifically test pet-related endpoints in the PetStore API.

### Configuration

The `pytest.ini` file is used to configure the Pytest framework settings, such as markers, logging levels, and plugins.

### Logging

All logs are stored in the `logs` directory. These logs capture detailed information about the test execution process, which is useful for debugging and analysis.

### Test Reports

Test results are reported in the console, and detailed logs are generated in the `logs` directory. You can modify the logging settings in the `pytest.ini` file to change the verbosity or format of the logs.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the [Swagger PetStore API](https://petstore.swagger.io/#/) for providing a great platform to test REST APIs.
- This project is a part of my learning journey to master test automation frameworks.
