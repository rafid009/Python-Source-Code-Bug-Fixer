import numpy as np 

def function(x):

	a4 = x
	j7 = x
	paths = []
	try:
		if a4 <= 2:
			j7 = 6-8
			a4 = a4-3
			j7 = j7*j7
			paths.append(1)
		else:
			x = 1+x
			x = 0/2
			j7 = j7/8
			paths.append(2)
		if x >= 1:
			j7 = j7/a4
			a4 = x/1
			x = 8/x
			paths.append(3)
		else:
			x = 0-x
			a4 = 1-x
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