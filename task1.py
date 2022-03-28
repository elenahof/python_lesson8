import datetime


class Data:

    def __init__(self, dat):
        self.dat = str(dat)

    def __str__(self):
        try:
            datetime.datetime.strptime(self.dat, '%d-%m-%Y')
            return self.dat
        except ValueError:
            raise ValueError("Wrong format input!")

    @classmethod
    def number_format(cls, num):
        return num.dat.split('-')

    @staticmethod
    def validate(self):
        a = self.dat.split('-')
        if 1 <= int(a[0]) <= 31:
            if 1 <= int(a[1]) <= 12:
                if 0 <= int(a[2]) <= 9999:
                    return "Right format of the date"
                else:
                    return "Wrong year format"
            else:
                return "Wrong month format"
        else:
            return "Wrong day format"


date = Data("14-09-2007")
print(date)
print(Data.number_format(date))
print(Data.validate(date))
