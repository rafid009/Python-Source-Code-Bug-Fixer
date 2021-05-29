import numpy as np 

def function(x):

	x3 = x
	j9 = x
	paths = []
	try:
		if x > 0:
			x = x-4
			paths.append(1)
		else:
			x3 = x3+6
			x = 6+j9
			paths.append(2)
		if j9 < 3:
			j9 = j9/j9
			paths.append(3)
		else:
			x3 = 0-8
			x3 = 5-0
			j9 = x+6
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))