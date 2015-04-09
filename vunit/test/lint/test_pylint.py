# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2015, Lars Asplund lars.anders.asplund@gmail.com

"""
Pylint check
"""


import unittest
from subprocess import check_call
from vunit import ROOT
from os.path import join, dirname


class TestPylint(unittest.TestCase):
    """
    Check that there are no pylint errors or warnings
    """
    @staticmethod
    def test_pylint():
        check_call(["pylint",
                    "--disable=too-few-public-methods",
                    "--disable=locally-disabled",
                    "--disable=interface-not-implemented",
                    "--ignore-imports=y",  # Ignore imports from code duplication check
                    "--rcfile=" + join(dirname(__file__), "pylintrc"),
                    join(ROOT, "vunit")])
