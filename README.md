# Introduction to Git - ALTA Shared Task

_Master Git version control while working on the ALTA Shared Task using command line (CLI) and VS Code._

## 📋 Table of Contents

- [Welcome](#welcome)
- [Project Overview](#project-overview)
- [Quick Start](#quick-start)
- [Learning Objectives](#learning-objectives)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Project Workflow](#project-workflow)
- [Resources](#resources)
- [License](#license)

## Welcome

- **Who is this for**: Beginner developers who want to learn Git version control while contributing to the ALTA Shared Task
- **What you'll learn**: Fundamental Git concepts including commits, branches, history, collaboration, and working with shared repositories
- **What you'll build**: A Git workflow for collaborative development on the ALTA Shared Task (Brain Pool corpus)
- **Prerequisites**:
  - No prior Git or version control experience required
  - Recommended: Basic familiarity with Command Line Interfaces (CLI)
  - Recommended: Basic familiarity with Visual Studio Code
  - Python 3.7+ for notebook execution

- **How long**: This exercise takes approximately 60-90 minutes to complete

## Project Overview

This repository integrates Git fundamentals with the **ALTA Shared Task**, specifically focusing on the **Brain Pool corpus**. You'll learn version control while working with real-world computational linguistics data and code.

### What is the ALTA Shared Task?

The ALTA (Australasian Language Technology Association) Shared Task provides datasets and evaluation frameworks for natural language processing research. The Brain Pool corpus is one such dataset used for various NLP tasks.

### Key Learning Areas

1. **Git Fundamentals** - Understanding version control concepts
2. **Collaborative Development** - Working with branches and pull requests
3. **Project Management** - Organizing code and documentation
4. **Jupyter Notebooks** - Working with interactive Python notebooks in Git
5. **ALTA Tasks** - Understanding shared task workflows in NLP research

## Quick Start

### Prerequisites Setup

```bash
# Install Git (if not already installed)
# macOS
brew install git

# Ubuntu/Debian
sudo apt-get install git

# Windows
# Download from https://git-scm.com/download/win
```

### Clone the Repository

```bash
git clone https://github.com/rifat-binreza/skills-introduction-to-git.git
cd skills-introduction-to-git
```

### Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Learning Objectives

After completing this exercise, you will be able to:

1. ✅ Understand what version control is and why developers use it
2. ✅ Configure your Git identity and settings
3. ✅ Create your first repository and make meaningful commits
4. ✅ View project history and compare file changes
5. ✅ Work with branches to experiment safely
6. ✅ Understand Git collaboration concepts and workflows
7. ✅ Work with Jupyter notebooks in a version-controlled environment
8. ✅ Contribute to shared tasks and collaborative projects

## Repository Structure

```
skills-introduction-to-git/
├── README.md                                    # This file
├── LICENSE                                      # MIT License
├── .github/                                     # GitHub configuration
│   └── workflows/                               # CI/CD workflows
├── .devcontainer/                               # Development container setup
├── notebooks/                                   # Jupyter notebooks
│   ├── alta-shared-task-brain-pool.ipynb       # Main ALTA task notebook
│   └── fork-of-alta-shared-task-brain-pool.ipynb # Alternative version
├── src/                                         # Source code
│   └── (utility scripts and modules)
├── docs/                                        # Documentation
│   ├── SETUP.md                                # Setup instructions
│   ├── CONTRIBUTING.md                          # Contribution guidelines
│   └── ALTA_SHARED_TASK.md                     # ALTA task guide
├── requirements.txt                            # Project dependencies
└── data/                                        # Data files (if applicable)
```

## Getting Started

### Step 1: Environment Setup

Follow the [Setup Guide](docs/SETUP.md) to install dependencies and configure your environment.

```bash
# Quick setup
pip install -r requirements.txt
```

### Step 2: Understanding Git Basics

```bash
# Check Git version
git --version

# View your Git configuration
git config --list
```

### Step 3: Clone and Explore

```bash
# Clone this repository
git clone https://github.com/rifat-binreza/skills-introduction-to-git.git

# Navigate to the repository
cd skills-introduction-to-git

# View commit history
git log --oneline

# Check current branch
git branch
```

### Step 4: Create Your Working Branch

```bash
# Create a new branch for your work
git checkout -b feature/my-contribution

# View all branches
git branch -a
```

### Step 5: Make Changes and Commit

```bash
# View changed files
git status

# Stage changes
git add .

# Commit with a meaningful message
git commit -m "Add: Description of your changes"

# View commit history
git log --oneline
```

### Step 6: Working with the Notebooks

```bash
# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook

# Open notebooks/alta-shared-task-brain-pool.ipynb
```

## Project Workflow

### Standard Git Workflow

1. **Create a Branch**: Start from main branch
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature
   ```

2. **Make Changes**: Edit files, run tests, validate notebooks
   ```bash
   # Edit your files
   # Run Jupyter notebook
   # Test your changes
   ```

3. **Commit Changes**: Save your work with clear messages
   ```bash
   git add .
   git commit -m "Add: Specific description of changes"
   ```

4. **Push to Remote**: Upload your branch
   ```bash
   git push origin feature/your-feature
   ```

5. **Create Pull Request**: Submit for review on GitHub
   - Use meaningful PR title and description
   - Reference relevant issues or tasks
   - Wait for review feedback

6. **Merge**: Integrate changes to main
   ```bash
   git checkout main
   git pull origin main
   git merge feature/your-feature
   ```

### Commit Message Guidelines

Write clear, concise commit messages following this format:

```
<Type>: <Short description (50 chars max)>

<Optional detailed explanation>

Example:
Add: Data preprocessing for ALTA brain pool corpus
Improve: Error handling in notebook cells
Fix: Memory leak in data processing loop
Docs: Update installation instructions
```

## Common Git Commands

| Command | Description |
|---------|-------------|
| `git status` | Show current changes |
| `git add <file>` | Stage changes for commit |
| `git commit -m "msg"` | Create a commit |
| `git push` | Upload changes to remote |
| `git pull` | Download changes from remote |
| `git branch` | List/create branches |
| `git checkout <branch>` | Switch branches |
| `git merge <branch>` | Merge branches |
| `git log` | View commit history |
| `git diff` | Show changes between versions |

## Documentation

- **[Setup Guide](docs/SETUP.md)** - Detailed installation and environment setup
- **[Contributing Guidelines](docs/CONTRIBUTING.md)** - How to contribute to this project
- **[ALTA Shared Task Guide](docs/ALTA_SHARED_TASK.md)** - Information about the ALTA task and Brain Pool corpus

## Resources

### Git Learning Resources
- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Skills - Introduction to Git](https://github.com/skills/introduction-to-git)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

### ALTA Shared Task Resources
- [ALTA Shared Tasks](https://www.altanlp.org/shared-task/)
- [Brain Pool Corpus Documentation](https://github.com/rcds/alta-shared-task)
- [ACL Shared Tasks](https://www.aclweb.org/portal/content/acl-shared-tasks)

### Jupyter & Python Resources
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Python Documentation](https://docs.python.org/3/)
- [Anaconda Setup Guide](https://docs.anaconda.com/anaconda/install/)

## Troubleshooting

### Problem: "fatal: not a git repository"
```bash
# Solution: Initialize or clone the repository
git init
# or
git clone <repository-url>
```

### Problem: "Your branch is behind 'origin/main'"
```bash
# Solution: Pull the latest changes
git pull origin main
```

### Problem: Jupyter Notebook Not Loading
```bash
# Solution: Rebuild Jupyter
jupyter notebook --generate-config
jupyter notebook
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on:
- Reporting bugs
- Submitting enhancements
- Code review process
- Commit message standards

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Next Steps

1. **Read through** this README completely
2. **Follow** the [Setup Guide](docs/SETUP.md)
3. **Clone this repository** and explore the structure
4. **Open the notebooks** and follow the exercises
5. **Read** the [ALTA Shared Task Guide](docs/ALTA_SHARED_TASK.md)
6. **Create your own branch** and make your first commit
7. **Practice the workflow** with each exercise
8. **Follow** [Contributing Guidelines](docs/CONTRIBUTING.md) for submissions

## Questions or Issues?

- 📝 [Create an Issue](https://github.com/rifat-binreza/skills-introduction-to-git/issues)
- 💬 [Start a Discussion](https://github.com/rifat-binreza/skills-introduction-to-git/discussions)
- 📚 Check the [documentation](docs/)

---

**Happy Learning! 🚀**

_Last Updated: September 2026_
_Maintained by: [rifat-binreza](https://github.com/rifat-binreza)_

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](LICENSE)
