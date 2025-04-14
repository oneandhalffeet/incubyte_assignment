import pytest
from app import add

def test_add_for_empty_string():
    assert add("") == 0
    assert add("2") == 2

    print("✓ All add tests passed!")


if __name__ == "__main__":
    try:
        test_add_for_empty_string()
    except ImportError:
        print("❌ Test failed: calculator.py or add function not found")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
