from setuptools import find_packages,setup
from typing import List
import projectConstant



def get_requirements(file_path)->List[str]:
    '''
        this function will return the packages as list
        from the file of the file_path
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[tempReq.replace("\n","") for tempReq in requirements]

    if '-e .' in requirements:
        '''
            -e . added in requirements.txt to automatically run setup.py file
            and it need to be remove during the get_requirments function call because there are no package
            named as -e .
        '''
        requirements.remove('-e .')

    return requirements




setup(
    name=projectConstant.PROJECT_NAME,
    version=projectConstant.PROJECT_VERSION,
    author=projectConstant.AUTHOR,
    author_email=projectConstant.AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)