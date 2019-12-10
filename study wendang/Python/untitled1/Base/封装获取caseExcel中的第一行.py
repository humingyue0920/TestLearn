from Base.重构封装Excel import InterfaceCase


class GlobalVar():
    # run = InterfaceCase()
    # case_id = run.get_cell(0, 0)
    # name = run.get_cell(0, 1)
    # option = run.get_cell(0, 2)
    # url = run.get_cell(0, 3)
    # header = run.get_cell(0, 4)
    # parameter = run.get_cell(0, 5)
    # request_way = run.get_cell(0, 6)
    # expection = run.get_cell(0, 7)
    # actual_ex = run.get_cell(0, 8)
    # excute = run.get_cell(0, 9)

    case_id = 0
    name = 1
    option = 2
    url = 3
    header = 4
    parameter = 5
    request_way = 6
    expection = 7
    actual_ex = 8
    is_excute = 9
    dependent_id = 10
    dependent_response_value = 11
    dependent_value = 12

    def get_case_id(self):
        return GlobalVar.case_id

    def get_name(self):
        return GlobalVar.name

    def get_option(self):
        return GlobalVar.option

    def get_url(self):
        return GlobalVar.url

    def get_header(self):
        return GlobalVar.header

    def get_parameter(self):
        return GlobalVar.parameter

    def get_request_way(self):
        return GlobalVar.request_way

    def get_expection(self):
        return GlobalVar.expection

    def get_actual_ex(self):
        return GlobalVar.actual_ex

    def get_is_excute(self):
        return GlobalVar.is_excute

    def get_header_value(self):
        data = {
            "header_name":"riu",
            "value":"434"
        }
        return data






