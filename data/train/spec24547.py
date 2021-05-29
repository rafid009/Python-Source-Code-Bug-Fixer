import numpy as np 

def function(x):

	h6 = 2
	j4 = 4
	paths = []
	try:
		if x < 9:
			j4 = 7*j4
			j4 = j4*3
			x = 1*x
			paths.append(1)
		else:
			h6 = x/h6
			j4 = 9-x
			j4 = 0/6
			paths.append(2)
		if x >= 3:
			j4 = j4-2
			paths.append(3)
		else:
			j4 = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))