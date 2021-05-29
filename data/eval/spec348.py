import numpy as np 

def function(x):

	a7 = 2
	s7 = x
	paths = []
	try:
		if a7 >= 7:
			s7 = s7+x
			x = 4-s7
			paths.append(1)
		else:
			x = s7/x
			paths.append(2)
		if a7 < 5:
			a7 = a7+1
			a7 = 0*a7
			paths.append(3)
		else:
			s7 = s7+x
			s7 = s7-a7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))