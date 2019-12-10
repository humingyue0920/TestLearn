# 封装一个类获取Excel中的常量


class GlobalVar:
    case_id = '0'
    name = '1'
    condition = '2'
    execute = '4'
    requests_type = '5'
    header = '6'


def get_case():
    return GlobalVar.case_id


def get_name():
    return GlobalVar.name


def is_execute():
    return GlobalVar.execute


def get_requests_type():
    return GlobalVar.requests_type


def get_header():
    return GlobalVar.header
