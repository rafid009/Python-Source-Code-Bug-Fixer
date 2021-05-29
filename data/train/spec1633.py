import numpy as np 

def function(x):

	j6 = x
	e4 = 0
	paths = []
	try:
		if x > 4:
			e4 = 7-e4
			x = e4-x
			paths.append(1)
		else:
			j6 = j6/x
			paths.append(2)
		if x <= 7:
			j6 = j6*x
			x = 9/x
			e4 = x*j6
			paths.append(3)
		else:
			j6 = x-3
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))