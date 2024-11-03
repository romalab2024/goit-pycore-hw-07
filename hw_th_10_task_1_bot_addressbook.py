from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) not in (10, 12):
            raise ValueError("Invalid phone number format. Only digits are allowed and length must be 10 or 12.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday is None:
            return None
        today = datetime.now().date()
        next_birthday = self.birthday.value.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days

class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name.value] = record

    def get_upcoming_birthdays(self, days=7):
        today = datetime.now().date()
        upcoming_birthdays = []
        for record in self.records.values():
            if record.birthday:
                days_to_bday = record.days_to_birthday()
                if days_to_bday is not None and 0 < days_to_bday <= days:
                    upcoming_birthdays.append(record.name.value)
        return upcoming_birthdays
