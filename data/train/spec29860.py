import numpy as np 

def function(x):

	y3 = 0
	s0 = 7
	paths = []
	try:
		if y3 <= 6:
			y3 = y3*x
			paths.append(1)
		else:
			s0 = 5*s0
			y3 = y3*x
			y3 = y3+4
			paths.append(2)
		if y3 > 2:
			x = x*s0
			paths.append(3)
		else:
			s0 = s0*4
			s0 = 7*s0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))