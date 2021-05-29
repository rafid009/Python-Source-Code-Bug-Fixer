import numpy as np 

def function(x):

	s5 = 0
	n4 = x
	paths = []
	try:
		if x < 9:
			s5 = s5*5
			s5 = s5*s5
			n4 = s5*n4
			paths.append(1)
		else:
			n4 = 1/n4
			n4 = 4+5
			paths.append(2)
		if n4 < 9:
			x = x/8
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))