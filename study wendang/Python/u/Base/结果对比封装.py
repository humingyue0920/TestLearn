# 定义一个类对接口返回数据进行比对
class CommonComparision():
    # 定义一个通用方法，判断一个字符串是否在另一个字符串中
    def is_contain(self, str_01, str_02):
        # str_01 excel表格中存的预期结果字段
        # str_02 接口返回数据
        """
        看视频中的代码报Unicode的错误，会引入python中的一个方法将Unicode类型转换为字符串类型
                if isinstance(str_01, unicode):
            str_01 = str_01.encode('unicode-escape').decode('string_escape')
        写进代码里报错，可能现在已经没有Unicode类型的数据了
        """
        flag = None
        if str_01 in str_02:
            flag = True
        else:
            flag = False
        return flag

