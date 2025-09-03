# IDS706_DE_w1
IDS706 Data Engineering Week 1 Assignment

This is the first project of Data Engineering Class.
The key of this project is to set up this repository in Github, the steps include
1. Create a new repository in Github and select README file as a default.
2. Clone the file in the local workspace (aka your onw computer), set up in the local environment.
3. In the local environment(VS code), set up the following in the terminal:
    a. touch Makefile
    b. touch hello.py
    c. touch test_hello.py
    d. touch requirements.txt
    This will create a Makefile (which allows user to run tasks automatically with simple make commands instead of long shell commands.), a py file for the code, a test py file to put test cases for the code, and a requirement txt file (which lists all the Python packages the project depends on)
    ** NOTE: If you are using VS code, a extension of [Makefile Tools] and [Dev Container] need to be installed
    ** Rebuild or update your container after the changes to pick up modifications
4. Run Makefile to install packages
5. Write some simple python code/function in the py file and put some test case for it in the test py file
6.  Run [make ___] from your Makefile to run the tests, format the code, lint the code, clean up the environment
7. Edit your README file to give a clear instruction of what the user need to do when they have your repository (This step can be moved forward or afterward, but it is very important!)
8. Push your local changes to github
    ** NOTE: IF you are editing in your local environment, stay local, don't edit anything directly in github or it will cause problems.
9. Enable GitHub Actions(in github) by setting up a workflow with YAML file, push this file to your repository.
10. Create a badge in the README file:

# Badges
[![IDS706 Week 1 Assignment](https://github.com/shellyycao/IDS706_DE_w1/actions/workflows/main.yml/badge.svg)](https://github.com/shellyycao/IDS706_DE_w1/actions/workflows/main.yml)



# To use this, please run:
a. Run [make install]
b. Run code in hello.py 
c. Run [make test]
d. Run [make format]
e. Run [make lint]
f. Run [make clean]


