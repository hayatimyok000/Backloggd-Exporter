# Contributing to Matrix Backloggd Exporter

First off, thank you for considering contributing to Matrix Backloggd Exporter! 🎉

## 🤔 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots if possible**
* **Include your Python version and OS**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and explain which behavior you expected to see instead**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python style guide (PEP 8)
* Include screenshots in your pull request whenever possible
* End all files with a newline
* Avoid platform-dependent code

## 🎨 Style Guidelines

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Examples:
```
Add CSV export validation
Fix memory leak in Matrix rain animation
Update README with new screenshots
```

### Python Style Guide

* Follow PEP 8
* Use 4 spaces for indentation (no tabs)
* Use docstrings for functions and classes
* Keep lines under 100 characters when possible
* Use meaningful variable names

### Code Organization

```python
# Imports
import standard_library
import third_party_library
from local_module import something

# Constants
CONSTANT_NAME = "value"

# Classes
class ClassName:
    """Class docstring."""
    
    def __init__(self):
        """Initialize method."""
        pass
    
    def method_name(self):
        """Method docstring."""
        pass

# Functions
def function_name():
    """Function docstring."""
    pass

# Main execution
if __name__ == "__main__":
    main()
```

## 🧪 Testing

Before submitting a pull request:

1. Test your changes on Windows (if possible)
2. Test with different Backloggd usernames
3. Test all export formats (CSV, JSON, TXT)
4. Ensure the UI renders correctly
5. Check for memory leaks with long-running operations

## 📝 Documentation

* Update README.md if you change functionality
* Add docstrings to new functions and classes
* Comment complex logic
* Update requirements.txt if you add dependencies

## 💡 Ideas for Contributions

Here are some areas where contributions would be especially welcome:

### Features
- [ ] Add Excel export format (.xlsx)
- [ ] Implement search/filter in extracted data
- [ ] Add statistics dashboard
- [ ] Multi-language support
- [ ] Dark/Light theme toggle
- [ ] Export to Google Sheets
- [ ] Batch user export
- [ ] Game cover image downloads

### UI Improvements
- [ ] Additional color themes
- [ ] Custom animation speeds
- [ ] Window resize handling
- [ ] Keyboard shortcuts
- [ ] System tray integration
- [ ] Notifications

### Technical
- [ ] Unit tests
- [ ] Integration tests
- [ ] CI/CD pipeline
- [ ] Logging system
- [ ] Configuration file support
- [ ] Command-line interface
- [ ] Installer/executable creation

### Documentation
- [ ] Video tutorial
- [ ] More screenshots
- [ ] Troubleshooting guide
- [ ] FAQ section
- [ ] API documentation

## 🏗️ Development Setup

1. Fork and clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/matrix-backloggd-exporter.git
cd matrix-backloggd-exporter
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a new branch
```bash
git checkout -b feature/your-feature-name
```

5. Make your changes and commit
```bash
git add .
git commit -m "Add your feature"
```

6. Push to your fork
```bash
git push origin feature/your-feature-name
```

7. Open a Pull Request

## 📞 Questions?

Feel free to open an issue with the `question` label if you have any questions!

## 🎉 Recognition

Contributors will be added to the README.md file. Thank you for making this project better!

---

**Happy Coding! 💚**