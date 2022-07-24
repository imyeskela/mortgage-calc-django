import random
from .models import Mortgage


def _random_bank_name():
    bank_names = ['SBER', 'VTB', 'RAIFEZENBANK', 'CITYBANK', 'DOICHEBANK', 'RNBANK']
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
    return mortgage_data


def _get_mortgages_by_name(mortgage_data, bank_name_filter):
    return list(filter(lambda x: x['bank_name'] == bank_name_filter, mortgage_data))


def _get_mortgages_by_rate(mortgage_data, rate_min_filter, rate_max_filter):
    return list(filter(lambda x: rate_min_filter <= x['rate'] <= rate_max_filter, mortgage_data))


def get_filtered_mortgages(mortgage_data, bank_name_filter, rate_min_filter, rate_max_filter):
    if (bank_name_filter != None) or (rate_min_filter != None and rate_max_filter != None):

        if (bank_name_filter != None) and (rate_min_filter != None and rate_max_filter != None):
            by_name = _get_mortgages_by_name(mortgage_data, bank_name_filter)
            return _get_mortgages_by_rate(by_name, rate_min_filter, rate_max_filter)

        elif bank_name_filter != None:
            return _get_mortgages_by_name(mortgage_data, bank_name_filter)

        else:
            return _get_mortgages_by_rate(mortgage_data, rate_min_filter, rate_max_filter)

    else:
        return mortgage_data


def save_data(json_data):
    for json_list in json_data:
        Mortgage.objects.create(**json_list)

