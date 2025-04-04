# Python Project

This project contains a simple Python application with a function to greet users.

## Files

- `app.py`: Contains the `greet` function that takes a name as an argument and returns a greeting message.
- `requirements.txt`: Lists the dependencies required for the project.

## Usage

To use the `greet` function, follow these steps:

1. Clone the repository or download the project files.
2. Install the required dependencies listed in `requirements.txt` using the command:
   ```
   pip install -r requirements.txt
   ```
3. Import the `greet` function from `app.py` in your Python script:
   ```python
   from app import greet
   ```
4. Call the `greet` function with a name:
   ```python
   message = greet("Your Name")
   print(message)
   ```

## Example

```python
from app import greet

print(greet("Alice"))  # Output: Hello, Alice!
```

## License

This project is open source and available under the MIT License.