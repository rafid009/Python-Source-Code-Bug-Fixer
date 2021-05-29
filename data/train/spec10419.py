import numpy as np 

def function(x):

	s7 = x
	a4 = 0
	paths = []
	try:
		if s7 > 6:
			s7 = a4-x
			paths.append(1)
		else:
			s7 = 4*s7
			a4 = a4-8
			paths.append(2)
		if x < 2:
			s7 = x/s7
			a4 = a4/2
			x = s7-x
			paths.append(3)
		else:
			a4 = x+3
			a4 = a4-9
			x = x+1
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