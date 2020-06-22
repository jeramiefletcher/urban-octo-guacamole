import setuptools
from distutils.command.install import INSTALL_SCHEMES


for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

try:
    from workingdays._version import version as __version__
except ImportError:
    __version__ = 'unknown'


setuptools.setup(
    name='workingdays',
    version=__version__,
    description='A collection of Workingdays date utilities/helper functions.',
    author="Jeramie Fletcher",
    author_email="jeramie.fletcher@gmail.com",
    url="https://github.com/jeramiefletcher/workingdays",
    license="GNU General Public License v3.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False)
