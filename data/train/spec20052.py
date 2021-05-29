import numpy as np 

def function(x):

	n8 = 5
	s8 = x
	paths = []
	try:
		if s8 >= 1:
			x = x+2
			s8 = 9-s8
			s8 = s8+2
			paths.append(1)
		else:
			n8 = 3-x
			paths.append(2)
		if n8 <= 9:
			x = n8/x
			n8 = n8-n8
			paths.append(3)
		else:
			x = 5+s8
			n8 = n8/x
			x = 1/s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))