import numpy as np 

def function(x):

	b2 = 2
	s8 = x
	paths = []
	try:
		if b2 > 5:
			x = 1/b2
			paths.append(1)
		else:
			b2 = b2/8
			x = x/5
			paths.append(2)
		if b2 >= 0:
			s8 = s8/9
			paths.append(3)
		else:
			b2 = b2-8
			b2 = b2-6
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))