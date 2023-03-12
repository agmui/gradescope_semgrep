import os
import re
import subprocess
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, partial_credit
from art import *

os.chdir("src")


# os.system("apt install cowsay")
class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0)
    @number("1")
    def test_make_grade(self):
        """autograder us1tests.c tests"""
        print(text2art("simple shell", "rand"))
        print("====================")
        print("NOTE: bc python is dumb this will not look nice but still will be correct")
        print("====================")
        os.system("make")
        process = subprocess.Popen("cat input.txt | ./simpleshell", stdout=subprocess.PIPE, encoding='UTF-8',
                                   shell=True)
        result, error = process.communicate()
        print(result)
        # f = open("output.txt")
        # file = f.read()
        # f.close()
        # print(file)

        process.wait()
        # testing for zombies
        process = subprocess.Popen(["ps", "-a"], stdout=subprocess.PIPE, encoding='UTF-8')
        zombie_result, error = process.communicate()
        print("========checking for zombies============")
        print(zombie_result)
        result_arr = result.split('\n')
        if "simpleshell" in zombie_result or "donothing" in zombie_result:
            self.assertTrue(False, "simpleshell or donothing is a zombie and did not exit")

        print("========other tests============")
        lines = [i for i, l in enumerate(result_arr) if "PID" in l]
        found_donothing = False
        for i in range(9):
            if "donothing" in result_arr[lines[1] + i]:
                print("found do nothing")
                found_donothing = True
        self.assertTrue(found_donothing, "donothing did not run")

        for i in range(9):
            if "donothing" in result_arr[lines[2] + i]:
                print("found zombie")
                self.assertTrue(False, "found zombie")
        self.assertTrue('exit' in result)


if __name__ == '__main__':
    unittest.main()
