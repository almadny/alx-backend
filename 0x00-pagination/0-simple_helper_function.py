#!/usr/bin/env python3
""" Module that defines a index range class """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function that returns the start index and end index of page """
    st_ind = (page - 1) * page_size
    end_ind = st_ind + page_size
    return st_ind, end_ind
