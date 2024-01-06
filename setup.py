from setuptools import setup, find_packages

setup(
    name='packagebau',
    version='0.1.0',
    packages=find_packages(include=['packbau']),
    install_requires=[
        install_requires=[
    'numpy>=1.19.0',
    'pandas>=1.3.0',
    'matplotlib>=3.4.0',
    'requests>=2.25.0',
    'flask>=2.0.0',
    'sqlalchemy>=1.4.0',
    'Django>=3.2.0',
    'pytest>=6.2.0',
    'tensorflow>=2.5.0',
    'scikit-learn>=0.24.0',
],

    ],
    entry_points={
        'console_scripts': [
            'your_script_name = your_package.module1:main_function',
        ],
    },
    author='Abdullah Alhusam',
    author_email='abdullah.alhusam@bahcesehir.edu.tr',
    description='BAU final project',
    url='https://github.com/abdullahalhusam',
    license='BAU2282858',
)
