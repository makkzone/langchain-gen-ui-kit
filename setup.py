from setuptools import setup, find_packages

setup(
    name='gen_ui_kit',
    version='0.1.0',
    description='Gen-UI-Kit is a developer tool that generates starter web UI kits based on project ideas and descriptions. Leveraging LangChain and Cloudscape Design System, it simplifies the process of starting a project by providing a customizable UI kit. Developers can easily connect the generated kit to their APIs or backends, accelerating the early stages of development for new apps or front-end interfaces.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    author='Manojkumar Kotakonda',
    author_email='manojkumar.kotakonda@gmail.com',
    url='https://github.com/makkzone/Gen-UI-Kit', 
    packages=find_packages(), 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        "langchain==0.3.2","gitpython==3.1.43",
    ],
)