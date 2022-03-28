# -*- coding:utf-8 -*-

# ======================================================================================================================
# NAME CHANGER
# AUTHOR: SUN
# DESCRIPTION: 类
# ======================================================================================================================
import re
from copy import copy
from os.path import splitext


class name_change_exception(BaseException):
    pass


class value_number_error(name_change_exception):
    pass


class same_name_error(name_change_exception):
    pass


class name_list(object):
    def __init__(self):
        self.org_name = []
        self.name_history = []
        self.last_names = []

    def set_org_names(self, names):
        self.org_name = copy(names)
        self.name_history.clear()
        self.name_history.append(copy(names))
        self.last_names = copy(names)

    def delete_words(self, word):
        for index, i in enumerate(self.last_names):
            i = i.replace(word, '')
            self.last_names[index] = i
        self._same_name_test()
        self.name_history.append(copy(self.last_names))
        return self.last_names

    def replace_words(self, word, new_word):
        for index, i in enumerate(self.last_names):
            i = i.replace(word, new_word)
            self.last_names[index] = i
        self._same_name_test()
        self.name_history.append(copy(self.last_names))
        return self.last_names

    def list_replace(self, order, name=''):
        if order:
            self.last_names.reverse()
        for index, i in enumerate(self.last_names):
            f = splitext(i)[1]
            inde = index+1
            if inde < 10:
                inde = '0'+str(inde)
            else:
                inde = str(inde)
            i = name+inde+f
            self.last_names[index] = i
        self._same_name_test()
        if order:
            self.last_names.reverse()
        self.name_history.append(copy(self.last_names))
        return self.last_names

    def re_change(self, key, form):
        for index, i in enumerate(self.last_names):
            key_word = re.findall(key, i)
            all_replace = re.findall(r'(<\d+?>)', form)
            if len(key_word) != len(all_replace):
                raise value_number_error
            for p in all_replace:
                num = int(re.findall(r'^<(\d+?)>$', p)[0])
                i = re.sub(p, key_word[num], form)
            self.last_names[index] = i
        self._same_name_test()
        self.name_history.append(copy(self.last_names))
        return self.last_names

    def change_name(self, old, new):
        if new in self.last_names:
            raise same_name_error
        self.last_names[self.last_names.index(old)] = new
        self.name_history.append(copy(self.last_names))
        return self.last_names

    def revocation(self):
        if len(self.name_history) != 1:
            self.name_history.pop()
            self.last_names = copy(self.name_history[-1])
            return self.last_names
        else:
            return copy(self.org_name)

    def roll_back(self):
        self.last_names = copy(self.org_name)
        self.name_history.append(copy(self.last_names))
        return self.last_names

    def _same_name_test(self):
        if len(tuple(self.last_names)) != len(self.last_names):
            raise same_name_error


if __name__ == '__main__':
    pass
