import numpy as np 

def function(x):

	x0 = 4
	j7 = 8
	paths = []
	try:
		if x0 < 9:
			x0 = x0*0
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x < 1:
			x = x+6
			x = 3-3
			j7 = j7+6
			paths.append(3)
		else:
			x = x-j7
			x0 = j7-x0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))