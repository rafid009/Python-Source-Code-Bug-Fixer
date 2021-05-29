import numpy as np 

def function(x):

	s8 = 5
	n1 = 4
	paths = []
	try:
		if n1 >= 8:
			n1 = n1/9
			s8 = s8+3
			paths.append(1)
		else:
			s8 = s8+0
			paths.append(2)
		if n1 < 9:
			s8 = 9/s8
			n1 = 4*n1
			n1 = n1*6
			paths.append(3)
		else:
			x = s8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))