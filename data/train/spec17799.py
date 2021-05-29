import numpy as np 

def function(x):

	k4 = x
	n2 = x
	paths = []
	try:
		if n2 < 8:
			x = 7/9
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x < 0:
			k4 = 5+n2
			n2 = 7/n2
			paths.append(3)
		else:
			n2 = 7+0
			n2 = n2/n2
			k4 = k4+k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))