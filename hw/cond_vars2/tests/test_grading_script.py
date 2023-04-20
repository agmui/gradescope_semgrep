import os
import subprocess
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, partial_credit
from art import *
import asyncio # TODO: add to reqirements.txt


async def async_run_cmd(cmd):
    print("running:", cmd)
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=90)
    except asyncio.TimeoutError:
        return {"code": 1,
                "output": "asyncio.TimeoutError"}

    print("finished:", cmd)
    if stdout:
        return {"code": proc.returncode,
                "output": stdout.decode()}
    if stderr:
        return {"code": proc.returncode,
                "output": stderr.decode()}

async def run():
    return await asyncio.gather(
        async_run_cmd('./inorder'),
        async_run_cmd('./max'),
        async_run_cmd('./prodcons_condvar'),
        async_run_cmd('./rooms'),
        async_run_cmd('./tunnel')
    )


print(text2art("cond vars 2", "rand"))


os.chdir("src")
os.system("make")

print("===starting tests===")
output1, output2, output3, output4, output5 = asyncio.run(run())

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0)
    @number("1")
    def test_make_grade(self):
        """autograder output tests"""
        print(output1)
        print(output2)
        print(output3)
        print(output4)
        print(output5)
        # process = subprocess.Popen(['../src/make grade'], stdout=subprocess.PIPE, encoding='UTF-8')
        # result, error = process.communicate()
        # print(result)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
