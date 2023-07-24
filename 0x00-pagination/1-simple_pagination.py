#!/usr/bin/env python3
""" A Module with class Sever """
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function that returns the start index and end index of page """
    st_ind = (page - 1) * page_size
    end_ind = st_ind + page_size
    return st_ind, end_ind


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get page from list of pages """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        st_ind, end_ind = index_range(page, page_size)
        Server.dataset(self)
        if len(self.__dataset) < end_ind:
            return []
        records = self.__dataset[st_ind: end_ind]
        return records
