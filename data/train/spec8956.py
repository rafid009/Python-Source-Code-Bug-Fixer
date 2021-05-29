import numpy as np 

def function(x):

	s7 = 4
	q7 = 8
	paths = []
	try:
		if q7 >= 1:
			x = x/6
			s7 = 8*9
			s7 = 7/s7
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x <= 9:
			s7 = x/4
			paths.append(3)
		else:
			x = 6+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))