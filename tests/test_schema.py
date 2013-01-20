import datetime
import unittest

from pydb import types


class SchemaTest(unittest.TestCase):

    def testIntegerTypeConversion(self):
        field = types.IntegerType()
        value = 1
        self.assertEqual(field.to_primitive(value), value)
        self.assertEqual(field.to_present(value), value)

    def testFloatTypeConversion(self):
        field = types.FloatType()

        value = 1
        self.assertEqual(field.to_primitive(value), float(value))

        value = 1.0
        self.assertEqual(field.to_primitive(value), value)
        self.assertEqual(field.to_present(value), value)

    def testDateTypeConversion(self):
        field = types.DateType()
        value = datetime.date(1970, 1, 1)
        primitive = field.to_primitive(value)
        self.assertEqual(field.to_present(primitive), value)

    def testTimeTypeConversion(self):
        field = types.TimeType()
        value = datetime.time(1, 1, 1)
        primitive = field.to_primitive(value)
        self.assertEqual(field.to_present(primitive), value)

    def testDateTimeTypeConversion(self):
        field = types.DateTimeType()
        value = datetime.datetime(1970, 1, 1, 1, 1, 1)
        primitive = field.to_primitive(value)
        self.assertEqual(field.to_present(primitive), value)
