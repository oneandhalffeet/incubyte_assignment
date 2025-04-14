import pytest
from app import add

def test_add_for_empty_string():
    assert add("") == 0
    assert add("2") == 2
    print("✓ All add tests passed-test_add_for_empty_string")


def test_add_for_comma_separated_values():
    assert add("1,2") == 3
    assert add("1,2,3") == 6
    assert add("1,2,3,4") == 10
    assert add("1,5") == 6
    print("✓ All add tests passed-test_add_for_comma_separated_values")

def test_add_for_newline_separated_values():
    assert add("1\n2") == 3
    assert add("1\n2,3") == 6
    assert add("1\n2,3\n4") == 10
    print("✓ All add tests passed-test_add_for_newline_separated_values")

def test_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//^\n1^2^3") == 6
    assert add("//*\n1*2*7") == 10
    assert add("//;\n1;2,3\n40") == 46
    assert add("//-\n1-2,3\n4,5") == 15
    print("✓ All add tests passed-test_custom_delimiter")

def test_negative_numbers():
    with pytest.raises(Exception, match="negative numbers not allowed -2"):
        add("1,-2")
    with pytest.raises(Exception, match="negative numbers not allowed -1,-2"):
        add("-1,-2")
    with pytest.raises(Exception, match="negative numbers not allowed -1,-2,-3"):
        add("-1,-2,-3")
    print("✓ All add tests passed-test_negative_numbers")


def test_numbers_bigger_than_1000():
    assert add("1,2,3,1001") == 6
    assert add("1,2,3,1000") == 1006
    assert add("1,2,3,1000,1001") == 1006
    print("✓ All add tests passed-test_numbers_bigger_than_1000")

def test_delimiter_of_any_length():
    assert add("//[***]\n1***2***3") == 6
    assert add("//[*#]\n1*#2*#3,4") == 10
    print("✓ All add tests passed-test_delimiter_of_any_length")

def test_big_delimiters():
    assert add("//[***]\n1***2***3") == 6
    assert add("//[***]\n1***2***3,4") == 10
    print("✓ All add tests passed-test_big_delimiters")

def test_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6
    assert add("//[*][%][#]\n1*2%3#4") == 10
    print("✓ All add tests passed-test_multiple_delimiters")


if __name__ == "__main__":
    try:
        test_add_for_empty_string()
        test_add_for_comma_separated_values()
        test_add_for_newline_separated_values()
        test_custom_delimiter()
        test_negative_numbers()
        test_numbers_bigger_than_1000()
        test_delimiter_of_any_length()
        test_big_delimiters()
        test_multiple_delimiters()
        print("✓ All add tests passed")
    except ImportError:
        print("❌ Test failed: calculator.py or add function not found")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
