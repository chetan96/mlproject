## responsible in creating ml app as a package, and can even deploy in pipy
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """_summary_: This function will return a list of requirements

    Args:
        file_path (str): _description_: path to requiremnts.txt file

    Returns:
        List[str]: _description_: a list of all the requirements as string name
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
    


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'chetan',
    author_email = 'chetan8126@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)