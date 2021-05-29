import numpy as np 

def function(x):

	e6 = 5
	j7 = x
	paths = []
	try:
		if x > 6:
			j7 = j7+6
			paths.append(1)
		else:
			j7 = 0-j7
			paths.append(2)
		if j7 > 6:
			e6 = e6-x
			x = x-j7
			j7 = j7*1
			paths.append(3)
		else:
			x = x+0
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