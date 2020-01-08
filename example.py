"""Example for magnetic field calculator API."""

from magnetic_field_calculator import MagneticFieldCalculator

def calculate_field_value(result):
    """Get and print field value."""

    field_value = result['field-value']
    declination = field_value['declination']
    inclination = field_value['inclination']
    total_intensity = field_value['total-intensity']
    north_intensity = field_value['north-intensity']
    east_intensity = field_value['east-intensity']
    vertical_intensity = field_value['vertical-intensity']
    horizontal_intensity = field_value['horizontal-intensity']

    print('FIELD VALUE:')
    print('Declination:', declination['value'], declination['units'])
    print('Inclination:', inclination['value'], inclination['units'])
    print('Total intensity:', total_intensity['value'], total_intensity['units'])
    print('North intensity:', north_intensity['value'], north_intensity['units'])
    print('East intensity:', east_intensity['value'], east_intensity['units'])
    print('Vertical intensity:', vertical_intensity['value'], vertical_intensity['units'])
    print('Horizontal intensity:', horizontal_intensity['value'], horizontal_intensity['units'])

def calculate_secular_variation(result):
    """Get and print secular variation."""

    secular_variation = result['secular-variation']
    declination = secular_variation['declination']
    inclination = secular_variation['inclination']
    total_intensity = secular_variation['total-intensity']
    north_intensity = secular_variation['north-intensity']
    east_intensity = secular_variation['east-intensity']
    vertical_intensity = secular_variation['vertical-intensity']
    horizontal_intensity = secular_variation['horizontal-intensity']

    print('SECULAR VARIATION:')
    print('Declination:', declination['value'], declination['units'])
    print('Inclination:', inclination['value'], inclination['units'])
    print('Total intensity:', total_intensity['value'], total_intensity['units'])
    print('North intensity:', north_intensity['value'], north_intensity['units'])
    print('East intensity:', east_intensity['value'], east_intensity['units'])
    print('Vertical intensity:', vertical_intensity['value'], vertical_intensity['units'])
    print('Horizontal intensity:', horizontal_intensity['value'], horizontal_intensity['units'])

def main():
    """Handle example."""

    # Create calculator with default WMM model and latest revision.
    calculator = MagneticFieldCalculator()

    # Get result
    result = calculator.calculate(latitude=-80, longitude=240, altitude=100, date='2027-07-02')

    # Calculate field value
    calculate_field_value(result)

    # Print newline
    print()

    # Calculate secular variation
    calculate_secular_variation(result)

if __name__ == '__main__':
    main()
