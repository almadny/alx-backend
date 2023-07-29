#!/usr/bin/env python3
""" A Module with class Sever """
import csv
import math
from typing import List
from typing import Tuple
from typing import Dict


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
        self.__records = None

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
        self.dataset()
        if len(self.__dataset) < end_ind:
            return []
        self.__records = self.__dataset[st_ind: end_ind]
        return self.__records

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """ Returns a dictionary of page navigation information """
        info = {}
        data = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.__dataset) / page_size)

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        info['page_size'] = page_size
        info['page'] = page
        info['data'] = data
        info['next_page'] = next_page
        info['prev_page'] = prev_page
        info['total_pages'] = total_pages

        return info
