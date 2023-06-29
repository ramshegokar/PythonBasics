import random
import string


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


cust_id = 10000
loan_type_list = ['HL', 'PL', 'AL', 'CC', 'GL', 'TWL']
city_list = ['Pune', 'Mumbai', 'Aurangabad', 'Akola', 'Nagar', 'Shegaon']


def gen_dob():
    return str(random.randint(1, 29)).zfill(2) + '/' + str(random.randint(1, 12)).zfill(2) + '/' + str(random.randint(1970, 2010))


def gen_pan():
    return random_char(5) + ''.join(str(random.randint(0,9)) for x in range(4)) + random_char(1)


def gen_mobile():
    return ''.join(str(random.randint(8,9)) for x in range(2))+ ''.join(str(random.randint(0,9)) for x in range(8))


def gen_email():
    return random_char(5) + '@gmail.com'


state = 'Maharashtra'


def zipcode():
    return ''.join(str(random.randint(0,9)) for x in range(6))


business_date = str(random.randint(1, 29)).zfill(2) + '/' + str(random.randint(10, 12)).zfill(2) + '/' + '2017'
ind = business_date
outd = '31/12/2099'

data = []

for i in range(10):
    data.append(
        str(1000+i) + ',' +
        gen_dob() + ',' +
        gen_pan() + ',' +
        gen_mobile()+ ',' +
        gen_email() + ',' +
        random.choice(city_list) + ',' +
        zipcode() + ',' +
        business_date + ',' +
        ind + ',' +
        outd)


with open('dim_customer.csv', 'w') as f:
    f.write('\n'.join(data))

