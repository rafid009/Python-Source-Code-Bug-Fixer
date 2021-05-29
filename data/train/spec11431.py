import numpy as np 

def function(x):

	j9 = 0
	j4 = x
	paths = []
	try:
		if j9 <= 9:
			j9 = j9+0
			paths.append(1)
		else:
			j9 = 5*j9
			j4 = 8-6
			j4 = 8-x
			paths.append(2)
		if x <= 7:
			j4 = 4-j4
			j9 = j9-6
			j9 = 8*j9
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))