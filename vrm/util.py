#!/usr/bin/env python
def unique(seq):
    """
    :param seq: リスト
    :return: 重複のないリストを返す
    """
    new_list = []
    for x in seq:
        if x not in new_list:
            new_list.append(x)
    return new_list
