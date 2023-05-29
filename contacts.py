from faker import Faker

class BaseContact:
    def __init__(self, first_name, last_name, telephone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.email = email
        # Variables
        self._length = 0

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def contact(self):
        print(f"kontaktuję się z {self.first_name} {self.last_name} {self.email}")

    @property
    def label_length(self):
        self._length = len(self.first_name) + len(self.last_name) + 1
        return self._length


class BusinessContact(BaseContact):
    def __init__(self, job, company_name, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company_name = company_name
        self.business_phone = business_phone

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.company_name} {self.job} {self.business_phone}'

    def contact(self):
        print(f"kontaktuję się z {self.first_name} {self.last_name} {self.business_phone}")


base_list = []
business_list =[]

def create_contacts(contact_type, quantity):
    fake = Faker()

    if contact_type == "base":
        for _ in range(quantity):
            base_list.append(BaseContact(
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email()
            ))
    elif contact_type == "business":
        for _ in range(quantity):
            business_list.append(BusinessContact(
                fake.job(),
                fake.company(),
                fake.phone_number(),
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email()
            ))
    else:
        print("Nieprawidłowy rodzaj wizytówki. Dostępne opcje: 'base', 'business'")
    return

base = create_contacts("base", 5)
business = create_contacts("business", 2)


print("\nPodstawowe kontakty:")
for base_contact in base_list:
    print(base_contact)

print("\nBiznesowe kontakty:")
for business_contact in business_list:
    print(business_contact)


print("Kontakt:")
for kontakt in business_list:
    print(kontakt.contact())

print("Kontakt:")
for kontakt in base_list:
    print(kontakt.contact())

print("\nDługość imienia i nazwiska")
for element in business_list:
    print(element.label_length)
