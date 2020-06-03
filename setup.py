from setuptools import setup

__project__ = 'mcpimv'
__desc__ = 'Python library for the Minecraft Pi edition and RaspberryJuice API modified for use with multiverse'
__version__ = '2'
__author__ = "Martin O'Hanlon, rpahu32323"
__author_email__ = 'martin@ohanlonweb.com, rpahu32323@gmail.com'
__license__ = 'MIT'
__url__ = 'https://github.com/rpahu32323/mcpimv'

__classifiers__ = [
    "Development Status :: 1 - Planning",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

setup(name=__project__,
      version = __version__,
      description = __desc__,
      url = __url__,
      author = __author__,
      author_email = __author_email__,
      license = __license__,
      packages = [__project__],
      classifiers = __classifiers__,
      zip_safe=False)
