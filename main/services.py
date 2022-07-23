import random
import json
from .models import Mortgage


def _random_bank_name():
    bank_names = ['SBER', 'VTB', 'RAIFEZENBANK', 'ROSBANK', 'UNICREDITBANK', 'CITYBANK', 'DOICHEBANK',
                  'RNBANK']
    return random.choice(bank_names)


def get_mortgage_list(price, initial_fee, term):
    credit_amount = price - initial_fee
    i = 0.5
    mortgage_data = []
    while i != 10.0:
        if i >= 10.0:
            i = 0.5
            break
        i += 0.5
        rate = round(i % 12, 1)
        formula = (credit_amount * rate) // (1 - (1 + rate) * (1 - term))
        mortgage_data.append(dict({'bank_name': _random_bank_name(), 'payment': int(formula), 'rate': float(rate)}), )
    # json_data = json.dumps({'bank_name': _random_bank_name(), 'payment': str(formula), 'rate': str(rate)})
    # print(mortgage_data)
    return mortgage_data


def save_data(json_data):
    for json_list in json_data:
        Mortgage.objects.create(**json_list)