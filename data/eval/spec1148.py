import numpy as np 

def function(x):

	a6 = x
	s2 = 2
	paths = []
	try:
		if a6 > 6:
			a6 = a6*a6
			x = x-9
			a6 = a6/3
			paths.append(1)
		else:
			x = 8/a6
			a6 = a6/s2
			paths.append(2)
		if x <= 4:
			x = s2+s2
			paths.append(3)
		else:
			s2 = s2+5
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))