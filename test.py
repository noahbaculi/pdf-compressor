import unittest

inputs = {
    'Children': ['Snow', 'Car', 'Fluffes', 'Snow', 'Acute', 'Age'],
    'Stars': ['Car', 'Hexagon', 'Year'],
    'Hearts': ['Car', 'Fluffes', 'Year', 'Orange'],
}

correct_outputs = {
    'Children': 3,
    'Stars': 1,
    'Hearts': 1,
}


def foo(input_dict):

    output = input_dict

    print(output)
    return output


if __name__ == '__main__':
    print(foo(inputs))
    # unittest.main()
    assert foo(inputs) == correct_outputs, "Should be correct"
