


ab = 'PING api1.intellitrain.emdiesels.com (12.108.237.208) 56(84) bytes of data.'

print(ab[38:52])

output =  ['Server:    0.0.0.0\n', 'Address 1: 0.0.0.0\n', '\n', 'Name:      12.108.237.208\n', 'Address 1: 12.108.237.208 api1.intellitrain\n']

api3 = []

for element in output:
    api3.append(element.strip())

print(api3)

if api3.__contains__('12.108.237.208'):
    print('yes')
else:
    print('no')