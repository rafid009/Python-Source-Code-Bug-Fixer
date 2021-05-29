import numpy as np 

def function(x):

	s6 = 1
	n6 = x
	paths = []
	try:
		if x <= 9:
			x = x*5
			n6 = 5*n6
			s6 = s6+6
			paths.append(1)
		else:
			x = 7-x
			n6 = n6-2
			x = 0/1
			paths.append(2)
		if s6 >= 4:
			s6 = s6*4
			paths.append(3)
		else:
			n6 = n6+6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))