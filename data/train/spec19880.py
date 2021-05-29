import numpy as np 

def function(x):

	j4 = x
	e7 = x
	paths = []
	try:
		if x > 1:
			x = x-e7
			j4 = 5+j4
			paths.append(1)
		else:
			j4 = j4+j4
			paths.append(2)
		if x <= 5:
			j4 = x-j4
			e7 = e7+3
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))