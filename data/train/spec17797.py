import numpy as np 

def function(x):

	j9 = x
	l8 = 9
	paths = []
	try:
		if j9 <= 0:
			x = x*9
			paths.append(1)
		else:
			j9 = 9+j9
			j9 = j9*9
			paths.append(2)
		if j9 < 0:
			l8 = x/2
			paths.append(3)
		else:
			l8 = 9/l8
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