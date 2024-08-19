from setuptools import setup, find_packages

setup(
    name='AILang',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'antlr4-python3-runtime==4.13.1',
        'openai',  # Or any other AI-related packages you plan to use
    ],
    entry_points={
        'console_scripts': [
            'ailang=main:main',
        ],
    },
)
