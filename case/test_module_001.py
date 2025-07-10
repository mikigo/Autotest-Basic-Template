from method.method import Method
from case.base_case import BaseCase

class TestMyCase(BaseCase):

    def test_mycase_001(self):
        """this is my test case title"""
        # 用例步骤，调用方法层封装好的方法进行操作
        Method().click_dde_file_manager_on_dock_by_attr()
        # 在关键节点进行断言
        self.assert_true(True)