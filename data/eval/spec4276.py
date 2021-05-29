import numpy as np 

def function(x):

	n1 = 4
	s7 = x
	x = 2
	paths = []
	try:
		if n1 < 3:
			s7 = s7*2
			paths.append(1)
		else:
			x = 3*x
			n1 = n1+0
			paths.append(2)
		if n1 <= 7:
			s7 = 7/s7
			x = s7/x
			paths.append(3)
		else:
			s7 = s7-2
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		n1 = s7**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))