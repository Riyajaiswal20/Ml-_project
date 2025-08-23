from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirment(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirment=[]

    with open(file_path) as file_obj:
        requirment=file_obj.readlines()
        requirment=[req.replace('\n',"") for req in requirment]

        if HYPEN_E_DOT in requirment:
            requirment.remove(HYPEN_E_DOT)

    return requirment

setup(
name='DS PROJECT',
version='0.0.1',
author='RIYA',
author_email='RIYAJAISWAL9005@gmail.com',
packages=find_packages(),
install_requires=get_requirment('requirment.txt')
)