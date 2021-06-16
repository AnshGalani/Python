from faker import Faker

fake=Faker()

'''for i in range(0 ,5):
    print("Name-->",fake.name())
'''
print("Name   :",fake.name())
print("Email   :",fake.email())
print("Country   :",fake.country())
print("Text   :",fake.text())
print("Url   :",fake.url())