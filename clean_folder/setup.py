from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Sort and clean your folders',
    url = 'https://github.com/sholohova27/homework_6',
    author='Natalia Sholohova',
    author_email='n.sholohova27@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['pathlib', 'os', 'shutil', 'sys'],
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']}
)

