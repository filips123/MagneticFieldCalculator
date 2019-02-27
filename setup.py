from setuptools import setup

def readme():
    with open('README.md') as f:
            return f.read()

setup(
    name = 'magnetic-field-calculator',
    description = 'Python API for British Geological Survey magnetic field calculator',
    long_description = readme(),
    long_description_content_type='text/markdown',
    license = 'GPLv3+',

    version_format='{tag}',
    setup_requires=['setuptools-git-version'],

    packages = ['magnetic_field_calculator'],

    entry_points = {
        'console_scripts': ['magnetic-field-calculator=magnetic_field_calculator.__main__:main'],
    },

    extras_require = {
        'lint': ['pylint'],
    },

    python_requires = '>= 3.4',

    author = 'Filip Š',
    author_email = 'projects@filips.si',
    url = 'https://github.com/filips123/MagneticFieldCalculator/',
    keywords = 'british-geological-survey, geomag, magnetic-field, api, calculator',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: Physics',
    ],

    include_package_data = True,
)
