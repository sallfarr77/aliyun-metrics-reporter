from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='aliyun-metrics-reporter',  
    version='0.1.0',  
    author='sallfarr77',  
    author_email='sallfarr@outlook.com', 
    description='A tool to report and analyze Aliyun ECS and CMS metrics', 
    long_description=long_description,  
    long_description_content_type='text/markdown',  
    url='https://github.com/sallfarr77/aliyun-metrics-reporter',  
    packages=find_packages(where='src'),  
    package_dir={'': 'src'}, 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
    install_requires=[
        'alibabacloud_ecs20140526',
        'alibabacloud_tea_openapi',
        'aliyunsdkcms',
        'aliyunsdkcore',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'aliyun-metrics-reporter=main:main',  
        ],
    },
)
