import argparse
import unittest

import sys

import main


class TestMain(unittest.TestCase):

    def test_asadfd(self):
        self.assertEqual(main.execute('asadfd'), '3ed340ef38eb08086ea4ab6e0c1d171b')

    def test_asaadfda(self):
        self.assertEqual(main.execute('asaadfda'), '3ed340ef38eb08086ea4ab6e0c1d171b')

    def test_asaadfdt(self):
        self.assertEqual(main.execute('asaadfdt'), '3ed340ef38eb08086ea4ab6e0c1d171b')

    def test_asadfdt(self):
        self.assertRaises(RuntimeError, main.execute('asadfdt'))

if __name__ == '__main__':
    unittest.main()
