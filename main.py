#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main file package for DataCapture module.
"""
import logging
from typing import Optional

logging.basicConfig(
        filename="logs.txt", encoding="utf-8", level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s"
)


class DataStats:
    """Handler for statistics operations.
    E.g.
    less, greater, between.
    """

    def __init__(self, storage: list[int]) -> None:
        """Will create a statistics handler.
        Args:
            storage (list(int)): A list of values to run stats operations over, Usually comes
                from DataCapture.storage.
        Return:
            None
        """
        self.storage = storage 

    def less(self, value: int) -> Optional[list[int]]:
        """Returns n count of values from self.storage that are lower than the provided value (x < value).
        Args:
            value (int): The value to be compared to, should be between 0 - 999.
        Returns:
            int: N values lower than `value`.
        """
        return sum(self.storage[:value])

    def greater(self, value: int) -> Optional[list[int]]:
        """Returns n count of values from self.storage that are greater than the provided value (x > value).
        Args:
            value (int): The value to be compared to, should be between 0 - 998.
        Returns:
            int: N values greater than `value`.
        """
        return sum(self.storage[value + 1:])

    def between(self, lower_value: int, upper_value: int) -> Optional[list[int]]:
        """Returns n count of values from self.storage that are between the provided values 
            (lower_value <= x <= upper_value).
        Args:
            lower_value (int): The value to be compared to, should be between 0 - 999.
            upper_value (int): The value to be compared to, should be between 0 - 998.
        Returns:
            int: N values between lower_value and upper_value.
        """
        return sum(self.storage[lower_value:upper_value + 1])



class DataCapture:
    """Main Class for capturing, handling, and processing the data statistics.
    E.g.
    `A program that computes some basic statistics on a collection of small positive integers.
    You can assume all values will be less than 1,000.`
    """

    def __init__(self) -> None:
        """Will create a handler that provides the input interface and further transforms into
        the stats by a build_stats method.
        """
        self.storage = [0] * 1000

    def add(self, value: int) -> bool:
        """Sorted insertion of the provided value (int) into the self.storage list.
        Args:
            value (int): The value to be inserted.
        Returns:
            bool: If the insertion was successful.
        Raises:
            ValueError if value type is not int.
        """
        try:
            if type(value) != int:
                raise ValueError("Provided type value is not integer.")
            if value > 999:
                raise ValueError("Provided value should be integer less than 1000.")
            self.storage[value] += 1
            return True
        except Exception as e:
            logging.error(f"Exception: {e}")
            return False

    def build_stats(self) -> DataStats:
        """Creates and sets the stored values for the subsequent stats operations.
        Args:
        Returns:
            DataStats: If the Stats build was successful.
        """
        return DataStats(self.storage)

