import numpy as np 

def function(x):

	u2 = x
	j7 = x
	paths = []
	try:
		if x >= 5:
			u2 = u2-u2
			u2 = u2/3
			paths.append(1)
		else:
			j7 = j7*j7
			u2 = 8-u2
			paths.append(2)
		if u2 >= 1:
			u2 = 3/u2
			paths.append(3)
		else:
			u2 = 2-4
			j7 = u2-j7
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