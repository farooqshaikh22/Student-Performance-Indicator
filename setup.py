from setuptools import find_packages,setup
from typing import List

HYPHON_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:
    
    requirements = []
    
    with open(filepath) as file_obj:
        
        requirements = file_obj.readlines()     
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
            
    return requirements
    

setup(
    name='student_performance_indicator',
    version='0.0.1',
    author='Faruq Shaikh',
    author_email='farooqshaikh22@ymail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)