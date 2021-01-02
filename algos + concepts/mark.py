def mark(function, test_cases):
    
    if function.__doc__:
        print()
        print(function.__doc__.upper())
        print()

    for i, test_case in enumerate(test_cases):
        test_input, expected_output = test_case

        if not isinstance(test_input, tuple):
            test_input = (test_input, )

        print(f'-----------[ Test Case {i + 1} ]-----------\n')
        print(f"Expected output: {expected_output}")
        actual = function(*test_input)
        print("Actual output:  ", actual)

        print()
