from setuptools import setup

setup(
    name='als_patcher',
    version='1.0.0',
    description='Patch als file to another live version',
    author='izno',
    packages=['als_patcher'],
    package_data={'config': ['config/live_headers.ini']},
    entry_points={
            'console_scripts': [
                'als_patcher = als_patcher.als_patcher:main'
            ]
        },

)

