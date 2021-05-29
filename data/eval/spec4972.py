import numpy as np 

def function(x):

	s8 = x
	p3 = x
	paths = []
	try:
		if p3 > 9:
			s8 = 2+s8
			s8 = 0/s8
			paths.append(1)
		else:
			s8 = 0/8
			p3 = 5+s8
			paths.append(2)
		if x < 5:
			x = x*p3
			s8 = 0-s8
			p3 = 6/p3
			paths.append(3)
		else:
			x = x+p3
			x = 3-x
			p3 = 8/p3
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