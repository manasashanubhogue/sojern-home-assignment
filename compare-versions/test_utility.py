import unittest
from version_utility import compare_versions

class VersionUtilityTestCase(unittest.TestCase):
    def test_version_comparison(self):
        self.assertEqual(compare_versions('0.1', '1.1'), -1)
        self.assertEqual(compare_versions('1.1', '1.2'), -1)
        self.assertEqual(compare_versions('1.2', '1.2.9.9.9.9'), -1)
        self.assertEqual(compare_versions('1.3', '1.3.4'), -1)
        self.assertEqual(compare_versions('1.10', '1.3'), 1)
        self.assertEqual(compare_versions('5.2.9.1', '5.2.9'), 1)

    def test_equal_versions(self):
        self.assertEqual(compare_versions('1.0', '1.0.0'), 0)
        self.assertEqual(compare_versions('2.5', '2.5'), 0)
        self.assertEqual(compare_versions('10.1.2', '10.1.2'), 0)

if __name__ == '__main__':
    unittest.main()