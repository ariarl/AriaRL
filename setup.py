import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='ariarl',  
     version='0.1',
     scripts=['ariarl'] ,
     author="HAMIDULLAH Yasser",
     author_email="yasserhamidullah@gmail.com",
     description="A Reinforcement Learning Framework",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ariarl/AriaRL",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: MIT License",
         "Operating System :: OS Independent",
     ],
 )