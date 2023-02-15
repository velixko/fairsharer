from fairsharer import fair_sharer

def test_fair_sharer():
    #Test 1:
    values = [0, 1000, 800, 0]
    num_iterations = 2
    expected_output = [100.0, 890.0, 720.0, 90.0]
    output = fair_sharer(values, num_iterations)
    assert output == expected_output
    #Test 2:
    values = [0, 1000, 800, 0]
    num_iterations = 2
    expected_output = [100.0, 890.0, 720.0, 90.0]
    output = fair_sharer(values, num_iterations)
    assert output == expected_output