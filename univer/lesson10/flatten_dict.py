d = {
    'one': {
        'two': 2,
        'three': 3,
        'four':
            {'4': 4}
    },
    'two': 22,

}

new_dict = {}


def flatten(d: dict, path):
    for k, v in d.items():
        name = '.'.join([path, k]) if path else k
        if isinstance(v, dict):
            flatten(v, name)
        else:
            new_dict[name] = v


flatten(d, '')

print(new_dict)





# {'one.two': 2, 'one.three': 3, 'one.four.4': 4, 'two': 22}