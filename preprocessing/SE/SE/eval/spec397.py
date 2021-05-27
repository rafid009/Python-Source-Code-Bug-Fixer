import numpy as np 

def function(x):

	s0 = 0
	n8 = x
	paths = []
	try:
		if n8 <= 2:
			x = x+5
			paths.append(1)
		else:
			n8 = 9-7
			x = x/4
			s0 = n8-9
			paths.append(2)
		if n8 < 2:
			s0 = n8-1
			s0 = s0-1
			paths.append(3)
		else:
			s0 = n8+s0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))