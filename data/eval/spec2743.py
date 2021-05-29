import numpy as np 

def function(x):

	s1 = 6
	n5 = x
	paths = []
	try:
		if x >= 6:
			n5 = n5*n5
			x = 4*x
			s1 = 5-x
			paths.append(1)
		else:
			n5 = 6/n5
			paths.append(2)
		if n5 >= 6:
			s1 = x-6
			paths.append(3)
		else:
			n5 = n5-6
			x = x+7
			x = s1-1
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))