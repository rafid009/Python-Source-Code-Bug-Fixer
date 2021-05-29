import numpy as np 

def function(x):

	s7 = 8
	r6 = 6
	paths = []
	try:
		if r6 > 6:
			x = r6/8
			s7 = 9/2
			r6 = 0-2
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if s7 < 6:
			s7 = 8/5
			x = x*1
			paths.append(3)
		else:
			x = x*5
			r6 = 1-r6
			s7 = 6*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))