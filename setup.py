"""
Setups the src folder as local package for installation.
"""

from setuptools import find_packages, setup

setup(
    name = "AI Medical Chatbot using Llama 2",
    version="0.0.0",
    author="Caner Karaoğlu",
    author_email="caner_karaoglu@hotmail.com",
    packages=find_packages(),
    install_requires=[]
)