'''
The setup.py file is an essential part of packaging and 
disturbing python projects. It is used by setuptools 
(or distutils in order Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function is used to get the list of required packages
    
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            ## Read lines from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Pranay Nepalia",
    author_email = "nepaliapranay2000@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)