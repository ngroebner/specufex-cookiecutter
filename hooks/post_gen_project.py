import os
import subprocess

repo_name = "{{ cookiecutter.repo_name }}"
project_name = "{{ cookiecutter.project_name }}"

if "{{ cookiecutter.create_environment }}" == "y":
    subprocess.run("make create_environment", shell=True)
