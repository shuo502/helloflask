#!/usr/bin/env python
# encoding: utf-8


from setuptools import setup, find_packages

setup(
    name='MyApp',  # 应用名
    version='1.0',  # 版本号
    author_email = "shuo502@163.com",
    description = "This is a sample flask package",
    keywords = "hello world example",
    url = "http://example.com/HelloWorld/",   # 项目主页
    packages=find_packages(),  # 包括在安装包内的Python包
    include_package_data=True,  # 启用清单文件MANIFEST.in
    exclude_package_date={'': ['.gitignore']},
    install_requires=[  # 依赖列表
        'click >= 6.7',
        'Flask >= 0.12.2',
        'itsdangerous >= 0.24',
        'Jinja2 >= 2.10',
        'MarkupSafe >= 1.0',
        'Werkzeug >= 0.14.1'

    ]
)


if __name__ == '__main__':
    #pip freeze >requirements.txt
    #pip install -r requirements.txt

    pass


