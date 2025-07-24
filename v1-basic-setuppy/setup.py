from setuptools import setup, find_packages

with open('v1-basic-setuppy\\requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="my_package",
    version="0.1",
    include_package_data=True,
    python_requires='>=3.8',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    author="Abdellah HALLOU",
    author_email="abdeallahhallou33@gmail.com",
    description="A short description of your package",
    long_description=open('v1-basic-setuppy\\README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.12.4",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    version_config={
       "dirty_template": "{tag}",
    }
)

# python setup.py sdist bdist_wheel
# .venv\Scripts\python.exe "C:\Users\Apró Gergely\Python_programs_by_APRG\test-packaging\v1-basic-setuppy\setup.py" sdist bdist_wheel