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
    assert add("//*\n1*2*3*4") == 10
    assert add("//;\n1;2,3\n4") == 10
    print("✓ All add tests passed-test_custom_delimiter")



if __name__ == "__main__":
    try:
        test_add_for_empty_string()
        test_add_for_comma_separated_values()
        test_add_for_newline_separated_values()
        test_custom_delimiter()
    except ImportError:
        print("❌ Test failed: calculator.py or add function not found")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
