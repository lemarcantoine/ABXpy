"""This file contains test for the examples of the package"""
import os.path as path
import subprocess


examples_folder = path.join(
    path.dirname(path.dirname(path.dirname(path.realpath(__file__)))),
    'examples')


complete_run_sh = path.join(examples_folder, 'complete_run.sh')
complete_run_py = path.join(examples_folder, 'complete_run.py')


def test_complete_run_sh():
    subprocess.check_call(['bash', complete_run_sh])

def test_complete_run_py():
    subprocess.check_call(['python', complete_run_py])
