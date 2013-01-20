import datetime


EPOCH = datetime.date(1970, 1, 1)


class DBType(object):
    def to_primitive(self, value):
        if type(value) == self.primitive:
            return value
        else:
            raise NotImplementedError

    def to_present(self, value):
        if type(value) == self.present:
            return value
        else:
            raise NotImplementedError


class IntegerType(DBType):
    present = int
    primitive = int


class FloatType(DBType):
    present = float
    primitive = float

    def to_primitive(self, value):
        if type(value) == int:
            value = float(value)

        return super(FloatType, self).to_primitive(value)


class DateType(DBType):
    present = datetime.date
    primitive = float

    def to_primitive(self, value):
        return datetime.datetime.combine(value, datetime.time()).timestamp()

    def to_present(self, value):
        return datetime.datetime.fromtimestamp(value).date()


class TimeType(DBType):
    present = float
    primitive = datetime.time

    def to_primitive(self, value):
        return datetime.datetime.combine(EPOCH, value).timestamp()

    def to_present(self, value):
        return datetime.datetime.fromtimestamp(value).time()


class DateTimeType(DBType):
    present = float
    primitive = datetime.datetime

    def to_primitive(self, value):
        print(value)
        return value.timestamp()

    def to_present(self, value):
        print(value)
        return datetime.datetime.fromtimestamp(value)
