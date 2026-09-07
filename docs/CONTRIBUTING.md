# Contributing to Skills Introduction to Git - ALTA Shared Task

Thank you for your interest in contributing! This document provides guidelines for participating in this project.

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md). By participating, you are expected to uphold this code.

## How to Contribute

### 1. Reporting Bugs

Before creating bug reports, check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what the problem is**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your system specifications** (OS, Python version, Jupyter version)

### 2. Suggesting Enhancements

Enhancement suggestions are tracked as GitHub Issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and the expected behavior**
- **Explain why this enhancement would be useful**
- **List some other projects or resources where this enhancement exists**

### 3. Pull Requests

- Fill in the required template
- Follow the Git and Python styleguides
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Git Workflow

### Step 1: Fork and Clone

```bash
# Fork the repository on GitHub (click the Fork button)

# Clone your fork
git clone https://github.com/YOUR-USERNAME/skills-introduction-to-git.git

# Add the original repository as upstream
git remote add upstream https://github.com/rifat-binreza/skills-introduction-to-git.git
```

### Step 2: Create a Feature Branch

```bash
# Update from upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create your feature branch
git checkout -b feature/your-feature-name
```

### Step 3: Make Your Changes

- Write clear, concise code
- Add comments where necessary
- Update documentation
- Test your changes thoroughly

### Step 4: Commit Your Changes

Follow these guidelines for commit messages:

```
<Type>: <Subject>

<Body>

<Footer>
```

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that don't affect code meaning (formatting, etc.)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Code change that improves performance
- `test`: Adding or updating tests

**Subject:**
- Use imperative, present tense: "Add" not "Added" or "Adds"
- Don't capitalize first letter
- No period (.) at the end
- Limit to 50 characters

**Body:**
- Use imperative, present tense
- Include motivation for the change
- Contrast with previous behavior
- Wrap at 72 characters

**Example:**
```
feat: add data preprocessing for ALTA brain pool

Add comprehensive data preprocessing pipeline for handling
ALTA shared task brain pool corpus with support for:
- Text normalization
- Tokenization
- Feature extraction

This closes #42
```

### Step 5: Push and Create Pull Request

```bash
# Push your feature branch
git push origin feature/your-feature-name

# Create a pull request through the GitHub web interface
```

## Pull Request Guidelines

- **Title**: Clear and descriptive
- **Description**: Follow the PR template
- **Reference Issues**: Use "Fixes #123" or "Closes #123"
- **Include Tests**: Add or update tests as needed
- **Update Docs**: Update README and other documentation
- **One Feature Per PR**: Keep PRs focused and manageable

### PR Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Fixes #(issue number)

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
Describe the tests you've run:
- [ ] Test A
- [ ] Test B

## Screenshots (if applicable)
Add screenshots or GIFs showing the changes

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented complex sections
- [ ] I have updated documentation
- [ ] My changes generate no new warnings
- [ ] I have tested my changes
```

## Styleguides

### Python Style Guide

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/):

```python
# Good
def calculate_metrics(data, threshold):
    """Calculate performance metrics from data."""
    results = []
    for item in data:
        if item > threshold:
            results.append(item)
    return results

# Bad
def calc_metrics(d,t):
  r=[]
  for i in d:
    if i>t:
      r.append(i)
  return r
```

### Jupyter Notebook Style Guide

1. **Structure**: Use markdown cells for clear section breaks
2. **Documentation**: Include descriptive markdown cells
3. **Code Clarity**: Write readable code with comments
4. **Output**: Clear output before committing
5. **Naming**: Use descriptive variable names

```python
# Good notebook cell
# Cell type: Markdown
# ## Data Preprocessing
# This section loads and preprocesses the ALTA brain pool corpus

# Cell type: Code
import pandas as pd

def load_data(file_path):
    """Load ALTA brain pool data from CSV file."""
    return pd.read_csv(file_path)

data = load_data('data/brain_pool.csv')
print(f"Loaded {len(data)} samples")
```

### Documentation Style

- Use clear, concise language
- Use active voice
- Break content into logical sections
- Include examples where helpful
- Keep line length to ~80 characters in markdown

## Review Process

1. **Automated Checks**: CI/CD pipeline runs tests and linting
2. **Code Review**: Maintainers review code quality, logic, and style
3. **Testing**: Verify all tests pass
4. **Documentation**: Ensure documentation is updated
5. **Merge**: Approved PRs are merged to main

## Development Setup

### Clone the Repository

```bash
git clone https://github.com/rifat-binreza/skills-introduction-to-git.git
cd skills-introduction-to-git
```

### Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using conda
conda create -n alta-git python=3.9
conda activate alta-git
```

### Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/

# Run specific test file
pytest tests/test_preprocessing.py
```

## Questions?

- 📖 Check the [README.md](../README.md)
- 📝 [Create an Issue](https://github.com/rifat-binreza/skills-introduction-to-git/issues)
- 💬 [Start a Discussion](https://github.com/rifat-binreza/skills-introduction-to-git/discussions)

---

**Thank you for contributing! 🎉**
