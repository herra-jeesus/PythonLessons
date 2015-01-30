#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ülesanne 8 - Testimine
Juhend: https://courses.cs.ttu.ee/w/images/8/87/2014_Loeng_8_-_Testing.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

import unittest
from Roman_numerals import convert

class Testing(unittest.TestCase):
	"""
	Klass testimiseks
	"""
	def test_1(self):
		self.assertEqual(convert("I"), 1)

	def test_2(self):
		self.assertEqual(convert("IV"), 4)

	def test_3(self):
		self.assertEqual(convert("VI"), 6)

	def test_4(self):
		# Failed: Test Cases missing
		self.assertEqual(convert("XC"), 90)

	def test_5(self):
		# Failed: Syntax faulty
		self.assertEqual(convert("CD"), 399)

	def test_6(self):
		self.assertEqual(convert("MMMMCMXCIX"), 4999)

	def test_7(self):
		self.assertEqual(convert("IIV"), -1)

	def test_8(self):
		self.assertEqual(convert("XXXXX"), -1)

	def test_9(self):
		self.assertEqual(convert("LLCDD"), -1)

	def test_10(self):
		self.assertEqual(convert("blah"), -1)

	def test_11(self):
		# Initially returned "None"
		# Case added
		self.assertEqual(convert(10), -1)

def main():
	unittest.main(verbosity=2)


if __name__ == '__main__':
	main()