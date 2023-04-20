# Test cases

def test_function():
    test_cases = [
        {'input': 'a = [1, 2, 3], b = [2, 3, 4]', 'output': '[1]'},
        {'input': 'a = [1, 2, 3], b = [4, 5, 6]', 'output': '[1, 2, 3]'},
        {'input': 'a = [1, 1, 1], b = [1, 2, 3]', 'output': '[]'},
        {'input': 'a = [], b = [1, 2, 3]', 'output': '[]'},
        {'input': 'a = [1, 2, 3], b = []', 'output': '[1, 2, 3]'},
    ]

    for case in test_cases:
        input_str = case['input']
        expected_output_str = case['output']
        inputs = tuple(map(eval, input_str.split(',')))
        expected_output = eval(expected_output_str)

        # Ensure the function is correct
        assert function(*inputs) == expected_output

        # Ensure str -> variable -> str consistency, while ignoring leading/trailing white space
        assert input_str.strip() == repr(tuple(map(eval, input_str.strip().split(',')))).strip()
        assert expected_output_str.strip() == repr(expected_output).strip()

        # Ensure variable -> str -> variable consistency
        assert inputs == tuple(map(eval, repr(inputs).strip()))
        assert expected_output == eval(repr(expected_output).strip())

    print('All test cases pass')

if __name__ == '__main__':
    test_function()