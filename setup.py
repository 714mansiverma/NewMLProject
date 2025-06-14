from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements.
    '''
    requirements=''
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
        
setup(
    name="ML Project",
    version='0.01',
    author='Mansi Verma',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)