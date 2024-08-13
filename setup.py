from setuptools import setup, find_packages

setup(
    name='Dokyumento',
    version='1.0.0',
    author='sebidev',
    author_email='sebidev@hotmail.com',
    description='Dokyumento is a simple Markdown documentation generator for many popular programming languages. Easily extensible and easy to use.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sebidev/Dokyumento',
    packages=find_packages(where='.', include=['languages', 'languages.*']),
    entry_points={
        'console_scripts': [
            'dokyumento=cli:main',
        ],
    },
    install_requires=[
        # Add any dependencies your project needs here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
