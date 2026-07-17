<div align="center">
  <h1> 30 Days Of Python: Day 23 - Virtual Environment </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>
</div>

[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 23](#-day-23)
  - [Setting up Virtual Environments](#setting-up-virtual-environments)
    - [Automating the Setup](#automating-the-setup)
  - [💻 Exercises: Day 23](#-exercises-day-23)

# 📘 Day 23

## Setting up Virtual Environments

When starting a project, it is better to use a virtual environment. A virtual environment creates an isolated workspace that helps avoid dependency conflicts across projects. If you run `pip freeze` on your terminal, you will see all packages installed on your computer. With `virtualenv`, only the packages specific to a project are available.

Open your terminal and install `virtualenv`:

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

Inside the `30DaysOfPython` folder, create a `flask_project` folder.

After installing the `virtualenv` package, go to your project folder and create a virtual environment by running:

For Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ virtualenv venv
```

For Windows:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

I prefer to call the new environment `venv`, but feel free to name it differently. Let us check if the `venv` folder was created by using `ls` (or `dir` on Windows).

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

Activate the virtual environment from the project folder.

For Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```

Activation on Windows may vary between Windows PowerShell and Git Bash.

For Windows Power Shell:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>venv\Scripts\activate
```

For Windows Git Bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>venv\Scripts\. activate
```

After activation, your prompt will start with `(venv)`. For example:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

Now, let's check the available packages by running `pip freeze`. You will not see any packages.

We are going to build a small Flask project, so let us install Flask inside this environment.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

Run `pip freeze` again to see the installed packages:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

When you finish, you should deactivate the active environment using `deactivate`.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

The necessary modules to work with Flask are installed and your project directory is ready. Remember to add `venv` to your `.gitignore` file so it is not pushed to GitHub.

### Automating the Setup

The steps above can be automated with a small, cross-platform helper script. The script below groups repeated operations into reusable functions, validates inputs, and handles errors.

```python
import os
import platform
import subprocess
import sys


def _validate_identifier(value: str, label: str) -> str:
    """Return a stripped identifier or raise ValueError."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string.")
    cleaned = value.strip()
    if any(char.isspace() for char in cleaned):
        raise ValueError(f"{label} must not contain spaces.")
    return cleaned


def create_project_directory(project_dir: str) -> str:
    """Create ``project_dir`` if it does not already exist."""
    project_dir = _validate_identifier(project_dir, "project_dir")
    try:
        os.makedirs(project_dir, exist_ok=True)
    except OSError as exc:
        raise RuntimeError(f"Could not create project directory: {exc}") from exc
    return os.path.abspath(project_dir)


def create_virtual_environment(project_dir: str, env_name: str = "venv") -> str:
    """Create a virtual environment named ``env_name`` inside ``project_dir``."""
    project_dir = _validate_identifier(project_dir, "project_dir")
    env_name = _validate_identifier(env_name, "env_name")

    full_project_path = os.path.abspath(project_dir)
    if not os.path.isdir(full_project_path):
        raise FileNotFoundError(f"Project directory not found: {full_project_path}")

    env_path = os.path.join(full_project_path, env_name)
    if os.path.exists(env_path):
        raise FileExistsError(f"Virtual environment already exists: {env_path}")

    try:
        subprocess.run(
            [sys.executable, "-m", "venv", env_path],
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"Failed to create virtual environment at {env_path}: {exc}"
        ) from exc
    return env_path


def get_activation_command(env_name: str = "venv") -> str:
    """Return the platform-specific command to activate the environment."""
    env_name = _validate_identifier(env_name, "env_name")
    if platform.system() == "Windows":
        return f"{env_name}\\Scripts\\activate"
    return f"source {env_name}/bin/activate"


def install_package(package: str) -> None:
    """Install ``package`` into the currently activated environment."""
    package = _validate_identifier(package, "package")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"Failed to install {package}: {exc}") from exc


def deactivate_virtual_environment() -> None:
    """Print the command used to deactivate the active virtual environment."""
    print("Run: deactivate")


def setup_flask_project(project_dir: str = "flask_project", env_name: str = "venv") -> None:
    """Create a project directory, a virtual environment, and install Flask."""
    create_project_directory(project_dir)
    env_path = create_virtual_environment(project_dir, env_name)
    activation_command = get_activation_command(env_name)

    print(f"Project directory: {os.path.abspath(project_dir)}")
    print(f"Virtual environment: {env_path}")
    print(f"Activate it with: {activation_command}")
    print("After activation, install Flask and run 'deactivate' when finished.")


if __name__ == "__main__":
    try:
        setup_flask_project()
    except (ValueError, FileNotFoundError, FileExistsError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
```

## 💻 Exercises: Day 23

1. Create a project directory with a virtual environment based on the example given above.

🎉 CONGRATULATIONS ! 🎉

[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)