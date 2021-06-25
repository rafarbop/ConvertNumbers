from wtforms import Form, DecimalField


class FormDecimal(Form):
    number_in_decimal = DecimalField('Decimal Number')
    number_to_binary = DecimalField('Number in Binary')
    number_to_hexa = DecimalField('Number in Hexadecimal')
