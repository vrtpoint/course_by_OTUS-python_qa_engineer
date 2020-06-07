from setuptools import setup, find_packages

setup(
    name='course_by_OTUS-python_qa_engineer',
    version='0.1',
    url='https://github.com/vrtpoint/course_by_OTUS-python_qa_engineer',
    license='MIT',
    author='vrtpoint',
    author_email='vrtpoint@gmail.com',
    description='Python QA Engineer',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'pytest==5.3.5',
        'requests== 2.23.0',
        'selenium==3.141.0'
    ],
    zip_safe=False
)