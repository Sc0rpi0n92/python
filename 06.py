goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
features_add = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        features_add = input(f'Input feature "{f}" ')
        features[f] = int(features_add) if (f == 'price' or f == 'quantity') else features_add
        analytics[f].append(features[f])
    goods.append((num, features))

