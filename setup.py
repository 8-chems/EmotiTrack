from setuptools import setup, find_packages

setup(
    name='sentiment-analysis-api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'transformers',
        'torch',
        'pandas',
        'scikit-learn',
    ],
)
