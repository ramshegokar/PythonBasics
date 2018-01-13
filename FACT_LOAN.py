import random


def disbdate():
    return str(random.randint(1, 29)).zfill(2) + '/' + str(random.randint(1, 12)).zfill(2) + '/' + str(random.randint(1970, 2010))


data = []


for i in range(10000000):
    business_date = str(random.randint(1, 29)).zfill(2) + '/' + str(random.randint(10, 12)).zfill(2) + '/' + '2017'
    ind = business_date
    outd = '31/12/2099'

    data.append(
        str(100080510+i) + ',' +
        random.choice(['AL' , 'PL' , 'HL']) + ',' +
        disbdate() + ',' +
        str(1000 + i) + ',' +
        str(random.randint(100000, 1500000)) + ',' +
        str(random.uniform(8.5, 14.5)) + ',' +
        str(random.randint(12,240)) + ',' +
        str(random.randint(1000, 30000)) + ',' +
        disbdate() + ',' +
        random.choice(['Active', 'Canceled', 'Closed']) + ',' +
        ind + ',' +
        outd
    )


with open('fact_loan.csv', 'w') as f:
    f.write('\n'.join(data))
