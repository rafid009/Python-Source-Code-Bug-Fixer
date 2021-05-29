import numpy as np 

def function(x):

	s5 = x
	y4 = 0
	paths = []
	try:
		if s5 >= 0:
			s5 = s5*8
			paths.append(1)
		else:
			s5 = s5-8
			y4 = 2*8
			paths.append(2)
		if s5 > 6:
			x = x-4
			paths.append(3)
		else:
			s5 = s5*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))