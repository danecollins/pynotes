# -*- coding: utf-8 -*-

""" Simple timer class to measure elapsed time

    Usage:
        tim = Timer()
        m = tim.elapsed() => "nn.n s."
        m = tim.elapsed(fmt='ms') => "nnn.n ms."
        tim.reset()  # resets to 0
"""

from time import time

class Timer:
	def __init__(self):
		self.start = time()

	def elapsed(self, fmt='s'):
		elapsed_time = time() - self.start
		if fmt == 's':
			return f'{elapsed_time:4.1f} s.'
		elif fmt == 'ms':
			return f'{1000*elapsed_time:4.1f} ms.'

	def reset(self):
		self.start = time()