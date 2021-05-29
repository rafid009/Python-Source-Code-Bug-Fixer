import numpy as np 

def function(x):

	s4 = 4
	q9 = 6
	paths = []
	try:
		if q9 < 4:
			q9 = x/x
			paths.append(1)
		else:
			s4 = 1+q9
			s4 = 3/s4
			paths.append(2)
		if q9 < 6:
			x = 6*x
			q9 = 7/x
			x = 7+x
			paths.append(3)
		else:
			s4 = x-4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))