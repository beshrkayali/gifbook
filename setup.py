from pip.req import parse_requirements
from setuptools import setup

install_reqs = parse_requirements('requirements.txt')

setup(
    name='gifbook',
    version='0.0.1',
    description='GifBook: Create sequenced Gifs from video clips and subtitles',
    author='Beshr Kayali',
    author_email='beshrkayali@gmail.com',
    maintainer='Besh Kayali',
    maintainer_email='beshrkayali@gmail.com',
    url='https://github.com/beshrkayali/gifbook/',
    # download_url='https://github.com/beshrkayali/gifbook/',
    license='GNU GPLv3',
    install_requires=[str(ir.req) for ir in install_reqs],
    data_files=[('requirements.txt', ['requirements.txt'])],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ],
    py_modules=['gb', 'gb_generate'],
    entry_points='''
        [console_scripts]
        gifbook=gb_generate:cli
    '''
)
