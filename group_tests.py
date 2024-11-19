import group
import unittest

class TestCases(unittest.TestCase):
    def testGroupsof3_1(self):
        input = [2,5,3,6,4,1,8,4,3,4,6,2,3]
        expected = [[2,5,3],[6,4,1],[8,4,3],[4,6,2], [3]]
        result = group.groups_of_3(input)
        self.assertEqual(expected, result)

    def testGroupsof3_2(self):
        input = [4,2,7,4,2,3,8,9,0]
        expected = [[4,2,7],[4,2,3],[8,9,0]]
        result = group.groups_of_3(input)
        self.assertEqual(expected, result)

if __name__ == '__main__':
        unittest.main()