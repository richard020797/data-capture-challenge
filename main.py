"""Main file package for DataCapture module.
"""
# TODO: If a base module is set, thi import should be relocated there.
from typing import Optional

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
        storage.sort()
        self.storage = storage 

    def less(self, value: int) -> Optional[list[int]]:
        """Returns values from self.storage that are lower than the provided value (x < value).
        Args:
            value (int): The value to be compared to.
        Returns:
            Optional(list(int)): The list of values lower than `value` if any, else empty list.
        """
        return [e for e in self.storage if e < value]

    def greater(self, value: int) -> Optional[list[int]]:
        """Returns values from self.storage that are greater than the provided value (x > value).
        Args:
            value (int): The value to be compared to.
        Returns:
            Optional(list(int)): The list of values greater than `value` if any, else empty list.
        """
         return [e for e in self.storage if e > value]

    def between(self, lower_value: int, upper_value: int) -> Optional[list[int]]:
        """Returns values from self.storage that are between the provided values 
            (lower_value <= x <= upper_value).
        Args:
            lower_value (int): The value to be compared to.
            upper_value (int): The value to be compared to.
        Returns:
            Optional(list(int)): The list of values between lower_value and upper_value if any,
            else empty list.
        """
        return [e for e in self.storage if lower_value <= e <= upper_value]



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
        self.storage = list()

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
                raise ValueError('Provided type value is not integer.')
            self.storage.append(value)
            return True
        except e:
            # TODO: Move error printing into logger structure and add log file in .gitignore.
            print(f'Exception {e}')
            return False

    def build_stats(self) -> DataStats:
        """Creates, orders and sets the stored values for the subsequent stats operations.
        Args:
        Returns:
            DataStats: If the Stats build was successful.
        """
        return DataStats(self.storage)

