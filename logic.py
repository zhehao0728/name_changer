# -*- coding:utf-8 -*-
# AUTHOR: SUN

from os import path, listdir
from re import findall
from copy import copy


class error(BaseException):
    """
    所有异常的父类
    """
    pass


class same_name_error(error):
    """
    重名错误
    """
    pass


class re_error(error):
    """
    正则表达式语法错误
    """
    pass


class file_list(object):
    """
    一个用于存储文件路径的数据类型
    """
    def __init__(self):
        self._history = []  # 所有修改历史
        self._list = []  # 当前状况
        self._org = []

    def __getitem__(self, key):
        """
        使用file_list[0]获取值的方式
        :param key: 数据索引
        :return: 数据
        """
        return self._list[key]

    def __delitem__(self, key):
        """
        通过__delitem__调用del方法
        :param key: 索引
        """
        self._history.append(self._list)
        del self._list[key]

    def __len__(self):
        """
        通过__len__调用len()方法
        :return: 长度
        """
        return len(self._list)

    def __contains__(self, key):
        """
        通过__contains__调用in方法
        :param key: 关键词
        :return: bool
        """
        return key in self._list

    def add_file(self, value):
        """
        向列表中添加文件
        :param value: 文件路径
        """
        self._history.append(copy(self._list))
        self._list.append(value)

    def add_path(self, path_, search=False):
        """
        根据路径扫描文件
        :param path_: 路径
        :param search: 是否使用迭代
        :return: 扫描结果
        """
        self._history.append(copy(self._list))
        for i in listdir(path_):
            if path.isfile(path.join(path_, i)):
                self._list.append(path.join(path_, i))
            elif path.isdir(path.join(path_, i)) and search:
                self.add_path(path.join(path_, i), True)
        return self._list

    def roll_back(self):
        """
        回滚至上一个
        :return: 结果
        """
        self._history.append(copy(self._list))
        self._list = copy(self._history[-2])
        return self._list


class namer(file_list):
    """
    数据处理
    """
    def __iter__(self):
        return self

    def __next__(self):
        """
        迭代器
        :return: 路径，文件名，后缀
        """
        for i in self._list:
            yield path.splitext(i)

    def read(self):
        """
        :return: 当前结果(路径，文件名，后缀)
        """
        pa = []
        na = []
        su = []
        for i in self._list:
            i = path.splitext(i)
            pa.append(i[0])
            na.append(i[1])
            su.append(i[2])
        return pa, na, su


if __name__ == '__main__':
    pass
