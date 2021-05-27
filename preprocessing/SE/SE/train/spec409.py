import numpy as np 

def function(x):

	s5 = 3
	n1 = x
	paths = []
	try:
		if s5 > 8:
			x = 9/x
			s5 = 1+s5
			n1 = n1-6
			paths.append(1)
		else:
			s5 = 3-6
			paths.append(2)
		if x < 5:
			s5 = 2+0
			paths.append(3)
		else:
			x = 4+8
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