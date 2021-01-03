from setuptools import find_packages, setup
setup(
    name='Wrencher',
    packages=find_packages(include=['Wrench']),
    version='0.1.9',
    description='Cool lib',
    author='Rostcraft',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
