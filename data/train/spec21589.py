import numpy as np 

def function(x):

	j6 = x
	e9 = 3
	paths = []
	try:
		if x > 7:
			j6 = e9/j6
			paths.append(1)
		else:
			x = x*e9
			e9 = e9*4
			e9 = e9*j6
			paths.append(2)
		if j6 > 6:
			x = j6*7
			paths.append(3)
		else:
			e9 = 6*j6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))