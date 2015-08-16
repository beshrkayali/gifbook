from distutils.core import setup
setup(
    name='gifbook',
    version='0.0.1',
    description='GifBook: Create sequenced Gifs from video clips and subtitles',
    author='Beshr Kayali',
    author_email='beshrkayali@gmail.com',
    maintainer='Besh Kayali',
    maintainer_email='beshrkayali@gmail.com',
    url='https://github.com/beshrkayali/gifbook/',
    download_url='https://github.com/beshrkayali/gifbook/',
    license='GNU GPL',
    install_requires=['pysrt', 'MoviePy'],
    packages=['gifbook'],
)
