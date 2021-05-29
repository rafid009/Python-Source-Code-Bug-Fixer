import numpy as np 

def function(x):

	i7 = 2
	q3 = x
	paths = []
	try:
		if q3 <= 7:
			q3 = 6+q3
			paths.append(1)
		else:
			i7 = 3/x
			i7 = 8/6
			q3 = q3/q3
			paths.append(2)
		if x < 8:
			x = x/7
			x = 1/x
			i7 = 8+i7
			paths.append(3)
		else:
			q3 = 6*q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))