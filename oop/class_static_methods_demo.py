# class_static_methods_demo.py
# Demonstrates the difference between @staticmethod and @classmethod

from typing import Union

Number = Union[int, float]


class Calculator:
    """
    A simple Calculator showing:
    - @staticmethod: a function that doesn't need class or instance data
    - @classmethod: a function that receives the class as the first argument (cls)
    """

    # Class attribute that will be referenced by the class method.
    calculation_type: str = "Arithmetic Operations"

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """
        Static method example.

        Step-by-step:
        1. This method does not use `self` or `cls`.
        2. It's just a plain function placed inside the class namespace.
        3. Use it for functionality related to the class logically but not requiring
           access to class/instance data.
        """
        # Return the simple arithmetic sum
        return a + b

    @classmethod
    def multiply(cls, a: Number, b: Number) -> Number:
        """
        Class method example.

        Step-by-step:
        1. Receives `cls`, the class itself, as the first argument.
        2. Can access or modify class-level state (class attributes, other classmethods).
        3. Here we print the class attribute `calculation_type` before multiplying.
        """
        # Print the class attribute to demonstrate access to class-level data
        print(f"Calculation type: {cls.calculation_type}")
        # Return the product
        return a * b
