import numpy as np 

def function(x):

	s4 = 4
	k4 = 2
	paths = []
	try:
		if k4 > 2:
			k4 = k4*s4
			x = x-s4
			paths.append(1)
		else:
			x = x+k4
			s4 = s4-0
			paths.append(2)
		if x < 7:
			s4 = s4*2
			paths.append(3)
		else:
			s4 = 1+s4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))