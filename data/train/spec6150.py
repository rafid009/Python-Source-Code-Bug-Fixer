import numpy as np 

def function(x):

	n4 = 1
	s7 = 5
	paths = []
	try:
		if n4 < 7:
			n4 = n4-s7
			paths.append(1)
		else:
			s7 = 5+x
			paths.append(2)
		if x > 9:
			s7 = s7+8
			paths.append(3)
		else:
			x = 8-s7
			n4 = n4-s7
			s7 = 6+0
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))