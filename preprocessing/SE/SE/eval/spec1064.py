import numpy as np 

def function(x):

	j0 = x
	a3 = 7
	paths = []
	try:
		if a3 > 4:
			x = 1-x
			j0 = j0-5
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if a3 <= 1:
			j0 = 9-j0
			paths.append(3)
		else:
			x = j0-0
			j0 = 1*7
			j0 = j0+x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		a3 = j0**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))