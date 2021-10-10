import os
from distutils.core import setup
from setuptools import find_packages

from renxianqi.setting import NAME,VERSION

README_RST = os.path.join(os.getcwd(), "README.rst")
with open(README_RST, 'r') as rfile:
    LONG_DESCRIPTION = rfile.read()


setup(name="qingdian",  # 包名
      version=VERSION,  # 版本号
      description='A small tool to check the absentee',
      long_description=LONG_DESCRIPTION if LONG_DESCRIPTION else "Powered by py4u (LeiXueWei). This tool is very useful to check the absentee for any activities!",
      author='levin',
      author_email='991219092@qq.com',
      url='https://blog.csdn.net/geeklevin',
      install_requires=["pypinyin","pyperclip"],
      license='Apache License 2.0',
      packages=find_packages(),
      platforms=["all"],
      entry_points={
          'console_scripts': [
              'rxq = renxianqi.main:main',
              'renxianqi = renxianqi.main:main',
              'qingdian = renxianqi.main:main',
          ]
      },
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )
