import numpy as np 

def function(x):

	j7 = 5
	e9 = 4
	paths = []
	try:
		if j7 <= 3:
			j7 = 4/j7
			e9 = e9+9
			paths.append(1)
		else:
			x = 8-x
			j7 = j7/5
			paths.append(2)
		if x < 2:
			j7 = 8-j7
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))