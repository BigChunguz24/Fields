# Fields
Generates the field lines of irrotational fields and their respective 
equipotential surfaces.

-----------------------------------------------------------------------------
### Setting up the virtual environment and installing libraries

A virtual environment is needed to install packages locally rather than globally.
This is important as different projects may need different versions of the same
library. It also allows to have project-specific dependencies.

1) Create a virtual environment via the following command:
```shell
$ py -m venv venv   //or//   python -m venv venv
```
2) Individual libraries(e.g. black) are then installed via the following command:
```shell
$ pip install black
```
For a particular version, one could use:
```shell
$ pip install black=22.3.0
```
For all the dependencies of the project at once, one could use:
```shell
$ pip install -r requirements.txt
$ pip install -r requirements-testrun.txt
```
-----------------------------------------------------------------------------
### Using Black

The Black library is a code formatter for Python, designed to enforce consistent 
and readable code formatting. It automatically reformats Python code to PEP 8.

1) Line length configuration - by default this sets lines to 88 characters. 
If needed, it can be changed via the following command:
```shell
$ black --line-length 100 my_file.py
```
2) Checking for formatting issues without modifying a file:
```shell
$ black --check my_file.py
```
3) Formatting a file:
```shell
$ black my_file.py
```
4) Formatting an entire directory:
```shell
$ black .
```
-----------------------------------------------------------------------------
### GitHub Workflows

A workflow is a configurable automated process that will trigger one or more jobs 
which are pre-defined by a YAML file in the repository. A job can be triggered 
manually, by an event or at a defined schedule. GitHub workflows are located 
in the `.github/workflows` directory. Steps:
- An event occurs with an associated commit SHA and Git reference;
- GitHub searches the .github/workflows directory for workflow files present in 
the reference;
- A workflow is triggered for any workflow that has `on:` values matching the 
triggering event;

An example on how to read workflows for ***.github/workflows/main.yml***:
1) Defining the name of the workflow:
```shell
name: CI/CD Master Branch
```
2) The workflow is triggered upon pushing to the main branch. There is a 
schedule that runs every day at 06:00 UTC.
```shell
on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 6 * * *'
```
Notes:
- The schedule has the same indent as the triggers - different triggers =/= 
different events;
- One can define multiple triggers, not just "push to main";
- Schedules can be stacked (i.e. crons)

3) Next we define the jobs that this workflow executes. In our case we have three 
jobs in total:
```shell
jobs:
  test: ...some actions...
  build: ...some actions...
  deploy: ...some actions...
```

### Docker Hub access tokens
To create an image in Docker, we need to access docker using a password replacement
used for GitHub Actions, GitLab CI, etc. Creating it requires the following steps:
1) Go to `https://hub.docker.com/` and login;
2) Go to `Account Settings` and navigate to `Personal Access Tokens`
3) Generate a new Read/Write token and copy the token immediately (you won't see it
again)
4) The copied value goes into `DOCKER_TOKEN` in the `Secrets` of `GitHub Actions`

-----------------------------------------------------------------------------
### Secrets:
This project uses GitHub Actions secrets to authenticate with Docker Hub during
the CI/CD workflow. The following repository secrets must be configured:
- `DOCKER_REPO_USER` - Docker Hub username
- `DOCKER_REPO_PASSWORD` - Docker Hub password
- `DOCKER_TOKEN` - Docker Hub access token

To configure existing secrets or add new ones:

1. Go to **Repository Settings**
2. Navigate to **Secrets and variables → Actions**
3. Click **New repository secret**
4. Add the required secrets listed above

After this has been done, secrets can be referenced via the secrets context
as follows:
- `DOCKER_REPO_USER` - secrets.DOCKER_REPO_USER
- `DOCKER_REPO_PASSWORD` - secrets.DOCKER_REPO_PASSWORD
- `DOCKER_TOKEN` - secrets.DOCKER_TOKEN