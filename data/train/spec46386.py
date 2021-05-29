import numpy as np 

def function(x):

	e3 = x
	j7 = 0
	paths = []
	try:
		if x <= 2:
			x = x-6
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if e3 <= 6:
			x = 2*2
			x = j7*x
			j7 = 0-4
			paths.append(3)
		else:
			j7 = x*9
			x = 8/j7
			j7 = j7-e3
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))