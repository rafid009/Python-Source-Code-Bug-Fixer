import numpy as np 

def function(x):

	s4 = 5
	i7 = x
	paths = []
	try:
		if x >= 9:
			x = i7/1
			x = x-s4
			paths.append(1)
		else:
			s4 = i7/7
			paths.append(2)
		if i7 > 8:
			s4 = s4-4
			s4 = s4/4
			i7 = 2*2
			paths.append(3)
		else:
			s4 = 9*s4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))