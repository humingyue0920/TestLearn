import unittest
import ddt
import xlrd


# 打开excel表
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
