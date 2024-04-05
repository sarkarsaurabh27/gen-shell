from setuptools import setup, find_packages

setup(
    name='gen-shell',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-dotenv',
        'openai==1.14.2',
        'langchain==0.1.13',
        'langchain-community==0.0.29',
        'langchain-core==0.1.33',
        'langchain-openai==0.1.1',
        'pydantic==1.10.13',
        'urllib3==1.26.6',
    ],
    entry_points={
        'console_scripts': [
            'gen-shell=gen_shell.main:main',
        ],
    },
)