Magnetic field calculator
=========================

[![Latest Version][icon-version]][link-pypi]
[![Total Downloads][icon-downloads]][link-pypi]
[![License][icon-license]][link-license]
[![Build Status][icon-travis]][link-travis]

Python API for British Geological Survey magnetic field calculator.

## Description

This project magnetic field calculator. It uses is British Geological Survey (BGS) API web service for calculation.

The web service makes the World Magnetic Model (WMM), the International Geomagnetic Reference Field (IGRF) and the BGS Global Geomagnetic Model (BGGM) available as a web service. The IGRF and WMM have no restrictions on use, the BGGM is only available to subscribers. The API provides options to select which model and revision to use. Values of the magnetic field at any point around the world can be retrieved for a given date.

**The project is not part of the BGS. It is just API client for it, made by community. For any information about BGS, you should use [the official website][link-bgs].**

## Usage

First, you need to import the calculator class:

```python
from magnetic_field_calculator import MagneticFieldCalculator
```

Then you need to init the calculator client, with default WMM model and it's latest available version:

```python
calculator = MagneticFieldCalculator()
```

Model, it's revisions and custom URS can be changed with parameters:

```python
calculator = MagneticFieldCalculator(
    model='wmm',
    revision='2020',
    sub_revision='2',
    custom_url='https://example.com'
)
```

You can then get the calculations for given location:

```python
result = calculator.calculate(
    latitude=-80,
    longitude=140,
    altitude=200,
    date='2028-12-31'
)
```

The only required parameters are latitude and longitude, but it is reccomended to also set others for best results. Some of them are exclusive and you should not use them at same time. You can also set username and password for HTTP auth for protected models. For more details about parameters, see [the official documentation][link-parameters].

Output is returned as dictionary:

```python
field_value = result['field-value']
declination = field_value['declination']
inclination = field_value['inclination']
total_intensity = field_value['total-intensity']
north_intensity = field_value['north-intensity']
east_intensity = field_value['east-intensity']
vertical_intensity = field_value['vertical-intensity']
horizontal_intensity = field_value['horizontal-intensity']
```

Some output properties will have `units` and `value` sub properties. Output format will depend on used input, specially for height and date.

You can also look to [example file][link-example] for more examples.

## Versioning

This library uses [SemVer][link-semver] for versioning. For the versions available, see [the tags][link-tags] on this repository.

## License

This library is licensed under the GPLv3+ license. See the [LICENSE][link-license-file] file for details.

[icon-version]: https://img.shields.io/pypi/v/magnetic-field-calculator.svg?style=flat-square&label=version
[icon-downloads]: https://img.shields.io/pypi/dm/magnetic-field-calculator.svg?style=flat-square&label=downloads
[icon-license]: https://img.shields.io/pypi/l/magnetic-field-calculator.svg?style=flat-square&label=license
[icon-travis]: https://img.shields.io/travis/com/filips123/MagneticFieldCalculator.svg?style=flat-square&label=build+status

[link-pypi]: https://pypi.org/project/magnetic-field-calculator/
[link-license]: https://choosealicense.com/licenses/gpl-3.0/
[link-semver]: https://semver.org/
[link-travis]: https://travis-ci.com/filips123/MagneticFieldCalculator/

[link-example]: https://github.com/filips123/MagneticFieldCalculator/blob/master/example.py
[link-tags]: https://github.com/filips123/MagneticFieldCalculator/tags/
[link-license-file]: https://github.com/filips123/MagneticFieldCalculator/blob/master/LICENSE

[link-bgs]: https://bgs.ac.uk/
[link-parameters]: http://geomag.bgs.ac.uk/web_service/GMModels/help/parameters
