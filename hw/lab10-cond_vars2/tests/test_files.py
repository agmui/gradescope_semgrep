import unittest
import sys
from gradescope_utils.autograder_utils.decorators import weight
from art import *

sys.path.insert(0, '../..')  # adds the hw project dir to the python path
from hw.grading_utils.random_utils import submitted_files


class TestFiles(unittest.TestCase):
    @weight(0)
    def test_submitted_files(self):
        """Check submitted files"""
        print(text2art("[Challenge] Condition Variables 2", "rand"))
        files = ['priority.c', 'threeJobs.c', 'band.c', 'littleredhen.c']
        self.assertEqual(submitted_files(files), 0, 'missing some required files!')