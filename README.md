# Lookup Domain

This project is a Python-based tool for performing domain lookups. It allows users to retrieve information about a domain, such as its IP address, registrar details, and more.

## Features

- Retrieve IP address of a domain
- Fetch registrar details
- Check domain availability
- Display DNS records

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/<your-username>/lookup-domain.git
    ```
2. Navigate to the project directory:
    ```sh
    cd lookup-domain
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the domain lookup tool, run the following command:

```sh
python lookup.py <domain>
```

Replace `<domain>` with the domain you want to look up.

### Example

```sh
python lookup.py example.com
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.
