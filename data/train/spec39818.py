import numpy as np 

def function(x):

	s4 = 1
	a5 = 2
	paths = []
	try:
		if a5 < 9:
			s4 = x-s4
			x = 1/x
			x = 1+s4
			paths.append(1)
		else:
			s4 = s4+3
			a5 = 5*a5
			paths.append(2)
		if x >= 2:
			x = x-x
			x = 6-s4
			paths.append(3)
		else:
			a5 = 0+8
			a5 = 2+a5
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		a5 = s4**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))