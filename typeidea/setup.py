from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='0.1',
    description='Blog system base on python',
    author='Blank',
    author_email='Blank@qq.com',
    url='http://www.blankblog.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    packages_date={'': [
        'themes/*/*/*/*',
    ]},
    # include_package_data=True,
    install_require=[
        'django~=1.11',
    ],
    extras_requires={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'manage.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage.main',
        ]
    },
    classifiers=[
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topics :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming language :: Python :: 3.6'
    ],
)