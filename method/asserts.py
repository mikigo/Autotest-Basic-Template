
class Asserts:

    def assert_equal(self, actual, expected, message=None):
        if actual != expected:
            raise AssertionError(message or f"Expected {expected}, but got {actual}")

    def assert_true(self, condition, message=None):
        if not condition:
            raise AssertionError(message or "Expected condition to be True")

    def assert_false(self, condition, message=None):
        if condition:
            raise AssertionError(message or "Expected condition to be False")