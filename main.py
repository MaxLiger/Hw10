from collections import UserDict


class Field:
    def __init__(self, raw_data) -> None:
        self.value = raw_data


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = [phone] if phone else []
        # if phone:
        #     self.phones.append(phone)
    
    
    def add_phone(self, new_phone: str):
        phone = Phone(new_phone)
        self.phones.append(phone)
        print(f'Phone {phone.value} added')


    def delete_phone(self, target_phone: str):
        phone = Phone(target_phone)
        for ph_obj in self.phones:
            if ph_obj.value == phone.value:
                self.phones.remove(ph_obj)
                print(f'Phone {ph_obj.value} removed')


    def change_phone(self, changed_phone: str, phone: str):
        old_phone = Phone(changed_phone)
        new_phone = Phone(phone)
        for ph_obj in self.phones:
            if ph_obj.value == old_phone.value:
                self.phones.remove(ph_obj)
                self.phones.append(new_phone)
                print(f'Phone {ph_obj.value} changed to {new_phone.value}')


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record




if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    print(name.value)
    print(phone.value)
    rec = Record(name, phone)
    print(rec.name.value)
    rec.add_phone('098763')
    print(rec.phones)
    # rec.delete_phone('098763')
    # print(rec.phones)
    rec.change_phone('098763', '00')
    print(rec.phones)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')