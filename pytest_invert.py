from invert import invert

def test_invert():
    # mock data postive test data
    data = ['abcd', 'a', None]
    excepted_data = ['dcba', 'a', '']
    for i, v in enumerate(data):
       assert invert(v) == excepted_data[i]

    #negative test data
    s = invert('abcd')
    assert s != 'abdc'


if __name__ == '__main__':
    test_invert()
