import argparse
import unittest

import sys

import main


class TestMain(unittest.TestCase):

    def test_asadfd(self):
        self.assertEqual(main.execute('asadfd'), 'b2bcb52072cb6fc9ed64080a151d4f6e')

    def test_asaadfda(self):
        self.assertEqual(main.execute('asaadfda'), 'f9cd2e11ccff25c7f606c537ece64d7a')

    def test_asaadfdt(self):
        self.assertEqual(main.execute('asaadfdt'), '27e54f02238a80ed60bf055f07ce37a9')

    def test_asadfdt(self):
        self.assertRaises(RuntimeError, main.execute('asadfdt'))

if __name__ == '__main__':
    unittest.main()
