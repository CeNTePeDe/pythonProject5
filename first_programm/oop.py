class ContactList(list):
    # наследуется от кдасса list
    def seach(self, name):
        """Return all contacts that contain the search values in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Suppliers(Contact):
    def order(self, order):
        print(
            "if this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )


c1 = Contact('Misha 1', 'misha@mail.ru')
c2 = Contact('Misha 2', 'misha2@mail.ru')
c3 = Contact('Olga 1', 'olga1@mail.ru')
s1 = Suppliers(c1.name, c1.email)
s2 = Suppliers(c2.name, c2.email)
s3 = Suppliers(c3.name, c3.email)

if __name__ == '__main__':
    # print(Contact.all_contacts)
    # print([c.name for c in Contact.all_contacts])
    # print([c.email for c in Contact.all_contacts])
    print(s1.order('orders'))
