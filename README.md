# Cookiecutter ML Experiment Template

A custom directory structure for machine learning experiments based on [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)

## Requirements to use the cookiecutter template

- Python 3.6+
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## To start a new project, run

``` bash
cookiecutter https://github.com/ngroebner/cookiecutter-ml-template
```

The setup script will walk you through choosing various option for your project. The options and defults are below.

1. ```project_name [project_name]```
The name of your project.

2. ```repo_name [project_name]```
Github repo name. This will also be the name of the root directory, and the name of the conda environment used for the project.

3. ```author_name [Your name (or your organization/company/team)]:```

4. ```description [A short description of the project.]:```

5. ``` Select open_source_license:``` Choose the license for the ```LICENSE``` file.

6. ```Select python_version:``` If yoou need a specific version for your packages

7. ```install_numpy_stack [y]:``` Answering "yes" will add numpy, scipy, pandas, matplotlib, jupyter, and jupyterlab to the conda environment specification.

8. ```use_mlflow [y]:``` Answering "yes" will add mlflow to the environment specification. mlflow can be used for, among other things, tracking hyperparameters used in each run.

9. ```install_dev [y]:``` Answering "yes" will install isort, flake8, and black packages for linting and formatting code.

10. ```create_environment [y]:``` Create a new conda envirronment with the packages you chose above. The name of the environment will be ```repo_name```.

Cookiecutter will create a standard [directory structure](Directory_Structure.md).


## How to use the new project

```cd``` into the directory and activate the conda environment. Add any other packages you know you will need.

In the ```src``` directory, write scripts to pull the raw data into the ```data/raw``` directory, preprocess that data for running your model, and saving the preprocessed data to the ```data/preprocessed``` directory.

Create your model training code and put it in....

## Make instructions

The gnu utility make is used to run standard workflows and development stuff. This section will include a reference at some point.

## Things to add

- Documentation!
- Perhaps have standard filenames for the processing steps, so that you can use ```make``` to run everything, without having to rewrite stuff in the Makefile. E.g:
  - pull_data.py
  - preprocess_data.py
  - train.py
  - transform.py/predict.py

