from setuptools import find_packages,setup
from typing import List 

Hypen_e_dot='-e .'
def get_attributes(file_path:str) -> List[str]:
    " this will return me the set of requirements in the list format."
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements
        


setup(
    name='Text_Tamer',
    version='0.0.1',
    author='shrimanthv',
    author_email='shrimanthv99@gmail.com',
    packages= find_packages(),
    install_requires=get_attributes('requirements.txt')
    
)