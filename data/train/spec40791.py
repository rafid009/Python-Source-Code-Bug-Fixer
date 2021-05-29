import numpy as np 

def function(x):

	b7 = x
	j7 = x
	paths = []
	try:
		if x <= 2:
			x = j7*x
			paths.append(1)
		else:
			j7 = b7*x
			paths.append(2)
		if j7 >= 2:
			j7 = j7/6
			paths.append(3)
		else:
			x = 8/x
			j7 = 7*j7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))