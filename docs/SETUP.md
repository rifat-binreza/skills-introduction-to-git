# Setup Guide - Skills Introduction to Git

This guide will help you set up your development environment to work with the ALTA Shared Task and Git learning materials.

## Prerequisites

- **Python 3.7+** (Recommended: 3.9 or 3.10)
- **Git 2.30+**
- **pip** or **conda** package manager
- **Visual Studio Code** (Optional but recommended)

## Installation Steps

### 1. Install Git

#### macOS
```bash
brew install git
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install git
```

#### Windows
Download from [https://git-scm.com/download/win](https://git-scm.com/download/win) and run the installer.

#### Verify Installation
```bash
git --version
```

### 2. Configure Git

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Optional: Set default editor
git config --global core.editor "code"

# Verify configuration
git config --list
```

### 3. Clone the Repository

```bash
git clone https://github.com/rifat-binreza/skills-introduction-to-git.git
cd skills-introduction-to-git
```

### 4. Set Up Python Environment

#### Option A: Using Python venv (Recommended for beginners)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Verify activation (should see "venv" in prompt)
```

#### Option B: Using Conda

```bash
# Create conda environment
conda create -n alta-git python=3.9

# Activate environment
conda activate alta-git
```

### 5. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Install development packages (optional)
pip install -r requirements-dev.txt
```

### 6. Verify Installation

```bash
# Check Python
python --version

# Check pip
pip --version

# Test Jupyter
jupyter --version

# Start Jupyter (should open in browser)
jupyter notebook
```

## IDE Setup

### Visual Studio Code Setup

1. **Install VS Code** from [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. **Install Extensions**:
   - Python (Microsoft)
   - Jupyter (Microsoft)
   - Git Graph (optional)
   - GitHub Pull Requests and Issues (optional)

3. **Configure Python Interpreter**:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
   - Type "Python: Select Interpreter"
   - Choose the virtual environment created above

4. **Open Project**:
   ```bash
   code .
   ```

### PyCharm Setup

1. **Download PyCharm** Community Edition from [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

2. **Configure Interpreter**:
   - File → Settings (or PyCharm → Preferences on macOS)
   - Project: skills-introduction-to-git → Python Interpreter
   - Add Interpreter → Add Local Interpreter
   - Select existing environment or create new venv

3. **Enable Jupyter Support**:
   - File → Settings → Languages & Frameworks → Jupyter
   - Enable Jupyter Server support

## Jupyter Notebook Setup

### Start Jupyter Notebook

```bash
# Make sure virtual environment is activated
jupyter notebook
```

This will open Jupyter in your default browser.

### Start JupyterLab (Alternative)

```bash
# JupyterLab provides a more modern interface
jupyter lab
```

### Create a New Notebook

1. Click "New" → "Python 3"
2. Start writing code and markdown

### Using Notebooks with Git

```bash
# Before committing, clear notebook output
# In Jupyter: Cell → All Output → Clear

# Or use command line
nbstripout *.ipynb
```

## Troubleshooting

### Problem: "python: command not found"

**Solution**: 
- Make sure Python is installed
- On macOS, you might need to use `python3` instead of `python`
- Add Python to PATH (Windows)

### Problem: "venv: command not found"

**Solution**:
```bash
# Try using Python module directly
python -m venv venv
```

### Problem: "ModuleNotFoundError" when importing packages

**Solution**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows

# Reinstall packages
pip install -r requirements.txt
```

### Problem: "Jupyter command not found"

**Solution**:
```bash
# Install Jupyter in your virtual environment
pip install jupyter jupyterlab

# Or reinstall from requirements
pip install -r requirements.txt
```

### Problem: Permission denied when running scripts

**Solution** (macOS/Linux):
```bash
chmod +x script_name.sh
./script_name.sh
```

## Next Steps

1. ✅ Verify your installation works
2. ✅ Open the main README.md and start learning
3. ✅ Navigate to `notebooks/alta-shared-task-brain-pool.ipynb`
4. ✅ Follow the Git exercises in the notebooks
5. ✅ Practice Git commands in the terminal

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Jupyter Documentation](https://jupyter.org/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Skills - Introduction to Git](https://github.com/skills/introduction-to-git)

## Getting Help

If you encounter issues:

1. Check this setup guide again
2. Search [GitHub Issues](https://github.com/rifat-binreza/skills-introduction-to-git/issues)
3. Create a new issue with:
   - Your operating system
   - Python version
   - Error message
   - Steps to reproduce

---

**Ready to learn Git? Let's go! 🚀**
