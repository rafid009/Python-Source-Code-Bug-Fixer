import numpy as np 

def function(x):

	j7 = x
	b4 = x
	paths = []
	try:
		if x <= 9:
			j7 = 7/x
			paths.append(1)
		else:
			x = 3+7
			paths.append(2)
		if x < 4:
			x = 4*x
			x = j7*x
			x = b4*x
			paths.append(3)
		else:
			x = x*6
			j7 = j7/j7
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